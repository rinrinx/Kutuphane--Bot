import asyncio
import logging
from info import AUTH_CHANNEL, FORCE_TXT, BUTTON_TEXT, LOG_CHANNEL, LOG_TEXT_P
from pyrogram.errors import FloodWait, UserNotParticipant, ChatAdminRequired
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
logger = logging.getLogger(__name__)

async def handle_force_subscribe(bot, message):
    try:
        date = message.date + 120
        invite_link = await bot.create_chat_invite_link(AUTH_CHANNEL, expire_date=date, member_limit=1)
    except ChatAdminRequired:
        logger.error("Bot'un Kanalında yönetici olduğundan emin olun.")
        return 400
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return 400
    try:
        user = await bot.get_chat_member(AUTH_CHANNEL, message.from_user.id)
        if user.status == "banned":
            await bot.delete_messages(
                chat_id=message.chat.id,
                message_ids=message.message_id,
                revoke=True
            )
            return 400
    except UserNotParticipant:
        btn = [
            [
                InlineKeyboardButton(
                    BUTTON_TEXT, url=invite_link.invite_link
                )
            ]
        ]
        await bot.send_message(
            chat_id=message.from_user.id,
            text=FORCE_TXT,
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode="markdown",
            reply_to_message_id=message.message_id,
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Bir şeyler ters gitti.",
            parse_mode="markdown",
            disable_web_page_preview=True,
            reply_to_message_id=message.message_id,
        )
        return 400
