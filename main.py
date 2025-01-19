import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 
db = {

}
@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        db["message.from_user.username"] = pokemon
        bot.reply_to(message, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['stats'])
def stats(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        bot.reply_to(message, "Сначала создай себе покемона")
    else:
        bot.reply_to(message, db["message.from_user.username"].info())

@bot.message_handler(commands=['battle'])
def deathmatch(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        bot.reply_to(message, "Сначала создай себе покемона")
    else:
        bot.reply_to(message, db["message.from_user.username"].battle())
bot.infinity_polling(none_stop=True)

