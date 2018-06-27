# IOT-project

Video demo: https://youtu.be/UQP0GKG_zJc

First, when you need to use python to voice control raspberry pi,you should pip install SpeechRecognition.

SpeechRecognition:https://pypi.org/project/SpeechRecognition/

To quickly try it out, run python -m speech_recognition after installing.

PyAudio is required if and only if you want to use microphone input (Microphone). PyAudio version 0.2.11+ is required, as earlier versions have 
known memory management bugs when recording from microphones in certain situations.

PyAudio:http://people.csail.mit.edu/hubert/pyaudio/#downloads

pip will download the PyAudio source and build it for your system. Be sure to install the portaudio library development package (portaudio19-dev) and the python development package (python-all-dev) beforehand

portaudio19-dev:https://people.csail.mit.edu/hubert/pyaudio/

Python 3 Artificial Intelligence: Offline STT and TTS,you can also use this to turn voice into text.

STT and TTS:https://stackoverflow.com/questions/34624277/python-3-artificial-intelligence-offline-stt-and-tts/43489811

When you are using your raspberry pi, you may encounter AttributeError: 'module' object has no attribute 'Recognizer'

Then,you can refer to the following discussion to solve it(rename your script ):
https://stackoverflow.com/questions/13813164/python-import-random-error

https://stackoverflow.com/questions/35576521/attributeerror-module-object-has-no-attribute-recognizer

Finally, print out the text converted from the voice.
use "if & else" to determine the content of voice commands printed to control your raspberry pi's basic operations.
