import telebot
import PIL
from telebot import types
#import everything you need to overcome problems 

bot = telebot.TeleBot('%BOT TOKEN%'')

def start(message):
    if message.text == '/go':
        bot.send_message(message.from_user.id, 'Who are you?');
        bot.register_next_step_handler(message, get_name); #Used get_name function
    elif message.text == '/start':
          bot.send_message(message.from_user.id, 'Wanna talk? What is you name?');
          bot.register_next_step_handler(message, get_name); #Used get_name function
    else:
        bot.send_message(message.from_user.id, "Let's start from the beginning. Use commands: /start or /go. Bot will send you its' author personal email after some random steps.");
      
def get_name(message): #Getting the name from the bot's interlocutor to form a little database
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, '%Necessary add interactions%');
    bot.register_next_step_handler(message, get_all_information_you_need_dont_be_like_crazy);

@bot.message_handler(commands=['%commands set via BotFather%'])
def get_text_messages(message): (message.chat.id, '%Start%')

@bot.message_handler(content_types=['text', 'picture', 'audio']) #But they can send selfies and there that way!

    if message.text == '/help':
       bot.send_message(message.from_user.id, '%Just write your own cookbook if you need to be totally clear%')
    else:
       bot.send_message(message.from_user.id, "%A helpful phrase full of empathy%")

    if message.text == "Хуй":
       bot.send_message(message.from_user.id, " ") #So, what would you do? Social is very complicated sometimes, don't overestimate either yourself, or them.
    elif message.text == '/finish':
       bot.send_message(message.from_user.id, 'Ciao.')
    else:
       bot.send_message(message.from_user.id, 'Бот тебя не понимает. Поразмысли об обозначаемом и обозначающем, будь проще в следующий раз. Do you need a /help? Пробуем?');
       
bot.polling(none_stop=True, interval=0) #After a program is written it can work all day and all night long
