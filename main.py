import telebot
import constants


bot = telebot.TeleBot(constants.token)
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('Получить прогноз', 'Информация')
    user_markup.row('Прайс лист','Профиль в Instagram')
    bot.send_message(message.from_user.id, 'Добро пожаловать...', reply_markup=user_markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Получить прогноз":
        bot.send_message(message.from_user.id, " Федерер - Циципас (П1) ")
    elif message.text == "Информация":
        bot.send_message(message.from_user.id, " Мы команда профессиональных беттеров запускаем "\
                                               " телеграм канал для всех желающих "\
                                               " улучшить своё финансовое положение ")
    elif message.text == "Прайс лист":
        bot.send_message(message.from_user.id, " Подписка на месяц - 2000 ₽ "    
                                               
                                               " Подписка на неделю - 700 ₽ "
                                               
                                               " Ставка дня - 200 ₽ "
                                               
                                               " Экспресс дня - 400 ₽ ")

    elif message.text == "Профиль в Instagram":

        bot.send_message(message.from_user.id, "https://www.instagram.com/tolko_100_procent/")


bot.polling(none_stop=True)




