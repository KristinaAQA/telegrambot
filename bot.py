import telebot

TOKEN = 'Вставьте_свой_токен'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Чем могу помочь?")



bot.infinity_polling()
