import os, logging
from enum import Enum

# main
ROOT = os.path.dirname(os.path.abspath(__file__))
ROOT_OF_ROOT = os.path.dirname(os.path.abspath(ROOT))
KRYSTAL = os.path.join(ROOT, 'krystal.py')
accessURL = 'http://www.able.digital/access'

# krystal
VERSION = '0.90.4'
TEMP_UPDATE_DIR = os.path.join(ROOT, 'krystal-master/') # grabbing zipfile path, this cannot be changed
GRAB_USER_INFO = os.path.join(ROOT_OF_ROOT, 'userinfo.json') # userinfo.json temp location during update
CONFIGJSON = os.path.join(ROOT, 'engine/etc/userinfo.json') # userinfo.json file location after update / original loc
ENGINE_DIR = os.path.join(ROOT, 'engine/etc/')
DEFKEY = '23Able'

# model
TRAINDATA = os.path.join(ROOT, 'model/train/traindata.json')
TESTDATA = os.path.join(ROOT, 'model/test/testdata.json')
TRAIN_FACES_DIR = os.path.join(ROOT, 'model/train')
TEST_FACES_DIR = os.path.join(ROOT, 'model/test')
FACES_MODEL = os.path.join(ROOT, 'model/faces.ai')
AUDIOMODEL = os.path.join(ROOT, 'model/Krystal.pmdl')
DET_PROTOTXT = os.path.join(ROOT, 'model/MobileNetSSD.prototxt.txt')
DET_MODEL = os.path.join(ROOT, 'model/MobileNetSSD.caffemodel')

# logs
EVENT_LOG = os.path.join(ROOT, 'engine/etc/events.log') # this file will be sent to Able Inc for diagnostics

# conversation
PERSONMODEL = os.path.join(ROOT, 'conversation/krystal_beta_model')
PERSONMODEL_TRAIN = os.path.join(ROOT, 'conversation/training_data')
PERSONMODEL_JSON = os.path.join(ROOT, 'conversation/personality.json')
PERSONMODEL_LOG = os.path.join(ROOT, 'conversation/tflearn_logs')

# Memory Engine
MEMORY_NEWINFORMATION = os.path.join(ROOT, 'memory/newInformation.json')

# create necessary files and directories
if not os.path.exists(TEST_FACES_DIR or ENGINE_DIR):
    os.makedirs(TEST_FACES_DIR)
    os.makedirs(ENGINE_DIR)
elif not os.path.isfile(EVENT_LOG):
    W = open(EVENT_LOG, 'w')
    W.close()


# Endpoints for Able Inc. API
class Endpoints(Enum):
    conversations = 'http://able.digital/krystal/api/conversations'
    notification = 'http://able.digital/krystal/api/push'
    system = 'http://able.digital/krystal/api/system'
    users = 'http://able.digital/krystal/api/users'
    localHost = 'http://localhost:3000/'  # developer purposes - do not remove



# pre-processed
# ERROR_LOGGER = logging.basicConfig(filename=EVENT_LOG, format='%(asctime)s:%(levelname)s:%(message)s', level=logging.ERROR)
# DEBUG_LOGGER = logging.basicConfig(filename=EVENT_LOG, format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
# INFO_LOGGER = logging.basicConfig(filename=EVENT_LOG, format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
# WARNING_LOGGER = logging.basicConfig(filename=EVENT_LOG, format='%(asctime)s:%(levelname)s:%(message)s', level=logging.WARNING)
