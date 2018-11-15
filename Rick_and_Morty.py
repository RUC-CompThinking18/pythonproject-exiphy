import json
import random
import requests

req = requests.get("https://rickandmortyapi.com/api/episode/" + str(random.randint(1,32)), timeout = 4)

j = json.loads(req.text)

print("Name:\t\t" + j['name'])
print("Air Date:\t" + j['air_date'])
print("Episode:\t" + j['episode'])

print()
x = random.choice(j['characters'])

random_character = requests.get(x, timeout = 4)
jj = json.loads(random_character.text)

print("Name:\t\t" + jj['name'])
print("Status:\t\t" + jj['status'])
print("Species:\t" + jj['species'])
print("Origin:\t\t" + jj['origin']['name'])
