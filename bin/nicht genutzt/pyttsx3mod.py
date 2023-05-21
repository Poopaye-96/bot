# -*- coding: utf-8 -*-
"""
Created on Fri May 19 18:33:09 2023

@author: Poopaye-96
░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░░░░░
░░░░░▄▄▄▄█▀▀▀░░░░░░░░░░░░▀▀██░░░░░░░░░░░
░░▄███▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄░░░░░░░
▄▀▀░█░░░░▀█▄▀▄▀██████░▀█▄▀▄▀████▀░░░░░░░
█░░░█░░░░░░▀█▄█▄███▀░░░░▀▀▀▀▀▀▀░▀▀▄░░░░░
█░░░█░▄▄▄░░░░░░░░░░░░░░░░░░░░░▀▀░░░█░░░░
█░░░▀█░░█░░░░▄░░░░▄░░░░░▀███▀░░░░░░░█░░░
█░░░░█░░▀▄░░░░░░▄░░░░░░░░░█░░░░░░░░█▀▄░░
░▀▄▄▀░░░░░▀▀▄▄▄░░░░░░░▄▄▄▀░▀▄▄▄▄▄▀▀░░█░░
░█▄░░░░░░░░░░░░▀▀▀▀▀▀▀░░░░░░░░░░░░░░█░░░
░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄██░░░░
░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░▄▀▀░░░▀█░░
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░█▀▄ █▀▀ █▀█ █░░░░█░▄░█ █ ▀█▀ █░█░░█ ▀█▀░█
█░░█░█ █▀▀ █▀█ █░░░░▀▄▀▄▀ █ ░█░ █▀█░░█ ░█░░█
█░░▀▀░ ▀▀▀ ▀░▀ ▀▀▀░░░▀░▀░ ▀ ░▀░ ▀░▀░░▀ ░▀░░█
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
A new file doing easy things complicated! 
"""

import pyttsx3


# init speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    if "German" in voice.name:
        engine.setProperty('voice', voice.id)
        break
    
# speak text --> Lautstärke (0.0 bis 1.0) 
#                Geschwindigkeit (normalerweise 100)
#                Tonhöhe (0.5 bis 2.0)
def speak(text:str = '', volume:int = 1, rate:int = 150, pitch:int = 1):
    engine.setProperty('volume', volume)  
    engine.setProperty('rate', rate)
    engine.setProperty('pitch', pitch)
    engine.say(text)
    engine.runAndWait()