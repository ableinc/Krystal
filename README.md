# Krystal
- Author: Able (Jaylen Douglas)
- Platform: MacOS (Windows & Linux Support in the future)<br>
- Version: 0.90.1<br>
- Required: <i>tensorflow>=1.5, pyaudio, spacy, opencv-python, face_recognition, speechrecognition, tflearn, beautifulsoup</i><br><br>
Krystal is intended to act as an intelligent friend you can always go to for a good conversation. 
She will learn you as a person and will accompany you when there may not be anyone else. <br><br>
Krystal is in <b>Beta</b> testing 
now and you should not expect full functionality from her. Some features have been deprecated but may still show in the code. She will will be updated with algorithms that will achieve the goal of an artificially intelligent friend. Right now she is very basic but that is the point. 
# Use
To use Krystal please register for an account on <a href="https://ableinc.us/access">Able Access</a>, there you will receive
your own Able Access ID. This ID grants you access to all of Able's latest software.
<br>
# Starting Krystal: 
Interacting with Krystal starts with: <i>"Hey Krystal" or "Krystal"</i><br>
Accepted commands:
<br>
1) What is your name?<br>
2) Who is Barack Obama?<br>
3) Who is that? (This uses face recognition to detect who's in front of the camera - Training required)<br>
4) What is that? (This uses object detection to detect what object is in front of the camera - No training required)<br>
# Training
Tensorflow 1.5 is required for Krystal. To train Krystal on faces close to your heart create a folder with the name of the face
 within the "train" directory (Model > Train > "persons name" folder) and run the 'facerectrain.py' script. Then she will
 be ready to use out of the box. Please use clear images, no filters or facial effect...yes, no duck lips.
<br>
# First start:
1) Clone or download the zip file for Krystal<br>
2) Run 'depends.py'<br>
3) Then run Krystal.py (Remember that an Able Access ID is required to use Krystal.) <br>

# Features (In-Detail)
<h2>Face Detection (Vision)</h2>
Krystal comes with a unique feature that allows her to detect whomever you desire with a blink of an eye (well, a captured frame but you get my point). She uses the well-designed source code of Ageitgey's <a href="https://github.com/ageitgey/face_recognition">Face Recognition</a>software. As described above and in Ageitgrey's example code which Krystal uses in order for her to known the names of the detected faces in the image you must train a model that will contain the information for each individual person name (described as the folder name/label). The training script is contained within the "model" folder, the file is called facerectrain.py. Special thanks to Ageitgrey.
<br>
<h2>Object Detection</h2>
Krystal also comes with an pre-trained caffee model that contains a few commonly present or easily trained images. The images are general and there is a good chance of misidentification of abstract or unqiue objects. You can see the exact images the model can detect by checking the resources > Detection.py file. 
<br>
<h2>Personality</h2>
Krystal contains a very simple personality model that contains general information about her such as her name, age or creator. She information is only invoked when a specific or relative question is asked with a high probability of matching a tag. She will generate a random response pre-programmed into the model. As stable updates are released in the coming time Krystal's personality model with expand with complexity and will begin to adapt to conversation in real-time as an artificially intellegent "human" or android for this purpose. Feel free to add information about krystal as much as please, though in the future it will be recommended that you not do so. In later updates, specifically speaking, the "environmental adaption" algorithm will be added to Krystal, this algorithm will gather information Krystal doesn't already know and add it to the training file for training at a later period. Krystal is intended to always be running and will only gather information when activated, when she is terminated she will retrain on restart before continuing normal functionality.<br>

# Known issues
1) Q: Random info when asked about who/what someone/something.<br>
   A: This is due to a less than stable algorithm that parses the web for information on what you're searching for.<br>
2) Q: No file found named _snowboydetect.so<br>
   A: You may need to grab a precombiled build for Snowboy (follow their instructions <a href="https://github.com/Kitt-AI/snowboy">here</a>) then add the correct files to the "SBpy3" folder. Also you could be running Krystal on an unsupprted platform
