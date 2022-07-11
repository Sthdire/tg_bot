import telebot
import requests
from bs4 import BeautifulSoup as BS
from telebot import types
from test import Parser

p = Parser

s = requests.Session()

html_h = s.get("https://randstuff.ru/fact/")
html_b = BS(html_h.content, "html.parser")


# Создаем экземпляр бота
bot = telebot.TeleBot('you telegrmB token')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):

    # Добавляем две кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Факт")
    item2 = types.KeyboardButton("Мудрость")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id,
                     'Нажми: \nФакт для получения интересного факта\nМудрость — для получения мудрой цитаты ',
                     reply_markup=markup)

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Факт":
        bot.send_message(message.chat.id, p.parse('https://randstuff.ru/fact/'))
    elif message.text == "Мудрость":
        bot.send_message(message.chat.id, p.parse('https://randstuff.ru/saying/'))
    else:
        bot.send_message(message.chat.id, "Я не понял, что ты сказал. Пожалуйста нажми на одну из кнопок")





# Запускаем бота
bot.polling(none_stop=True, interval=0)
