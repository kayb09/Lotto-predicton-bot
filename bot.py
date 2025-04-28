import telebot

# Your Telegram bot token
TOKEN = '7633193305:AAHRi_tKHKe335_fw_1bGyD71mmV4aLSYs4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! I will predict Lotto and Powerball numbers soon!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Prediction feature coming soon. Stay tuned!")

bot.infinity_polling()