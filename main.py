import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to SecurePass!\n\n"
        "Use /generate to create a strong password.\n"
        "Use /check to test a password's strength.\n"
        "Use /help for more info."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Main menu\n"
        "/generate - Generate a secure password\n"
        "/check - Check password strength\n"
        "/help - Show this message"
    )

async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    import secrets
    import string
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(secrets.choice(alphabet) for _ in range(16))
    await update.message.reply_text(f"Your secure password:\n\n`{password}`", parse_mode="Markdown")

def main():
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN is not set!")
    
    print("Bot is starting...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("generate", generate))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
