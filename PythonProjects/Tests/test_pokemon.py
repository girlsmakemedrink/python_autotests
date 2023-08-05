import requests
import pytest

token = '3850cbcceda91870a8314d15a2f7639f'
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers', params= {'trainder_id' : '1932'})
    assert response.status_code == 200

def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : '1932'})
    assert response.json()['trainer_name'] == 'python'
