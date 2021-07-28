import telebot
import time

from telebot import types

token = 'Your token here'
bot = telebot.TeleBot(token)

 # keyboard
 markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
 item1 = types.KeyboardButton("Расписание понедельник")
 item2 = types.KeyboardButton("Расписание вторник")
 item3 = types.KeyboardButton("Расписание среда ")
 item4 = types.KeyboardButton('Расписание четверг')
 item5 = types.KeyboardButton('Расписание пятница')

    markup.add(item1, item2, item3, item4, item5)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот,созданный,чтобы присылать расписание.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(func=lambda n: True)
def response(message):
        if message.text == 'Расписание понедельник':
            bot.reply_to(message,
                             '1.Химия\n''2.Алгебра\n''3.Физ-ра\n''4.ОБЖ/Информатика\n''5.Русский язык\n' '6.Английский язык\n''7.Литературный практикум\n')
        if message.text == 'Расписание вторник':
            bot.reply_to(message,
                             '1.Геометрия\n' '2.Физика\n''3.Алгебра\n''4.Русский язык\n''5.Литература\n''6.Английский язык\n')
        if message.text == 'Расписание среда':
            bot.reply_to(message,
                             '1.Химия\n''2.Алгебра\n''3.География\n''4.История\n' '5.Немецкий/Французский язык\n' '6.Алгебра\n' '7.Английский язык\n')
        if message.text == 'Расписание четверг':
            bot.reply_to(message,
                             "1.Обществознание\n"'2.Геометрия\n' '3.Биология\n''4.Русский язык\n''5.Английский язык\n''6.Физика\n' '7.Литература\n')
        if message.text == 'Расписание пятница':
            bot.reply_to(message,
                             '2.Физ-ра\n''3.Биология\n''4.История\n''5.География\n' '6.Немецкий/Французский язык\n' '7.МХК\n')


bot.polling(none_stop=True, interval=0)
