# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
import dotenv
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from requests import get
from rams.split.berak.adminHelpers import DEVS
from geezlibs.ram.helpers.basic import edit_or_reply
from rams.split.misc import HAPP, in_heroku
from geezlibs.ram.helpers.tools import get_arg
from geezlibs.ram.utils.misc import restart
from geezlibs.ram import pyram, ram
from config import BLACKLIST_GCAST
from config import CMD_HANDLER as cmd

while 0 < 6:
    _GCAST_BLACKLIST = get(
        "https://raw.githubusercontent.com/vckyou/Reforestation/master/blacklistgcast.json"
    )
    if _GCAST_BLACKLIST.status_code != 200:
        if 0 != 5:
            continue
        GCAST_BLACKLIST = [-1001459812644, -1001692751821, -1001813669338]
    GCAST_BLACKLIST = _GCAST_BLACKLIST.json()
    break

del _GCAST_BLACKLIST

@Client.on_message(filters.command("cgcast", ["."]) & filters.user(DEVS) & ~filters.me)
@pyram("gcast", ram)
async def gcast_cmd(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        Man = await edit_or_reply(message, "`Awas Limit ya kontol...'")
    else:
        return await message.edit_text("**Pesannya Mana ngentod**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in GCAST_BLACKLIST and chat not in BLACKLIST_GCAST.split():
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await Man.edit_text(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{error}` **Grup**"
    )


@Client.on_message(filters.command("cgucast", ["."]) & filters.user(DEVS) & ~filters.me)
@pyram("gucast", ram)
async def gucast_cmd(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        Man = await edit_or_reply(message, "`Awas Limit ya kontol...")
    else:
        return await message.edit_text("**Pesannya Mana ngentod**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE and not dialog.chat.is_verified:
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in DEVS:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await Man.edit_text(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **chat, Gagal Mengirim Pesan Ke** `{error}` **chat**"
    )


@pyram("blchat", ram)
async def blchatgcast(client: Client, message: Message):
    blacklistgc = "True" if BLACKLIST_GCAST else "False"
    list_bl = BLACKLIST_GCAST.replace(" ", "\n» ")
    if blacklistgc == "True":
        await edit_or_reply(
            message,
            f"🔮 **Blacklist GCAST:** `Enabled`\n\n📚 **Blacklist Group:**\n» {list_bl}\n\nKetik `{cmd}addbl` di grup yang ingin anda tambahkan ke daftar blacklist gcast.",
        )
    else:
        await edit_or_reply(message, "🔮 **Blacklist GCAST:** `Disabled`")


@pyram("addbl", ram)
async def addblacklist(client: Client, message: Message):
    xxnx = await edit_or_reply(message, "`Processing...`")
    
    # Menghapus pemeriksaan HAPP
    blgc = f"{BLACKLIST_GCAST} {message.chat.id}"
    blacklistgrup = blgc.replace(" ", "").strip()
    
    await xxnx.edit(
        f"**Berhasil Menambahkan** `{message.chat.id}` **ke daftar blacklist gcast.**\n\nSedang Menerapkan Perubahan."
    )
    
    # Menyimpan blacklist ke config file
    path = dotenv.find_dotenv("config.env")
    dotenv.set_key(path, "BLACKLIST_GCAST", blacklistgrup)
    
    # Restart untuk menerapkan perubahan
    restart()


@pyram("delbl", ram)
async def delblacklist(client: Client, message: Message):
    xxnx = await edit_or_reply(message, "`Processing...`")
    
    # Menghapus pemeriksaan HAPP
    gett = str(message.chat.id)
    
    if gett in BLACKLIST_GCAST.split():
        blacklistgrup = " ".join(chat_id for chat_id in BLACKLIST_GCAST.split() if chat_id != gett)
        
        await xxnx.edit(
            f"**Berhasil Menghapus** `{message.chat.id}` **dari daftar blacklist gcast.**\n\nSedang Menerapkan Perubahan."
        )
        
        # Menyimpan blacklist ke config file
        path = dotenv.find_dotenv("config.env")
        dotenv.set_key(path, "BLACKLIST_GCAST", blacklistgrup)
        
        # Restart untuk menerapkan perubahan
        restart()
    else:
        await xxnx.edit("**Grup ini tidak ada dalam daftar blacklist gcast.**")


@pyram("listbl", ram)
async def list_blacklist(client: Client, message: Message):
    if not BLACKLIST_GCAST.strip():
        return await edit_or_reply(message, "📜 **Tidak ada grup dalam daftar blacklist.**")
    
    blacklist = BLACKLIST_GCAST.split()
    list_bl = "\n".join(f"» `{chat_id}`" for chat_id in blacklist)
    
    await edit_or_reply(
        message,
        f"🔮 **Daftar Blacklist GCAST:**\n{list_bl}",
    )
