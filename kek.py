# import line

# fIrSt uSe

# pip install vk
# pip install telebot
import vk
import telebot

# config line
vsession = vk.AuthSession('id_app', 'login', 'pass')
bot = telebot.TeleBot('token')
vapi = vk.API(session)

# example config line

#vsession = vk.AuthSession('1234567', 'durov@vk.com', 'gitHUB123')
#vapi = vk.API(session)
#bot = telebot.TeleBot('242589731:AAGDz-F8q5TN0IfD3Y_D4WB0BmerHm1UYiw')
