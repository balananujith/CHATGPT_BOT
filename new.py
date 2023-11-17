import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set your Telegram Bot token and OpenAI API key
TELEGRAM_TOKEN = '6324222449:AAEU1mJ_1kRWgXGyXIOfVQw15OnglNkveDw'
openai.api_key = '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'

# Initialize the Telegram updater
updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define the start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! I am your ChatGPT bot. Send me a message, and I will try to generate a response.')

# Define the help command handler
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Send me any message, and I will generate a response for you.')

# Define the message handler
def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    # Use OpenAI GPT to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=150
    )
    bot_reply = response['choices'][0]['text']
    update.message.reply_text(bot_reply)

# Add command handlers to the dispatcher
start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help_command)
message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
updater.idle()

