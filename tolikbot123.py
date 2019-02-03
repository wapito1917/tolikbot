import os
import random
import telebot
from telebot.types import Message
TOKEN='706950167:AAEMzTSjTEmkCEW44dLmVW_pH9UeFhTHmgs'
bot = telebot.TeleBot(TOKEN)

answer=[
        'Готов я о любви к тебе, я вечно говорить',
        'Твои глаза, как звезды и луна, прекрасны и манят меня',
        
        'Если с утра залпом выпить литровую кружку лимонного сока, то можно до вечера проходить с кислой физиономией.',
	]


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, 'Привет, я скучаю по тебе Дина, давай поболтаем о любви!')

@bot.message_handler(func=lambda message: True)
def talk(message:Message):
    if message.from_user.id==559107101:
        bot.reply_to(message,random.choice(answer))
    else:
        bot.reply_to(message,message.chat.id)


bot.polling()
