from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters

import logging

TOKEN = "unknown"

updater = Updater(TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='This bot repeats messages sent by the user.')


def text(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{update["message"]["text"]}')


start_handler = CommandHandler('start', start)
text_handler = MessageHandler(Filters.text, text)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_handler)

updater.start_polling()
