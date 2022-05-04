from pyrogram import Client,filters
from pyrogram.types import ReplyKeyboardMarkup
import math
import os
import youtube_dl
import pornhub
import random
# ======            ======#
api_id = 2802662
api_hash = 'b8a41227faa9481313ecfa661ef50ef4'
Token = '1912172231:AAHvDazD0KgjWv2I5iNoPSs0-pIjrvddXjY' #ØªÙˆÚ©Ù† Ø±Ø¨Ø§Øª
# ======            ======#
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=Token)
#---------  (  ) ---------#
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
def setfile(name,chat_id,data=''):
    try:
        f = open('data\\'+chat_id+'\\'+name, "w", encoding="Utf-8")
        f.write(data)
    except:
        f = open('data\\'+chat_id+'\\'+name, "a", encoding="Utf-8")
        f.write(data)
    return True
def getfile(name,chat_id):
    f = open('data\\'+chat_id+'\\'+name, "r", encoding="Utf-8")
    contents = f.read()
    return contents
#---------  (  ) ---------#
back = ReplyKeyboardMarkup(['ðŸ”™'],resize_keyboard=True)
menu = ReplyKeyboardMarkup(
            [
                ["ðŸ”search video"],
                ["ðŸ“¥download video"],
                ["ðŸª§help"]
            ],resize_keyboard=True)
#---------  (  ) ---------#
@app.on_message(filters.text and filters.private)
async def Bot(Client , message):
    text = message.text
    chat_id = message.chat.id
    chatid = str(chat_id)
    if os.path.isdir(f"data\\{chatid}"):
        pass
    else:
        os.mkdir(f"data\\{chatid}")
        setfile('step.txt',chatid)
    step = getfile('step.txt',chatid)
    if text == '/start' or text == 'ðŸ”™':
        setfile('step.txt',chatid)
        await message.reply_text('Welcome to Robot Downloader.\n\nðŸ', quote=True,reply_markup=menu)
    if text == 'ðŸ”search video':
        setfile('step.txt',chatid,'s')
        await message.reply_text('ðŸ”Ž Send your **text** to **search video**.\nâš ï¸ **Do not be long **.\n\nðŸ @python3_channel', quote=True,reply_markup=back)
    if text == 'ðŸ“¥download video':
        setfile('step.txt',chatid,'d')
        await message.reply_text('ðŸ“¹send your **video link** to **download**.\n\nðŸ @python3_channel', quote=True,reply_markup=back)
    if text == 'ðŸª§help':
        await message.reply_text('**In the search section, you can search for the desired video**.\n**In the download section, you can download it by sending the movie link**.\n\nðŸ @python3_channel', quote=True)
    if step == 's' and text != 'ðŸ”™':
        r = random.randrange(10)
        try:
            search_keywords = [str(""+text)]
            client = pornhub.PornHub(search_keywords)
            for video in client.getVideos(5,page=int(r)):
                await app.send_photo(chat_id,str(video["background"]),f"á‘Žá—©á—°E: <code>"+video["name"]+"</code>\nð—Ÿð—¶ð—»ð—¸: `"+video["url"]+"`\nð——ð˜‚ð—¿ð—®ð˜ð—¶ð—¼ð—»ï¼„1¤7"+video["duration"])
            await app.send_message(chat_id=chat_id,text="ðŸ”™We returned to the main menu",reply_markup=menu)
            setfile('step.txt',chatid)
        except:
            await message.reply_text("âŒTá•¼Eá–‡E Iá”„1¤7 á—„1¤7 á‘­á–‡Oá—·á’ªEá—„1¤7!")
    if step == 'd' and text != 'ðŸ”™':
            m = await message.reply_text("ð—½ð—¹ð—²ð—®ð˜€ð—² ð˜„ð—®ð—¶ð˜")
            try:
                dire = '/data/{}/%(title)s.%(ext)s'.format(chatid)
                ydl_opts = {
                    'format': 'best',
                    'outtmpl': dire,
                    'nooverwrites': True,
                    'no_warnings': False,
                    'ignoreerrors': True,
                    }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([text])
                    await m.edit_text('âœ…download\nðŸ”œUpload')
                    for item in os.scandir('data/{}'.format(chatid)):
                        if '.mp4' in item.name:
                            size = convert_size(os.path.getsize('data\\{}\\{}'.format(chatid,item.name)))
                            await app.send_document(chat_id, 'data\\{}\\{}'.format(chatid,item.name),caption=f'''
    ðŸ“¹É´á´„1¤7á´á´‡ : {item.name}
    ðŸ“¦êœ±Éªá´¢á´„1¤7 : {size}
    ðŸ”—ÊŸÉªÉ´á´„1¤7 : {text}
                                        ''')
                            os.remove('data\\{}\\{}'.format(chat_id,item.name))
                            await app.send_message(chat_id=chat_id,text="ðŸ”™We returned to the main menu",reply_markup=menu)
                    setfile('step.txt',chatid)
                    await m.edit_text('âœ…download\nâœ…Upload')
            except:
                await message.reply_text("âŒTá•¼Eá–‡E Iá”„1¤7 á—„1¤7 á‘­á–‡Oá—·á’ªEá—„1¤7!")
app.run()
