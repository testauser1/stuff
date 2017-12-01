# -*- coding: utf-8 -*-
import time
import config
import telebot
import vk_api
import vk

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "веселькрафт няшка") # Отправка сообщения

	
@bot.message_handler(commands=['post'])
def send_welcome(message):
	vk_api = vk.API(session)
	vk_api.wall.post(message="hello")
	

if __name__ == '__main__':
     bot.polling(none_stop=True)
	