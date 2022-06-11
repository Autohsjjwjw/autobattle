from pyrogram import Client, filters
import time

import schedule
import threading

app = Client(
    "session",
    api_id=000000,
    api_hash="api hash"
)



        
@app.on_message(filters.private & filters.text)
def dspam(client, message):
    if '/challenge raju' in message.text:

        n = message.reply_to_message.message_id

        def oof(n):
            client.send_message(message.chat.id, '/challenge ', reply_to_message_id=n)

        schedule.every(180).seconds.do(oof, n)

        def forever():
            while True:
                schedule.run_pending()
                time.sleep(1)

        t1 = threading.Thread(target=forever)
        t1.start()


    if 'Daily' in message.text:

        try:
           x = message.message_id
           client.send_message(
              chat_id=message.chat.id,
              text="kdjfieodj",
              reply_to_message_id=x
           )
        except Exception as e:
           client.send_message('KamibutEvil', e)
           client.send_message('KamibutEvil', message.text)

    if 'King has defeated Rocky\nDaily limit' in message.text:

        try:
           x = message.message_id
           client.send_message(
              chat_id=message.chat.id,
              text="/kickme",
              reply_to_message_id=x
           )
        except Exception as e:
           client.send_message('KamibutEvil', e)
           client.send_message('KamibutEvil', message.text)

    for i in range(0, 3):
        try:
            message.click("Ready ✅")
            time.sleep(0.3)
        except:
            pass 

    if 'kdjfieoajajiajwj' in message.text:

        try:
           x = message.message_id
           client.send_message(
              chat_id=message.chat.id,
              text="/trade",
              reply_to_message_id=x
           )
        except Exception as e:
           client.send_message('KamibutEvil', e)
           client.send_message('KamibutEvil', message.text)


while True:
    try:
        app.run()
    except:
        time.sleep(15)
