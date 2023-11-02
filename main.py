import telebot
from telebot import types
bot = telebot.TeleBot("6776366650:AAGpqPbqvjveIosv8XahXBWyJgYQHLPcBjs")
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    markup.add(btn1,btn2)
    bot.send_message(message.chat.id,"Хочешь посмотреть что-то интересное?",reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    if call.message:
        if call.data=="sticker":
            bot.send_sticker(call.message.chat.id,"CAACAgIAAxkBAAJUMWVDsUUQGP9AvKtdDaW1woCq5W2RAAK0DgACeuewSEicxAjipUlPMwQ")
        elif call.data=="photo":
            photo = open("lukash_2.jpg")
            bot.send_photo(call.message.chat.id,photo)

@bot.message_handler()
def answer_yes(message):
    if message.text=="Да":
        new_markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("Отправить стикер?", callback_data="sticker")
        btn2 = types.InlineKeyboardButton("Отправить фотографию?", callback_data="photo")
        new_markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Выберите одну из двух возможностей", reply_markup=new_markup)
    elif message.text=="Нет":
        bot.send_message(message.chat.id,"Это ваш выбор")
        bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAJUSmVD63vRnqfEfRsywStiymn0C8zNAAIaAAPANk8TgtuwtTwGQVczBA")

bot.polling(none_stop=True)
