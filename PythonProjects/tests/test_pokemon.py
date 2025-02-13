import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f03a5127a2ffe88ff9e23a0698fe11d9'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
trainers_id = 18724


def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainers_id' : trainers_id}) 
    assert response.status_code == 200

def test_name_trainers():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : '18724'})
    assert response_get.json()["data"][0]["trainer_name"] == 'Gaide'
