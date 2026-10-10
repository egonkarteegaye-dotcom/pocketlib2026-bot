import asyncio, random, os
from datetime import datetime, timedelta
from telegram import Bot
TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
async def main():
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHANNEL_ID, text="🤖 GONKARTEE SON ROBOT (P-OPT) 🔥✅ STARTED!")
    pairs = ["EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY", "AUD/USD"]
    while True:
        try:
            msg = f"🤖 GONKARTEE SON ROBOT (P-OPT) 🔥✅\n📊 {random.choice(pairs)}\n📈 {random.choice(['BUY UP 🟢','BUY DOWN 🔴'])}\n⏰ Entry: {(datetime.utcnow()+timedelta(minutes=2)).strftime('%H:%M')} UTC\n⏰ Expiry: 5 MIN"
            await bot.send_message(chat_id=CHANNEL_ID, text=msg)
            await asyncio.sleep(900)
        except Exception as e:
            print(e)
            await asyncio.sleep(60)
asyncio.run(main())
