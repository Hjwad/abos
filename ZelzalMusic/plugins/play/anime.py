#sos
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ZelzalMusic import app, Telegram
import random
from config import ASAAQ_CHANNEL, YAFA_NAME
import asyncio
from pyrogram import Client, filters
from random import choice
from strings import get_command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)



@app.on_message(filters.command(["انمي","صور انمي"],"")) 
async def ihd(client: Client, message: Message):
    rs = random.randint(166,212)
    url = f"https://t.me/aftarat56/{rs}"
    await client.send_photo(message.chat.id,url,caption="✧---------✧ [sos](t.me/mmmsc) ",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/lllby")
                ],
            ]
        )
    )
