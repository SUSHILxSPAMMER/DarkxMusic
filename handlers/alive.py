import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/afac20e0707e8cfc6f041.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
Hᴇʟʟᴏ ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍs ɢʀᴏᴜᴘs...
┏━━━━━━━━━━━━━━━━━┓
┣★ Uᴘᴅᴀᴛᴇs : [Dᴇᴍᴏɴ Cʀᴇᴀᴛᴏʀs](https://t.me/TAG_BAN)
┣★ Sᴜᴘᴘᴏʀᴛ : [Wᴏʀʟᴅ FʀɪᴇɴᴅSʜɪᴘ Zᴏɴᴇ](https://t.me/clan8xofficial)
┣★ Oᴡɴᴇʀ   : [8x Cobra](https://t.me/Simple_Mundaa)
┣★ Fᴇᴍᴀʟᴇ Oᴡɴᴇʀ : [niShu](https://t.me/sushil8xop)
┗━━━━━━━━━━━━━━━━━┛
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "Sumit"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/1b99b29043777af4e3898.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/clan8xofficial")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["NishuxMusic","Nishu", "#Channel", "@Channel", "/Channel", "Channel"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/afac20e0707e8cfc6f041.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Uᴘᴅᴀᴛᴇs", url=f"https://t.me/clan8xofficial")
                ]
            ]
        ),
    )
