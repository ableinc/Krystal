# things we need for NLP
import warnings
from os import environ

import nltk
from nltk.stem.lancaster import LancasterStemmer

environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
warnings.filterwarnings('ignore', '', category=RuntimeWarning)
warnings.filterwarnings('ignore', '', category=FutureWarning)

import numpy as np
import tflearn
import random
import pickle
import json
from root import PERSONMODEL, PERSONMODEL_TRAIN, PERSONMODEL_JSON, PERSONMODEL_LOG

# restore all of our data structures
stemmer = LancasterStemmer()
data = pickle.load(open(PERSONMODEL_TRAIN, "rb"))
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']
import site

site.setquit()
# import our chat-bot intents file
with open(PERSONMODEL_JSON) as json_data:
    intents = json.load(json_data)

# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Define models and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir=PERSONMODEL_LOG)


def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)

    return np.array(bag)


# p = bow("what is your name?", words)
# print(p)
# print(classes)

# load our saved models
model.load(PERSONMODEL)

# create a data structure to hold user context
context = {}
ERROR_THRESHOLD = 0.75


def classify(sentence):
    # generate probabilities from the models
    results = model.predict([bow(sentence, words)])[0]
    # filter out predictions below a threshold
    results = [[i, r] for i, r in enumerate(results) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # return tuple of intent and probability
    return return_list


def response(sentence, userid='krystal', show_details=False):
    results = classify(sentence)
    # if we have a classification then find the matching intent tag
    if results:
        # loop as long as there are matches to process
        while results:
            for i in intents['personality']:
                # find a tag matching the first result
                if i['tag'] == results[0][0]:
                    # set context for this intent if necessary
                    if 'context_set' in i:
                        if show_details:
                            print('context:', i['context_set'])
                        context[userid] = i['context_set']

                    # check if this intent is contextual and applies to this user's conversation
                    if not 'context_filter' in i or (userid in context and 'context_filter' in i and i['context_filter'] == context[userid]):
                        # if show_details:
                        #     print('tag:', i['tag'])
                        # a random response from the intent
                        text = ''.join(random.choice(i['responses']))
                        return text

            results.pop(0)

