import telebot
import random
import pandas as pd

# Your bot token
TOKEN = '7633193305:AAHRi_tKHKe335_fw_1bGyD71mmV4aLSYs4'
bot = telebot.TeleBot(TOKEN)

# Load the historical data
lotto_data = pd.read_csv('lotto_results.csv')
powerball_data = pd.read_csv('powerball_results.csv')

def predict_lotto():
    numbers = list(range(1, 53))
    hot_numbers = lotto_data.iloc[:, 1:7].values.flatten()
    hot = pd.Series(hot_numbers).value_counts().head(20).index.tolist()
    prediction = random.sample(hot, 4) + random.sample(numbers, 2)
    prediction = sorted(set(prediction))[:6]
    bonus = random.choice(numbers)
    return prediction, bonus

def predict_powerball():
    numbers = list(range(1, 51))
    pb_numbers = list(range(1, 21))
    hot_numbers = powerball_data.iloc[:, 1:6].values.flatten()
    hot = pd.Series(hot_numbers).value_counts().head(15).index.tolist()
    prediction = random.sample(hot, 3) + random.sample(numbers, 2)
    prediction = sorted(set(prediction))[:5]
    powerball = random.choice(pb_numbers)
    return prediction, powerball

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to your Lottery Predictor Bot! Send /predict_lotto or /predict_powerball")

@bot.message_handler(commands=['predict_lotto'])
def handle_lotto(message):
    prediction, bonus = predict_lotto()
    bot.reply_to(message, f"Lotto Prediction: {prediction}\nBonus Ball: {bonus}")

@bot.message_handler(commands=['predict_powerball'])
def handle_powerball(message):
    prediction, powerball = predict_powerball()
    bot.reply_to(message, f"PowerBall Prediction: {prediction}\nPowerBall: {powerball}")

print("Bot is running...")
bot.polling()
