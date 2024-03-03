from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Zenaku import config
from Zenaku import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=" ᴄᴏᴍᴍᴀɴᴅꜱ ",
                url=f"https://t.me/{BOT_USERNAME}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text=" ʙᴏᴛ ꜱᴇᴛᴛɪɴɢ ", callback_data="settings_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text=" ᴄʜᴀɴɴᴇʟ ", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text=" ɢʀᴏᴜᴘ ", url=config.SUPPORT_GROUP
            )
        ],
        ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=" ᴀᴅᴅ ʏᴏᴜʀ ɢʀᴏᴜᴘ ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text=" Help ", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text=" ᴄʜᴀɴɴᴇʟ ", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text=" ɢʀᴏᴜᴘ ", url=config.SUPPORT_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                text=" ᴏᴡɴᴇʀ ", user_id=OWNER
            )
        ]
     ]
    return buttons
