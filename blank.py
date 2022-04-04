

import pyttsx3



engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[2].id)




def say(message):
    engine.say(message)
    engine.runAndWait()


say("good morning sir")
