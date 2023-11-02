import telebot
from telebot import types
bot = telebot.TeleBot("6776366650:AAGpqPbqvjveIosv8XahXBWyJgYQHLPcBjs")
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,f"<b>Привет {message.from_user.first_name}</b>",parse_mode="html")
@bot.message_handler()
def get_user_text(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Да",callback_data="yes")
    btn2 = types.InlineKeyboardButton("Нет",callback_data="no")
    markup.add(btn1,btn2)
    bot.send_message(message.chat.id,"Хочешь покажу что то интересное?",reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    if call.message:
        if call.data=="yes":
            new_markup = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton("Отправить стикер?",callback_data="sticker")
            btn2 = types.InlineKeyboardButton("Отправить фотографию?",callback_data="photo")
            new_markup.add(btn1,btn2)
            bot.send_message(call.message.chat.id,"Выберите одну из двух возможностей",reply_markup=new_markup)
        elif call.data=="no":
            bot.send_message(call.message.chat.id,"Вы хозяин своего решения")
        elif call.data=="sticker":
            bot.send_sticker(call.message.chat.id,"CAACAgIAAxkBAAJUL2VDsG4XaoUfo-SM8DWtsRx1WawPAAIVAAPANk8TzVamO2GeZOczBA")
        elif call.data=="photo":
            photo = open("lukash_batman_2.png")
            bot.send_photo(call.message.chat.id,photo)
bot.polling(none_stop=True)
