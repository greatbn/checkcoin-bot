from telegram.ext import Updater,  CommandHandler
import requests
import os
import sys


TOKEN = os.getenv('TELEGRAM_TOKEN', '478374777:AAGpNrKIc-NSd5PUC1VMJZZ7OWyqZF4hdPY')

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

def check_coin(bot, update, args): 
    data = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=2000')
    data = data.json()
    response = ""
    for arg in args:
        try:
            for coin in data:
                if arg.upper() == coin['symbol']:
                    response += "Name: {}\nRate: {}\nBTC Rate: {}\nChange(1h): {}\nChange(24h): {}\n".format(
                        coin['name'],coin['price_usd'], coin['price_btc'],
                        coin['percent_change_1h'], coin['percent_change_24h'])
        except:
            continue
    
    chat_id=update.message.chat_id
    sys.stdout.write('Receive command from {} with args: {}\n'.format(chat_id, args))
    bot.send_message(chat_id=chat_id, text=response)

check_handler = CommandHandler('check', check_coin, pass_args=True)
dispatcher.add_handler(check_handler)

sys.stdout.write('Staring bot...\n')
updater.start_polling()
