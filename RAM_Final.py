"""
Name: Mehul Khedekar
RUID: 182000013
This code is written and complied in Python 3
"""
import json
import random
import requests


def get_random_ep():
    """
    Returns two random values to make a random episode Name
    """
    episode = ["Pilot", "Lawnmower", "Dog", "Anatomy", "Park", "M. Night", "Shaym-Aliens", "Meeseeks", "Destroy", "Rick", "Potion #9", "Raising", "Gazorpazorp", "Rixty", "Minutes", "Something", "Ricked", "This", "Way", "Comes", "Close", "Rick-counters", "Rick Kind", "Ricksy Business", "Rickle", "Time", "Mortynight", "Run", "Auto", "Erotic", "Assimilation", "Total", "Rickall", "Get", "Schwifty", "Ricks", "Crazy", "Big", "Trouble", "Little", "Sanchez", "Interdimensional", "Cable", "Tempting", "Fate", "Look", "Purging", "Wedding", "Squanchers", "Rickshank", "Rickdemption", "Rickmancing", "Stone", "Pickle", "Vindicators", "Return", "Worldender", "Whirly", "Dirly", "Conspiracy", "Rest", "Ricklaxation", "Ricklantis", "Mixup", "Morty’s", "Mind", "Blowers", "ABC’s", "Beth", "Rickchurian", "Mortydate"]
    random1 = random.choice(episode)
    random2 = random1
    while (random1 == random2):
        random2 = random.choice(episode)
    return [random1,random2]

try:
    #Trying to connect with the api, if it is not connected the rpogram will terminate itself
    req = requests.get("https://rickandmortyapi.com/api/episode/" + str(random.randint(1,32)), timeout = 4)
except:
    print("Connection error")
    exit()

j = json.loads(req.text)

name = get_random_ep()
#printing the random episode name
print("Name: " + name[0] + " " + name[1])
#Random episode description
with open("desc.txt", 'r') as f:
    print(random.choice(f.read().split('\n')))

x = random.choice(j['characters'])
random_character = requests.get(x, timeout = 4)
jj = json.loads(random_character.text)
#Printing all character info from the given API
print("Character name:\t" + jj['name'])
print("Status:\t\t" + jj['status'])
print("Species:\t" + jj['species'])
print("Origin:\t\t" + jj['origin']['name'])

with open("quotes.txt", 'r') as f:
    #Quotes from the series randomly selected
    print(random.choice(f.read().split('\n')))
