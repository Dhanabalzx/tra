# TradingView Python Bot (No Webhook Version)

This bot simulates signal monitoring from TradingView and sends alerts to Telegram.

## Features

- Free to use with TradingView (no webhook required)
- Simulates price condition (replace with real logic)
- Sends alerts to your Telegram bot

## Setup

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Replace `BOT_TOKEN` and `CHAT_ID` in `main.py` with your actual Telegram bot token and chat ID.

3. Run the bot:
```
python main.py
```

## Notes

- This version simulates alerts. You can upgrade it to fetch actual chart data using Selenium or `tvdatafeed`.
- For real-time data, consider scraping chart values or using broker APIs.