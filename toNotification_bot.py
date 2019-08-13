from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Bot
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

token = "<token>"
#https://api.telegram.org/bot<token>/sendMessage?chat_id=381354140&text=TestReply


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def msg(bot, update):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, msg))
    updater.start_polling()
    updater.idle()
        
if __name__ == '__main__':
    main()
    

     