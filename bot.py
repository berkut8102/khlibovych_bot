import telebot

# Токен від BotFather
TOKEN = '7741715644:AAHfQIgiHxsRBcVQbG4hwR1ef57CDu_NeZs'
bot = telebot.TeleBot(TOKEN)

print("Бот запущений")


# Обробник команди /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Це твій бот для запису на Міні-курс 26 ГОДИН. Щоб сплатити 980 грн. за Інтенсив, скористайся цим посиланням: https://pay.mbnk.biz/2410197arKv5mUV3eXyq  Посилання дійсне до 22 жовтня")



# Запуск бота
bot.polling()
