import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f03a5127a2ffe88ff9e23a0698fe11d9'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_pokemons = {
    "name": "Gaide",
    "photo_id": 22
}
name_pokemons = {
    "pokemon_id": "233160",
    "name": "garbodor",
    "photo_id": 22
}
in_pokeball = {
    "pokemon_id": "233160"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(response_create.text)'''

'''response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = name_pokemons)
print(response_create.text)'''

'''response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = in_pokeball)
print(response_create.text)'''

response_get = requests.get(url = f'{URL}/me', headers = HEADER)
print(response_get.text)


