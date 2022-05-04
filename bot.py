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
Token = '1912172231:AAFqazBULPeaYY3rPjHdEAKWCH6n0EykLoA' #鬲賵讴賳 乇亘丕鬲
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
back = ReplyKeyboardMarkup(['馃敊'],resize_keyboard=True)
menu = ReplyKeyboardMarkup(
            [
                ["馃攳search video"],
                ["馃摜download video"],
                ["馃help"]
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
    if text == '/start' or text == '馃敊':
        setfile('step.txt',chatid)
        await message.reply_text('馃尫Welcome to Robot Porn Downloader.\n\n馃悕 @python3_channel', quote=True,reply_markup=menu)
    if text == '馃攳search video':
        setfile('step.txt',chatid,'s')
        await message.reply_text('馃攷 Send your **text** to **search video**.\n鈿狅笍 **Do not be long **.\n\n馃悕 @python3_channel', quote=True,reply_markup=back)
    if text == '馃摜download video':
        setfile('step.txt',chatid,'d')
        await message.reply_text('馃摴send your **video link** to **download**.\n\n馃悕 @python3_channel', quote=True,reply_markup=back)
    if text == '馃help':
        await message.reply_text('**In the search section, you can search for the desired video**.\n**In the download section, you can download it by sending the movie link**.\n\n馃悕 @python3_channel', quote=True)
    if step == 's' and text != '馃敊':
        r = random.randrange(10)
        try:
            search_keywords = [str(""+text)]
            client = pornhub.PornHub(search_keywords)
            for video in client.getVideos(5,page=int(r)):
                await app.send_photo(chat_id,str(video["background"]),f"釕庒棭釛癊: <code>"+video["name"]+"</code>\n饾棢饾椂饾椈饾椄: `"+video["url"]+"`\n饾棗饾槀饾椏饾棶饾榿饾椂饾椉饾椈锛�"+video["duration"])
            await app.send_message(chat_id=chat_id,text="馃敊We returned to the main menu",reply_markup=menu)
            setfile('step.txt',chatid)
        except:
            await message.reply_text("鉂孴釙糆釚嘐 I釘� 釛� 釕枃O釛丰挭E釛�!")
    if step == 'd' and text != '馃敊':
            m = await message.reply_text("饾椊饾椆饾棽饾棶饾榾饾棽 饾槃饾棶饾椂饾榿")
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
                    await m.edit_text('鉁卍ownload\n馃敎Upload')
                    for item in os.scandir('data/{}'.format(chatid)):
                        if '.mp4' in item.name:
                            size = convert_size(os.path.getsize('data\\{}\\{}'.format(chatid,item.name)))
                            await app.send_document(chat_id, 'data\\{}\\{}'.format(chatid,item.name),caption=f'''
    馃摴纱岽�岽嶀磭 : {item.name}
    馃摝隃鄙储岽� : {size}
    馃敆薀瑟纱岽� : {text}
                                        ''')
                            os.remove('data\\{}\\{}'.format(chat_id,item.name))
                            await app.send_message(chat_id=chat_id,text="馃敊We returned to the main menu",reply_markup=menu)
                    setfile('step.txt',chatid)
                    await m.edit_text('鉁卍ownload\n鉁匲pload')
            except:
                await message.reply_text("鉂孴釙糆釚嘐 I釘� 釛� 釕枃O釛丰挭E釛�!")
app.run()
