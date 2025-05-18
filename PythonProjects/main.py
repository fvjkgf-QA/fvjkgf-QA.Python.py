import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0b60c866091bdafcc3664ad9ece6a9d7'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '38093'
URLlavka = 'https://lavka.pokemonbattle.ru/'

body_registration = {
    "trainer_token": TOKEN,
    "email": "isagadeev220196@gmail.com",
    "password": "89033501356Jacksonww1l"
}
body_confirmation = {
    "trainer_token": TOKEN
}

body_create ={
    "name": "Бульбазавр",
    "photo_id": 1
}

body_pokid = {
    "pokemon_id": "317309"
}

body_fight = {
    "attacking_pokemon": "317309",
    "defending_pokemon": "317753"
}

body_rename = {
    "pokemon_id": "317312",
    "name": "Бибазавр",
    "photo_id": 3
}
body_paschange ={
    "password_old": "Q1234",
    "password_new": "123453456Il"
}

body_lavka ={
    "order_type": "avatar",
    "details": {
        "avatar_id": "1",
        "card_number": "4111111111111111",
        "card_name": "german dolnikov",
        "card_actual": "10/25",
        "card_cvv": "125",
        "secure_code": "56456"
    }
}

#Регистрация
'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

#Подтверждение почты
'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

#Смена пароля
'''response_passchange = requests.put(url = f'{URL}/trainers/edit_password', headers = HEADER, json = body_paschange)
print(response_passchange.text)
print(response_passchange.status_code)'''

#Создание покемона
'''response_create = requests.post(url=f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
print(response_create.status_code)
message = response_create.json()['message']
print (message)'''

#Поймать покемона
'''response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokid)
print(response_add.text)
print(response_add.status_code)'''

#Переименовать покемона
'''response_rename = requests.put(url=f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)
print(response_rename.status_code)'''

#Список покемонов
'''response_pokemonlist = requests.get(url=f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
print(response_pokemonlist.text)
print(response_pokemonlist.status_code)'''

#Список тренеров
'''response_trainerlist = requests.get(url=f'{URL}/trainers', params = {'level' : 3})
print(response_trainerlist.text)
print(response_trainerlist.status_code)'''

#Битва
'''response_fight = requests.post(url=f'{URL}/battle', headers = HEADER, json = body_fight)
print(response_fight.text)
print(response_fight.status_code)'''

#Покупка аватара
'''response_lavka = requests.post(url=f'{URLlavka}/payments', headers = HEADER, json = body_lavka)
print(response_lavka.text)
print(response_lavka.status_code)'''
