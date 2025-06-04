import time
import requests
from telegram import Bot
from datetime import datetime

# Replace with your bot token and chat ID
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


# Simulate getting data from TradingView (replace with actual scraping or TV API workaround)
def get_trading_signal():
    # This is mock logic. Replace it with actual logic to scrape TradingView or read signals.
    # You can use tvdatafeed or Selenium to get real chart data.
    current_minute = datetime.now().minute
    if current_minute % 2 == 0:
        return "BUY", 48200
    elif current_minute % 3 == 0:
        return "SELL", 48600
    else:
        return None, None

def send_telegram_alert(message):
    bot = Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)

def main():
    print("Starting TradingView Bot...")
    while True:
        signal, level = get_trading_signal()
        if signal:
            msg = f"🔔 {signal} Signal Triggered for Bank Nifty Options at Level: {level}"
            print(msg)
            send_telegram_alert(msg)
        time.sleep(60)

if __name__ == "__main__":
    main()
