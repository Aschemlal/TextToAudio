from gtts import gTTS
import telegram.ext, telegram
from languages import languages, langues

API = "5203230093:AAEwbDKhNNu8xfNrtqatciP6WWZhWR4IO1M"

def start(update, context):
        userId = update.message.chat_id
        userName = update.message.chat.first_name
        userLast = update.message.chat.last_name
        update.message.reply_text(f"Hi {userName}.")
        message(update, context)


def help(update, context):
    message(update, context)
    update.message.reply_text(langues)
    update.message.reply_text("Enter /lang with the code to change audio's language, like \"/lang fr\" \nDefault: English")


language = "en"

def lang(update, context):
        message(update, context)
        msg = update.message.text

        global language

        if ((msg=="/lang zh-TW") | (msg=="/lang zh-CN")):
            language = msg[6:11]
        else:
            language = msg[6:8]

        update.message.reply_text(f"language chenged to: {languages[language]}")


def envoyer(update, context):

    message(update, context)

    try:
        texte = update.message.text
        audio = 'speech.mp3'
        sp = gTTS(text = texte, lang = language, slow=False)
        sp.save(audio)
        update.message.reply_text("Here is your speech: ")
        context.bot.sendAudio(chat_id = update.message.chat_id,
        audio = open("speech.mp3", 'rb'), filename ="speech.mp3")
        update.message.reply_text("Thanks for using our bot \U0001F606.")

    except Exception as ex:
        update.message.reply_text(ex)


def message(update, context):
    if (update.message.chat_id != 811477411):
        context.bot.send_message(chat_id = 811477411, text = update.message.text+" from "+update.message.chat.first_name)
    else:
        print(update.message.text)

updater = telegram.ext.Updater(API, use_context=True)

disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))

disp.add_handler(telegram.ext.CommandHandler("help", help))

disp.add_handler(telegram.ext.CommandHandler("lang", lang))

disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, envoyer))

updater.start_polling()

updater.idle()
