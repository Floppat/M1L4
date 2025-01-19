from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.health = randint(50,200)
        self.attack = round(50 - (self.health/5),0)


        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return "ошибка получения изображения"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f'''Имя твоего покемона: {self.name}\n
Здоровье твоего покемона: {self.health}
Сила твоего покемона: {self.attack}'''

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

    def battle(self):
        enemy_health = randint(50,150)
        en_h = enemy_health
        enemy_attack = round(35 - (enemy_health/5),0)
        en_a = enemy_attack
        while self.health > 0:
            self.health -=enemy_attack
            enemy_health -= self.attack
            if enemy_health <= 0 and self.health > 0:
                return (f'вы победили, ваш враг был: Здоровье:{en_h} Сила:{en_a}, у вас осталось {self.health} здоровья')
        return (f'''вы проиграли, ваш враг был: Здоровье:{en_h} Сила:{en_a}. 
то ли игра жестока то ли разраб ленив но воскресить его нельзя, игра окончена.''')
