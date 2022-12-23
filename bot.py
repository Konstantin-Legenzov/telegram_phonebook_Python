import telebot
from userInterface import get_info
from file_manager import creating, changer

bot = telebot.TeleBot('5788937924:AAHZ6XyO5Oc9r4l20X8KM6PfjvwSOnTCITQ')

contact = get_info()
create = creating()
change = changer()

old_value = ''

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(   telebot.types.InlineKeyboardButton('add', callback_data= 'add'),
                telebot.types.InlineKeyboardButton('change', callback_data= 'change') )
                 
                

@bot.message_handler(commands=['add','change'])

# #def get_message(message):
#     global value
#     if value == '':
#         bot.send_message(message.from_user.id, '0', reply_markup=keyboard) 
#     else: 
#         bot.send_message(message.from_user.id, value, reply_markup=keyboard) 


@bot.callback_query_handler(func=lambda call: True)
def call_back(query):
    global value, old_value
    data = query.data #теперь дата, то что возвращает кнопка 

    if data =='add':
        create()
        contact()
    elif data == 'change':
        change()
   
bot.polling(none_stop=False, interval= 0) #Запускаем БОТА
