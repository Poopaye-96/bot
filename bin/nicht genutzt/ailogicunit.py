# -*- coding: utf-8 -*-
"""
Created on Fri May 19 16:02:27 2023

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
#from . import speechrecmod as sr
#from . import pyttsx3mod as tts
#from . import browsermod as bm
#from . import wikimod as wiki
#from . import walphamod as wa
import os


def logic(activationWord:str):
    query = sr.parse_speech().lower().split()
    
    if query[0] == activationWord:
        query.pop(0)
        
        # open website
        if query[0] == 'öffne' and query[1] == 'die' and query[2] == 'website':
            tts.tts.speak('Einen Moment bitte...')
            query = ' '.join(query[3:])
            query = query.replace(' ', '')
            try:
                bm.get_pc_browser('firefox', query)
            except Exception as error:
                print(f'Ich konnte die Website {query} nicht finden!' + 
                      f' Fehlermeldung:: {error}')
                tts.tts.speak(f'Ich konnte die Website {query} nicht finden!')
                
        # search wikipedia
        if query[0] == 'erkläre':
            tts.speak('Ich durchsuche Wikipedia...')
            query = ' '.join(query[1:])
            tts.speak(wiki.searchWikipedia(query))
            
        # calculate on wolfram alpha
        if query[0] == 'berechne':
            query = ' '.join(query[1:])
            tts.speak('Ich berechne...')
            try:
                tts.speak(wa.searchWolframalpha(query))
            except Exception as error:
                print(f'Ein Berechnungsfehler wurde erkannt. Fehlermeldung: {error}')
                tts.speak('Ein Berechnungsfehler wurde erkannt.')
        
        # exit
        if query[0] == 'shutdown':
            tts.speak('Speichern und herunterfahren!')
            return False
        

if __name__ == '__main__':
    load_conf()