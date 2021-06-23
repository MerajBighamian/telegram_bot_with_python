

#------------import classes of package telegram.ext----------------#
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
#--------------------------------------end-----------------------------------------------#

#------------import classes of module telegram----------------#
from telegram import InlineQueryResultArticle, InputTextMessageContent,InlineKeyboardButton, Video
#--------------------------------------end-----------------------------------------------#

#-------import mpdule logging-------#
import logging
#----------end-------------#

#---------import module db for work with data base-----------#
import db
#-----------------------end-------------------------#
#------------- define a instance of class Updater for fetch data from telegram chat-----------#
updater  = Updater(token='1199397772:AAEWp1trAiU_tyHy5-QkqFVgf-Bwu_cXSJo', use_context=True)
#------------------end-------------------------#

#----------- define dispatcher of updater -----------#
dispatcher = updater.dispatcher
#-----------------------end-------------------------#
#------------------------------logging for exception handler---------------------#
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
#-------------------------------end----------------------------------------

#----response for start command ----#
def start(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="سلام این ربات معراج بیغمیان است")
    context.bot.send_message(chat_id=update.effective_chat.id, text= "لطفا نام خود را وارد کنید")
#--------------------end----------------------#


#----------------------- get name of user and insert to db --------------------------#
def name(update,context):
    name_user = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text= "ممنون از شما کاربر %s" % name_user)
    chat_id=update.effective_chat.id
    db.open_cursor()
    db1 = db.db(name_user,chat_id)
    db1.insert_in_db()
#--------------------end----------------------#

#----- close connection of db ---------------#
db.curso_close()
#--------------------end----------------------#

# def caps(update,context):
#     text_caps = ''.join(context.args).upper()
#    context.bot.send_message(chat_id=update.effective_chat.id, text = text_caps)


def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='captalize',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

# def say_hello(update,context):
#     query = update.inline_query.query
#     if not query:
#         return 
#     results 


#----handle command is not defined for bot----#
def unknown(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = "!دستور وارد شده صحیح نیست")
#----------------end------------------#


video_me  = Video("./17-css-in-js.mp4","./17-css-in-js.mp4",1000,500,60)



button_url = InlineKeyboardButton(text="دیدن وبسایت من", url='https://roocket.ir/')
dispatcher.add_handler(button_url)

#--------------------------------------------------------------------------#

# --------------------------------handlers---------------------------------#
 

#--define handler of command start--#
start_handler = CommandHandler('start', start)
#----------end----------------------#

#--add handler of command start to dispatcher--#
dispatcher.add_handler(start_handler)
#---------------------end----------------------#

#-----------define handler of input name--------#
name_handler = MessageHandler(Filters.text & (~ Filters.command), name)
dispatcher.add_handler(name_handler)
#---------------------end----------------------#

# caps_handler = CommandHandler('caps',caps)
# dispatcher.add_handler(caps_handler)


#--define handler of command is not define--#
unknown_handler = MessageHandler(Filters.command, unknown)
#----------end----------------------#

#--add handler of command is not define to dispatcher--#
dispatcher.add_handler(unknown_handler,1)
#---------------------end----------------------#


inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)


#---start polling data from telegram chat with updater--#
updater.start_polling()
#---------------------end----------------------#
