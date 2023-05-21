# -*- coding: utf-8 -*-
"""
Created on Fri May 19 18:25:17 2023

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

import wolframalpha

# init wolfram alpha
appid =  '5TE4H2-U3RPG8PPQL'
wolframClient = wolframalpha.Client(app_id = appid)

# list or dict
def listOrDict(var):
    if isinstance(var, list):
        return var[0]['plaintext']
    else:
        return var['plaintext']
    
# search wolfram alpha
'''
Wolfram|Alpha v2.0 client

Basic usage is pretty simple. Get your App ID at
https://products.wolframalpha.com/api/.
Create the client with your App ID:

>>> app_id = getfixture('API_key')
>>> client = Client(app_id)

Send a query, which returns Results objects:

>>> res = client.query('temperature in Washington, DC on October 3, 2012')

Result objects have `pods` (a Pod is an answer group from Wolfram Alpha):

>>> for pod in res.pods:
...     pass  # do_something_with(pod)

Pod objects have ``subpods`` (a Subpod is a specific response
with the plaintext reply and some additional info):

>>> for pod in res.pods:
...     for sub in pod.subpods:
...         print(sub.plaintext)
temperature | Washington, District of Columbia
Wednesday, October 3, 2012
(70 to 81) °F (average: 75 °F)
...

To query simply for the pods that have 'Result' titles or are
marked as 'primary' using ``Result.results``:

>>> print(next(res.results).text)
(70 to 81) °F (average: 75 °F)
(Wednesday, October 3, 2012)

All objects returned are dictionary subclasses, so to find out which attributes
Wolfram|Alpha has supplied, simply invoke ``.keys()`` on the object.
Attributes formed from XML attributes can be accessed with or without their
"@" prefix (added by xmltodict).
'''
def searchWolframalpha(query:str = ''):
    result = wolframClient.query(query)
    if result['@success'] == 'false':
        return 'Die Anfrage konnte nicht berechnet werden.'
    else:
        pod0 = result['pod'][0]
        pod1 = result['pod'][1]
        if (('result') in pod1['@title'].lower()) or (pod1.get('@primary', 'false') == 'true') or ('definition' in pod1['@title'].lower()):
            result = listOrDict(pod1['subpod'])
            # Remove the bracketed section
            return result.split('(')[0]
        else: 
            question = listOrDict(pod0['subpod'])
            # Remove the bracketed section
            return question.split('(')[0]