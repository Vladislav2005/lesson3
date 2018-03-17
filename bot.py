import telebot
import config

bot = telebot.TeleBot(config.token)
spisok_stud = ["Лена","Катя","Еркебулан","Никита","Дастан","Влад","Стас","Рома"]
@bot.message_handler(content_types = ["text"])
def answer_stud_messages(message):
    if message.text == "Студенты":
        for i in range (0,8+1):
            bot.send_message(message.chat.id, spisok_stud[i])
    print(message)
if __name__=='__main__':
    bot.polling(none_stop=True)
    
