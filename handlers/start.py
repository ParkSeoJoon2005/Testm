from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from handlers import __version__
from helpers.decorators import sudo_users_only
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["mstart", f"mstart@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_private(client: Client, message: Message):
    await message.reply_text(
        f""" [☘️](https://telegra.ph/file/a8d7b996ab1696894dda4.jpg)ƑҽҽӀ Ͳհąէ Ɱվʂէҽɾìօմʂ...""",
     
    


@Client.on_message(

    command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited

)

async def start_group(client: Client, message: Message):

    current_time = datetime.utcnow()

    uptime_sec = (current_time - START_TIME).total_seconds()

    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(

        [

            [

                InlineKeyboardButton("✨ Group", url=f"https://t.me/{GROUP_SUPPORT}"),

                InlineKeyboardButton(

                    "📣 Channel", url=f"https://t.me/{UPDATES_CHANNEL}"

                ),

            ]

        ]

    )
               
               
            
       
    

    alive = f"**ђєɭɭ๏{message.from_user.mention()}, I'm{BOT_NAME}**\n\n◉**I'm Online!**\n ◉ᴍᴀꜱᴛᴇʀ:`ᴛʜᴇ ᴀᴜʀᴏʀᴀ ᴘʀᴏᴊᴇᴄᴛ`\n◉ᴠᴇʀꜱɪᴏɴ: `v{__version__}`\n ◉ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ: `{pyrover}`\n◉ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ: `{__python_version__}`\n◉ᴍᴏɴɢᴏ ᴅᴀᴛᴀʙᴀꜱᴇ:´ᴡᴏʀᴋɪɴɢ´ \n◉ᴜᴘᴛɪᴍᴇ: `{uptime}`Aurora❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(
    command(["mhelp", f"mhelp@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""┏━━━[⚙️](https://telegra.ph/file/36fdb173afe664d96b058.jpg)ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʙᴀꜱɪᴄ ʜᴇʟᴘ ꜰᴏʀ ᴍᴜꜱɪᴄ ʙᴏᴛ ━━━┓""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="🌙ʙᴀꜱɪᴄ ʜᴇʟᴘ", callback_data="cbguide")]]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴘɪɴɢɪɴɢ...")
    delta_ping = time() - start
    await m_reply.edit_text( `PONG!!`\n" f" `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🌙ꜱᴛᴀᴛꜱ:\n"
        f"• **ᴜᴘᴛɪᴍᴇ:** `{uptime}`\n"
        f"• **ꜱᴛᴀʀᴛ ᴛɪᴍᴇ:** `{START_TIME_ISO}`"
    )
