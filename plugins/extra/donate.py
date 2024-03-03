from pyrogram import Client, filters

from Zenaku import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("donate")
    & filters.group)
async def donate(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/f73af9a4ffe130a83d8d2.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧 𝐅𝐨𝐫 𝐃𝐨𝐧𝐚𝐭𝐞 & 𝐂𝐥𝐢𝐜𝐤 𝐁𝐞𝐥𝐨𝐰 𝐁𝐢𝐤𝐚𝐬𝐡 𝐨𝐫 𝐀𝐝𝐢𝐭𝐲𝐚 𝐅𝐨𝐫 𝐐𝐫 𝐂𝐨𝐝𝐞, 𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬 𝐎𝐫 𝐎𝐭𝐡𝐞𝐫𝐬 𝐋𝐢𝐧𝐤 𝐓𝐡𝐞𝐧 𝐂𝐥𝐢𝐜𝐤 𝐎𝐭𝐡𝐞𝐫𝐬 𝐁𝐮𝐭𝐭𝐨𝐧 & 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐎𝐫 𝐆𝐫𝐨𝐮𝐩.. 🥀 [𝐘𝐨𝐮𝐭𝐮𝐛𝐞](https://youtube.com/@Huu-12_2k?si=0qeQ63u0HTMJ59Sl)..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " Zenaku ", url=f"https://t.me/mamee_is_my_existence")
            ],          
                [
                    InlineKeyboardButton(
                        " 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ", url=f"https://t.me/seriosvs_version10"
                    ),
                    InlineKeyboardButton(
                        " 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 ", url=f"https://t.me/seriosvs_version20")
                ]
            ]
        ),
    )
