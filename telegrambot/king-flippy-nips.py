import logging
import json
import datetime

from telegram import Update, user
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler

from CRED import TOKEN

# File handler
def add_data():
    """Will be replace by add_trip as soon as I find my whish to live"""
    f = open("numero.txt", mode='r')
    s = f.readline()
    f.close()
    print(s)
    f = open("numero.txt", mode='w')
    f.write(str(int(s) + 0))
    f.close()


def add_trip(comment=None):
    """Add 1 to totals trips to Pluto """
    """Right know total trips numbers are stored on a shitty txt file, in the future the will be store with json"""
    date = datetime.datetime.now().strftime("%Y/%B/%A")
    time = datetime.datetime.now().strftime("%H:%M")
    trip_data = {"date": date,
                 "time": time,
                 "note": comment
                 }

    with open("../data/data.json", "a") as data_file:
        data_file.write(json.dumps(trip_data, indent=4))

    add_data()  # Call function to perform +1


def remove_trip():
    """Remove 1 to total trips to Pluto"""
    ...


def total_trips():
    """Get total trips numbers"""
    f = open("numero.txt", mode='r')
    n = f.readline()
    f.close()
    return n


# Telegram commands
def start(update: Update, context: CallbackContext):
    """Reply when user starts bot"""
    context.bot.send_message(chat_id=update.effective_chat.id, text="Chi rizza appizza e ammazza!")


def helper(update: Update, context: CallbackContext):
    """Print help for stoned user"""
    context.bot.send_message(chat_id=update.effective_chat.id, text="It's so simple you don't need help")


def bot_add_trip(update: Update, context: CallbackContext):
    """Add one trip"""
    user_comment = context.args
    add_trip(user_comment)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Verso l'infinito e oltre!")


def bot_remove_trip(update: Update, context: CallbackContext):
    """Remove one trip"""
    # remove_trip()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Non rimosso")  # What should I write here?


def bot_total_trip(update: Update, context: CallbackContext):
    """Send to user total trips number"""
    n = total_trips()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hai effettuato {n} viaggi!")


# Word games (or whatever they are called)
def cipciop(update, context):
    """Replay with 'ciop' when stoned user writes 'cip'."""
    user.say = "cip".join(context.args)
    update.message.replay_test("ciop")


# Main
def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", helper))
    dispatcher.add_handler(CommandHandler("aggiungi", bot_add_trip))
    dispatcher.add_handler(CommandHandler("rimuovi", bot_remove_trip))
    dispatcher.add_handler(CommandHandler("totale", bot_total_trip))

    updater.start_polling()


if __name__ == '__main__':
    main()
