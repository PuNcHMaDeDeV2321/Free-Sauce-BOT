import telebot
from telebot import types

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'asis'])
def start(message):
    custom_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    custom_keyboard.add(types.KeyboardButton('Free-Sauce💋'), types.KeyboardButton('Sauce-Tools 💋'))
    custom_keyboard.add(types.KeyboardButton('Pagina Web'), types.KeyboardButton('Dueño'))
    custom_keyboard.add(types.KeyboardButton('Spam Sauce 💋'))
    bot.send_message(message.chat.id, '¡Hola! Soy el asistente de 𝕮𝖔𝖒𝖒𝖚𝖓𝖎𝖙𝖞 𝕾𝖆𝖚𝖈𝖊 💋. Elige una opción:', reply_markup=custom_keyboard)

@bot.message_handler(func=lambda message: message.text in ['Free-Sauce💋', 'Sauce-Tools 💋', 'Pagina Web', 'Dueño', 'Spam Sauce 💋'])
def button_handler(message):
    query = message.text
    if query == 'Free-Sauce💋':
        bot.send_message(message.chat.id, 'Visita el canal Free-Sauce [Aquí](https://t.me/+Zuu_E7mHDYpmZTVh).', parse_mode='Markdown')
    elif query == 'Sauce-Tools 💋':
        bot.send_message(message.chat.id, 'Visita el canal Sauce-Tools [Aquí](https://t.me/saucetools2321).', parse_mode='Markdown')
    elif query == 'Pagina Web':
        bot.send_message(message.chat.id, 'Nuestra Pagina Web Pulsando [Aquí](https://lc.cx/Qwyxc3).', parse_mode='Markdown')
    elif query == 'Dueño':
        bot.send_message(message.chat.id, 'Creador del canal [@PuNcHMaDeDeV2321](https://t.me/PuNcHMaDeDeV2321).', parse_mode='Markdown')
    elif query == 'Spam Sauce 💋':
        bot.send_message(message.chat.id, 'Visita el canal Spam-sauce [Aquí](https://t.me/SpamSaucee).', parse_mode='Markdown')

if __name__ == '__main__':
    bot.polling()
