import Constants as keys
import Response as R
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters
import json
import sys
sys.path.append('Method/News')
import News

print("Bot Starting....")

def start_command(update: Update, context: CallbackContext) -> None:
  update.message.reply_text(f'Chào {update.effective_user.first_name}')

def help_command(update: Update, context: CallbackContext):
  update.message.reply_text("Bạn muốn tôi giúp gì? \n 1. Đọc báo -> /news <số lượng>")

def news_command(update: Update, context: CallbackContext):
  try:
    limit_news = int(context.args[0])
    news = News.GetNews(limit_news)
    for x in range(0, len(news)):
      message = json.loads(news[x])
      update.message.reply_text(message['title'] + "\n" 
        + message['link'] + "\n" + message['description'])
  except (IndexError, ValueError):
    update.message.reply_text('Vui lòng chọn số lượng tin hiển thị!!')

def handle_message(update: Update, context: CallbackContext):
  text = str(update.message.text).lower()
  response = R.sample_response(text)
  update.message.reply_text(response)

def error(update: Update, context: CallbackContext):
  print(f"Update {update} cause error {context.error}")

def main():
  updater = Updater(keys.API_KEY, use_context=True)
  dp = updater.dispatcher
  dp.add_handler(CommandHandler("start", start_command))
  dp.add_handler(CommandHandler("help", help_command))
  dp.add_handler(CommandHandler("news", news_command))
  dp.add_handler(MessageHandler(Filters.text, handle_message))
  dp.add_error_handler(error)

  updater.start_polling()
  updater.idle()

main()
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler


# def start_message(update: Update, context: CallbackContext) -> None:
#   update.message.reply_text(f'Hello {update.effective_user.first_name}')
# def help_command(update: Update, context: CallbackContext) -> None:
#   update.message.reply_text("Bạn muốn tôi giúp gì?")
# def main():
#   updater = Updater(keys.API_KEY)
#   dp = updater.dispatcher
#   dp.add_handler(CommandHandler('hello', hello))
#   updater.start_polling()
#   updater.idle()

# main()