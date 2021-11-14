import logging

from telegram import Update, user
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler

from CRED import TOKEN


def start(update: Update, context: CallbackContext):
    """Reply when user starts bot"""
    context.bot.send_message(chat_id=update.effective_chat.id, text="Chi rizza appizza e ammazza")


def test(update: Update, context: CallbackContext):
    """Random function to test bot"""
    context.bot.send_message(chat_id=update.effective_chat.id, text="Questo e' un test tossico bastardo")


def fa_na_canna(update: Update, context: CallbackContext):
    """Add +1 to joint counter"""
    context.bot.send_message(chat_id=update.effective_chat.id, text="Fumo, fumo, fumo e rido")


def ma_quanto_fumo():
    """Send to user total smoked joints"""
    ...


def cipciop(update, context):
    """Replay with 'ciop' when stoned user writes 'cip'."""
    user.say = "cip".join(context.args)
    update.message.replay_test("ciop")


def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s', level=logging.INFO)

    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    test_handler = CommandHandler('test', test)
    cannetta_handler = CommandHandler('cannetta', fa_na_canna)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(test_handler)
    dispatcher.add_handler(cannetta_handler)

    dispatcher.add_handler(CommandHandler("cipciop", cipciop))

    updater.start_polling()


if __name__ == '__main__':
    main()
