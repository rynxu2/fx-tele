from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import daemon

def main():
    async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f'Hello {update.effective_user.first_name}')


    app = ApplicationBuilder().token("6963085023:AAHeorUslbIFCXdADcyRZEfzQYmsanOYSJ4").build()

    app.add_handler(CommandHandler("hello", hello))

    app.run_polling()

with daemon.DaemonContext():
    main()