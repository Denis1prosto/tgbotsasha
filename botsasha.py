import telebot
from telebot import types
from random import choice
RANDOM_POSLO =["Ты охуенно соблазнительная", "На твой охренительный попец текут слюнки", "Твоя охуительно соблазнительная фигура подталкивакет на грех мастурбации"]
RANDOM_RADOST = ["Ты красотка💗","Напиши мне скину денежку💗" , "Я тебя люблю💗" , "Лакки красавчик💖", "Все челядь а ты приецесса💖"]
RANDOM_POD = ["У тебя все получится💗","Ты молодец не сдавайся💋","Трудности пройдут а охуенна ты всегда💗","Напиши мне скину денежку💗"]
RANDOM_chmok= ["💋💋💋💋","💋","💋В попочку💋💋","💋В носик💋💋","Чмок в пупок💋💋"]
RANDOM_milota = ["Мав💗", "Ты котик я котик💗","Я вмурчался в тебя💗"]
RANDOM_PNI=["JUST DO IT!!! Ленивая попка💗","До шубы осталось 10 приседаний😂","Вставай!! Впереди плодотворный день!!"]
LOVE = ["Привет! Я сообщение, которому поручено передать тебе неограниченное количество самых нежных и сладких поцелуев!💋💋💋💋",
"Есть кое-что, что так приятно делать мне — закрыть глаза и думать о тебе.💗", "Люблю, сильнее чем это было вчера, но недостаточно сильно, как это будет завтра💗",
"Прочти это и улыбнись, ведь ты обладательница самой чудесной улыбки😍 Люблю тебя!❤️❤️❤️"]
Utro = ["Доброе утро, Любимая💗","Доброе утро и хорошего дня️❤️❤️","Какая красотка проснулась!😍 😍 😍 Привет!💗"]

bot = telebot.TeleBot('5791166428:AAHhzJqKXCmOkFNDH45aPGuTZsRoFR0HNFs')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Порадовать")
    btn2 = types.KeyboardButton("Поддержать")
    btn3 = types.KeyboardButton("Пошлый комплимент")
    btn4 = types.KeyboardButton("Поцелуй")
    btn5 = types.KeyboardButton("Пни меня")
    btn6 = types.KeyboardButton("Милота")
    btn7 = types.KeyboardButton("Нежное признание в любви")
    btn8 = types.KeyboardButton("Доброе утро")
    markup.add(btn1, btn2,btn3,btn4,btn5,btn6,btn7,btn8)
    mess = "Привет любимая💗, чем я могу помочь?"
    bot.send_message(message.chat.id, mess, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def funk(message):
    if(message.text == "Порадовать"):
        text = choice(RANDOM_RADOST)
        bot.send_message(message.chat.id, text)
    elif(message.text == "Поддержать"):
        text = choice(RANDOM_POD)
        bot.send_message(message.chat.id, text)

    elif(message.text == "Пошлый комплимент"):
        text = choice(RANDOM_POSLO)
        bot.send_message(message.chat.id, text)

    elif(message.text == "Поцелуй"):
        text = choice(RANDOM_chmok)
        bot.send_message(message.chat.id, text)

    elif(message.text == "Пни меня"):
        text = choice(RANDOM_PNI)
        bot.send_message(message.chat.id, text)

    elif(message.text == "Милота"):
        text = choice(RANDOM_milota)
        bot.send_message(message.chat.id, text)

    elif(message.text == "Нежное признание в любви"):
        text = choice(LOVE)
        bot.send_message(message.chat.id, text)

    elif(message.text == "Доброе утро"):
        text = choice(Utro)
        bot.send_message(message.chat.id, text)

    else:
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         btn1 = types.KeyboardButton("Порадовать")
         btn2 = types.KeyboardButton("Поддержать")
         btn3 = types.KeyboardButton("Пошлый комплимент")
         btn4 = types.KeyboardButton("Поцелуй")
         btn5 = types.KeyboardButton("Пни меня")
         btn6 = types.KeyboardButton("Милота")
         btn7 = types.KeyboardButton("Нежное признание в любви")
         btn8 = types.KeyboardButton("Доброе утро")
         markup.add(btn1, btn2,btn3,btn4,btn5,btn6,btn7,btn8)
         bot.send_message(message.chat.id, "Прости такого не умею, тыкни в кнопку красавица😍", reply_markup=markup)

bot.polling(none_stop=True)
