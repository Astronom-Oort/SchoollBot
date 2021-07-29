import telebot
import json

from telebot import types


with open("configs/config.json") as f:
    i = json.load(f)

with open("configs/config.json") as k:
    week = json.load(k)["week"]
    
for day in week:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*week)


bot = telebot.TeleBot(i["token"])


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот,созданный,чтобы присылать расписание.".format(
                message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=markup)


@bot.message_handler()
def message(message):
    if message.text == 'Расписание понедельник':
            bot.reply_to(message,
                             '1.Химия\n''2.Алгебра\n''3.Физ-ра\n''4.ОБЖ/Информатика\n''5.Русский язык\n' '6.Английский язык\n''7.Литературный практикум\n')
    elif message.text == 'Расписание вторник':
            bot.reply_to(message,
                             '1.Геометрия\n' '2.Физика\n''3.Алгебра\n''4.Русский язык\n''5.Литература\n''6.Английский язык\n')
    elif message.text == 'Расписание среда':
            bot.reply_to(message,
                             '1.Химия\n''2.Алгебра\n''3.География\n''4.История\n' '5.Немецкий/Французский язык\n' '6.Алгебра\n' '7.Английский язык\n')
    elif message.text == 'Расписание четверг':
            bot.reply_to(message,
                             "1.Обществознание\n"'2.Геометрия\n' '3.Биология\n''4.Русский язык\n''5.Английский язык\n''6.Физика\n' '7.Литература\n')
    elif message.text == 'Расписание пятница':
            bot.reply_to(message,
                             '2.Физ-ра\n''3.Биология\n''4.История\n''5.География\n' '6.Немецкий/Французский язык\n' '7.МХК\n')


bot.polling(none_stop=True, interval=0)
