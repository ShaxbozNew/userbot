import os
try:
    from telethon.sync import TelegramClient
    from telethon import TelegramClient,events,sync
    from telethon import functions,types
except:
    os.system('pip install telethon')
    from telethon.sync import TelegramClient
    from telethon import TelegramClient,events,sync
    from telethon import functions,types

bot = input("Shaxboz")
api_id = 10279988
api_hash = "cc10c52f2706c2e5969b366e3cab421c"
client = TelegramClient(bot,api_id,api_hash)
client.start()
@client.on(events.NewMessage)
async def my_event_handler(event):
    if event.raw_text == "M":
        await event.edit("Men olaman bu nomerdi roʻyxatdan oʻtkizaman ")
    elif event.raw_text == "K":
        await event.edit("kod ketdi 🕛 ")
        await event.edit("kod ketdi 🕛 ")
        await event.edit("kod ketdi 🕐 ")
        await event.edit("kod ketdi 🕐 ")
        await event.edit("kod ketdi 🕑 ")
        await event.edit("kod ketdi 🕑 ")
        await event.edit("kod ketdi 🕒 ")
        await event.edit("kod ketdi 🕒 ")
        await event.edit("kod ketdi 🕓 ")
        await event.edit("kod ketdi 🕓 ")
        await event.edit("kod ketdi 🕔 ")
        await event.edit("kod ketdi 🕔 ")
        await event.edit("kod ketdi 🕕 ")
        await event.edit("kod ketdi 🕕 ")
        await event.edit("kod ketdi 🕖 ")
        await event.edit("kod ketdi 🕖 ")
        await event.edit("kod ketdi 🕗 ")
        await event.edit("kod ketdi 🕗 ")
        await event.edit("kod ketdi 🕘 ")
        await event.edit("kod ketdi 🕘 ")
        await event.edit("kod ketdi 🕙 ")
        await event.edit("kod ketdi 🕙 ")
        await event.edit("kod ketdi 🕚 ")
        await event.edit("kod ketdi 🕚 ")
        await event.edit("kod ketdi 🕛 ")
        await event.edit("kod ketdi 🕛 ")
    elif event.raw_text == "O":
        await event.edit("Ovoz berdi boʻldi 🎉🎉🎉")
    elif event.raw_text == "Y":
        await event.edit("Boʻmadi vaqt tugadi ✖️")
    elif event.raw_text == "Q":
        await event.edit("Qaytatdan urunamiz ")
    elif event.raw_text == ".help":
                              await event.edit("M \nO \nK \nY \nQ")
                              
                              
                        
client.run_until_disconnected()        