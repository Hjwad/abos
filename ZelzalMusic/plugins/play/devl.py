#sos


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from ZelzalMusic import app
import config


@app.on_message(
    command(["المطور", "السورس", "المصنع"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://te.legra.ph/file/08cec0a2a844713e1624a.jpg",
        caption="~ Not ᥉ꪮ᥉ . \n~ Dev BY ᥉ꪮ᥉ ",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- Dev Bot .", url=f"https://t.me/lllBY"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "- Not ᥉ꪮ᥉ . ", url=config.SUPPORT_CHAT
                    ),
                ],
            ]
        ),
    )
