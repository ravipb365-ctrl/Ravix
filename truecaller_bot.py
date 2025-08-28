import requests
from telegram.ext import Updater, CommandHandler
import os

# ✅ Railway me BOT_TOKEN environment variable se aayega
BOT_TOKEN = os.getenv("7394121126:AAFI4U4O-X13HwXfcfNLri2LTmQAdFm8WXQ")

def start(update, context):
    update.message.reply_text(
        "👋 Welcome to 📞 Truecaller Info Bot!\n\n"
        "🔹 This bot helps you to get basic information about any phone number.\n\n"
        "📌 Example:\n"
        "`/lookup +916351516535`"
        , parse_mode="Markdown"
    )

def lookup(update, context):
    if not context.args:
        update.message.reply_text("❌ Please provide a number!\n\nUsage: `/lookup +911234567890`", parse_mode="Markdown")
        return

    number = context.args[0]
    url = f"https://numb.hosters.club/?number={number}"

    try:
        r = requests.get(url, timeout=10)
        data = r.json()

        reply_msg = (
            "===================================\n"
            "📞 Truecaller Info Bot\n"
            "===================================\n"
            f"📱 Number   : {data.get('number')}\n"
            f"👤 Name     : {data.get('name')}\n"
            f"📡 Carrier  : {data.get('carrier')}\n"
            f"🌍 Country  : {data.get('country')}\n"
            "===================================\n"
            "✅ Lookup Completed!\n\n"
            "🛠 Script Prepared By Ravi"
        )
        update.message.reply_text(reply_msg)

    except Exception as e:
        update.message.reply_text(f"❌ Error: {e}")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("lookup", lookup))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
