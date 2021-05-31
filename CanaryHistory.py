#import ctypes
#import subprocess
#import time
#updater = Updater(token=token)
#dp = updater.dispatcher
from time import localtime, strftime

#from telegram.ext import (CommandHandler, ConversationHandler, Filters,
#                          MessageHandler, Updater)
import telegram

token='TELEGRAM_BOT_ID_HERE'
chat_id = 'CHAT_ID_HERE'

def CheckConnection(times,interval):
    for x in range(times):
        a=subprocess.run("ping www.google.com -n 1")
        b=a.returncode
        print(b)
        if not b:
            return True
        time.sleep(interval)
    return False


def startup():
    a=strftime(f"%Y-%m-%d %H:%M:%S", localtime())
    telegram.Bot(token).send_message(chat_id=chat_id, text=f"Canary - Laptop\nStarted on {a}\nNot you? /lock")

def lock(bot, update):
    print('chere')
    time.sleep(1)
    ctypes.windll.user32.LockWorkStation()


#if CheckConnection(30,5):
if True:
    #dp.add_handler(CommandHandler("lock", lock))

    #! Not adding lock in, could be maliciously locked by others by spamming my bot with /lock or by my own mistake with /lock. 
    # ! - security of bot not confirmed as of 08/07/2019
    #dp.add_handler(CommandHandler("startup", startup))

    #updater.start_polling()
    
    startup()
    #time.sleep(60)
    #print("Stopping bot")
    #updater.stop()
