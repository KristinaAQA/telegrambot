import telebot

TOKEN = '7790671470:AAEHt0JSVLvfFSqWtfFz3iadF_Bvx5iL7hE'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Чем могу помочь?")



bot.infinity_polling()
