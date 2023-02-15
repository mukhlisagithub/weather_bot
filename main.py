import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


updater = Updater(token='5961378352:AAH0ij93CPAbXPVFG4L2E_8ksSQLLzNOzsE', use_context=True)



def start(update:Update, context:CallbackContext):
    update.message.reply_text("Ob-havo botiga xush kelibsiz!!\n"
                              "So'rovingizni  /search dan keyin kiriting!!!")

def search (update:Update, context:CallbackContext):
    # query = update.message.text
    word = context.args
    manzil = ' '.join(word)
    url = f"https://open-weather13.p.rapidapi.com/city/{manzil}"

    headers = {
        "X-RapidAPI-Key": "fcbc9f002emsh198a497f3a391d6p177e38jsn86e86532949a",
        "X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    data = response.json()
    joylashuv = data['name']
    n_t = (data['main']['temp'] - 32) * (5 / 9) // 1
    min_t = data['main']["temp_min"]
    max_t = data['main']["temp_max"]
    havo = data['weather'][0]['main']
    shamol = data['wind']['speed'] // 1
    if havo == "Rain":
        havo = "Yomg'ir"
    elif havo == "Mist":
        havo = "Tuman"
    elif havo == "Sunny":
        havo = "Quyoshli"
    elif havo == "Clouds":
        havo = "Bulutli"
    elif havo == "Snow":
        havo = "Qor"



    # print(response.text)
    # print(f"Bugun {joylashuv}da {n_t} °C, shamol tezligi {shamol} m/s, havo {havo}")

    update.message.reply_text(f"Bugun {joylashuv} da {n_t} °C, shamol tezligi {shamol} m/s,  {havo}")





dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('search', search))
# dispatcher.add_handler(MessageHandler(filters & ~filters.COMMAND, api))
updater.start_polling()
updater.idle()