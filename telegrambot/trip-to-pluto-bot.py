import logging
import json
import datetime

from telegram import Update, user
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler

from CRED import TOKEN

#logica controllo id + creazione decorator
#passo prima di ogni funzione il decorator


def add_new_element(comment=None):
    """ +1, """
    date = datetime.datetime.now().strftime("%Y/%B/%A")
    time = datetime.datetime.now().strftime("%H:%M")
    data = { "date": date,
          "time": time,
          "note": comment
    }

    with open("data.json", "a") as data_file:
        data_file.write(json.dumps(data, indent=4))


def add_to_file():
    """Add +1 joint smoked broh"""
    f = open("numero.txt", mode='r')
    s = f.readline()
    f.close()
    print(s)
    f = open("numero.txt", mode='w')
    f.write(str(int(s) + 1))
    f.close()


def retrive_smoked_joints():
    """Give me my jointsss"""
    f = open("numero.txt", mode='r')
    drummini = f.readline()
    f.close()
    return drummini


def start(update: Update, context: CallbackContext):
    """Reply when user starts bot"""
    context.bot.send_message(chat_id=update.effective_chat.id, text="Chi rizza appizza e ammazza!")


def help(update: Update, context: CallbackContext):
    """Print help for stoned user"""
    """Yeh shitty help I know"""
    context.bot.send_message(chat_id=update.effective_chat.id, text="Fumo, fumo, fumo e rido!")


def fa_na_canna(update: Update, context: CallbackContext):
    """Add +1 to joint counter"""
    user_comment = context.args
    add_new_element(user_comment)
    add_to_file()
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ne ho appena fumata una!")


def ma_quanto_fumo(update: Update, context: CallbackContext):
    """Send to user total smoked joints"""
    n = retrive_smoked_joints()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hai fumato {n} cannoni fratm!")


# Word games (or whatever they are called)
def cipciop(update, context):
    """Replay with 'ciop' when stoned user writes 'cip'."""
    user.say = "cip".join(context.args)
    update.message.replay_test("ciop")


# Main
def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s', level=logging.INFO)

    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    cannetta_handler = CommandHandler('cannetta', fa_na_canna)
    numero_handler = CommandHandler('numero', ma_quanto_fumo)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(cannetta_handler)
    dispatcher.add_handler(numero_handler)

    dispatcher.add_handler(CommandHandler("cipciop", cipciop))

    updater.start_polling()


if __name__ == '__main__':
    main()
