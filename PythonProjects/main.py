import requests
token = '3850cbcceda91870a8314d15a2f7639f'
host = 'https://api.pokemonbattle.me:9104'

'''response = requests.post('https://api.pokemonbattle.me:9104/trainers/reg', json = {
    "trainer_token": token,
    "email": "python@mail.ru",
    "password": "Python1"
}, 
 headers= {'Content-Type' : 'application/json'})
print (response.text)''' 

'''response_confirm_email = requests.post(f'{host}/trainers/confirm_email', json = {
    "trainer_token": token
}, headers= {'Content-Type' : 'application/json'})
print (response_confirm_email.text)'''

'''response_create_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "generate",
    "photo": "generate"
}, headers= {'Content-Type' : 'application/json',
             'trainer_token' : token})
print (response_create_pokemon.text)'''

'''response_change_pokemon = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "5911",
    "name": "stone python",
    "photo": "https://dolnikov.ru/pokemons/albums/095.png"},
      headers= {'Content-Type' : 'application/json',
             'trainer_token' : token})
print (response_change_pokemon.text)'''

'''response_pokeball_pokemon = requests.post(f'{host}/trainers/add_pokeball', json ={
    "pokemon_id": "5911"},
      headers= {'Content-Type' : 'application/json',
             'trainer_token' : token})
print (response_pokeball_pokemon.text)''' 