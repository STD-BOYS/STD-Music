import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
💔 Hey {message.from_user.mention()} !

This Is [{bn}](t.me/{bu}), A Super Fast VC Player Bot For Telegram Group VideoChats...

Press /help to see all the commands and how they work!
┏━━━━━━━━━━━━━━┓
┣★
┣★Made By: [𝐓𝐄𝐀𝐌 𝐒𝐓𝐃~🇮🇳](t.me/STD_DEEPANSHU)
┣★
┗━━━━━━━━━━━━━━┛

💞 If You Have Any Questions About Me Then DM To My[👑Owner👑](t.me/STD_DEEPANSHU).....
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕Add Me To Your Chat➕", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "👑Owner👑", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "[► Instagram ◄]​", url=f"https://www.instagram.com/deep_meena_99/"
                    )
                ],[
                    InlineKeyboardButton(
                        "[►Inline🔎◄]", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "[► 𝐒𝐓𝐃 𝐆𝐑𝐎𝐔𝐏💬 ◄]", url=f"https://t.me/{SUPPORT_GROUP}"
                    )],[
                    InlineKeyboardButton(
                        "𝐒𝐓𝐃 𝐔𝐏𝐃𝐀𝐓𝐄 Or More✅", url=f"https://t.me/STD_Vs_LIFELINE"
                       ),
                  ]
            ]
       ),
    )

