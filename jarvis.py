from datetime import datetime
from distutils.cmd import Command
from multiprocessing.connection import Listener
import speech_recognition as sr
import pyttsx3
import pywhatkit

Listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk():
  engine.say('Hey ! I Am Your assistant')
  engine.say('How can I help You??')
  engine.runAndWait()

def take_command():
    try:
       with sr.Microphone() as source:
         print("Listening.....")
         voice = Listener.listen(source)
         Command =Listener.recognize_google(voice)
         Command = Command.lower()
         print(Command)
    except:
     pass
    return Command

def run_assi():
    Command = take_command()

    if 'play' in Command:
       song = Command.replace('play', '')
       engine.say('Playing' + song)
       engine.runAndWait()
       print('playing....' + song)
       pywhatkit.playonyt(song)
    elif 'send' in Command:
      mssg = Command.replace('send', '')
      engine.say('Sending' + mssg)
      engine.runAndWait()
      print('Sending....' + mssg)
      # pywhatkit.sendwhats_image("+917999690339", "./img.png")
      pywhatkit.sendwhatmsg("+917999690339", "Hi Karan", 17, 42)
      
run_assi()