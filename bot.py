
import telebot

facebook_url = "https://www.facebook.com/ProgresstechUA/"
vk_url = "https://vk.com/progresstech_ukraine"
instagram_url = "https://www.instagram.com/progresstech.ua/?hl=ru"

TOKEN = "1474183111:AAESqYDrVO8lqxDvcG-yD0rFzMtWLNB7Hkw"
bot = telebot.TeleBot(TOKEN)
a= "1112"
b= "331"
c= "532"

answer = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
answer.row('Текущая статистика')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Доброго времени суток, если вы желаете посмотреть статистику подписчиков, нажмите кнопку \"Текущая статистика\" на клавиатуре!", reply_markup= answer)

@bot.message_handler(content_types = ['text'])
def statistic(message):
    if message.text.lower() == "текущая статистика":
        bot.send_message(message.chat.id, "Статистика подписчиков:\nFacebook: " + a + "\nВконтакте: " + b + "\nInstagram: " + c)

