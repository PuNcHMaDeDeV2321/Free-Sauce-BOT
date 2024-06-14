import telebot
from telebot import types

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'asis'])
def start(message):
    custom_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    custom_keyboard.add(types.KeyboardButton('Free-Sauce💋'), types.KeyboardButton('Sauce-Tools 💋'))
    bot.send_message(message.chat.id, '¡Hola! Soy el asistente de 𝕮𝖔𝖒𝖒𝖚𝖓𝖎𝖙𝖞 𝕾𝖆𝖚𝖈𝖊 💋. Elige una opción:', reply_markup=custom_keyboard)

@bot.message_handler(func=lambda message: message.text in ['Free-Sauce💋'])
def button_handler(message):
    query = message.text
    if query == 'Free-Sauce💋':
        bot.send_message(message.chat.id, 'Visita el canal Free-Sauce [Aquí](https://t.me/+Zuu_E7mHDYpmZTVh).', parse_mode='Markdown')

if __name__ == '__main__':
    bot.polling()
