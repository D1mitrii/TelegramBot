from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import ParseMode, Update, MessageEntity
from config import TOKEN

import logging


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='This bot uses filters.')


def send_photo_or_video(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Cool video or photo!')

def send_photo_or_video_bold(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='<b>Cool video or photo!</b>', parse_mode=ParseMode.HTML)


def send_audio(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Cool sound!')

    
def send_link(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Wow weird link!')

def get_number(update, context):
    key, value = context.args
    context.user_data[key] = value
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Key: {key} contains: {value}')


def put_sum(update, context):
    key1, key2 = context.args

    try:
        value1 = context.user_data[key1]
        value2 = context.user_data[key2]
    except KeyError:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Invalid key')
        return

    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Sum = {int(value1) + int(value2)}')
    


def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    number_handler = CommandHandler('number', get_number)
    sum_handler = CommandHandler('sum', put_sum)

    no_forwarded_photo_video_handler = MessageHandler(~Filters.forwarded & (Filters.photo | Filters.video), send_photo_or_video)
    forwarded_photo_video_handler = MessageHandler(Filters.forwarded & (Filters.photo | Filters.video), send_photo_or_video_bold)
    audio_handler = MessageHandler(Filters.audio, send_audio)
    link_handler = MessageHandler(Filters.text & (Filters.entity(MessageEntity.URL) | Filters.entity(MessageEntity.TEXT_LINK)), send_link)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(number_handler)
    dispatcher.add_handler(sum_handler)

    dispatcher.add_handler(no_forwarded_photo_video_handler)
    dispatcher.add_handler(forwarded_photo_video_handler)
    dispatcher.add_handler(audio_handler)
    dispatcher.add_handler(link_handler)

    updater.start_polling()

if __name__ == "__main__":
    main()
