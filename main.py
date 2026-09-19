import os
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
app = ApplicationBuilder().token(TOKEN).build()
