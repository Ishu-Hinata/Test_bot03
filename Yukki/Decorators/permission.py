from typing import Dict, List, Union

from Yukki import BOT_ID, app


def PermissionCheck(mystic):
    async def wrapper(_, message):
        if message.chat.type == "private":
            return await mystic(_, message)
        a = await app.get_chat_member(message.chat.id, BOT_ID)
        if a.status != "administrator":
    await message.reply_text(
                "I need to be admin with some permissions:\n"
                + "\n- **can_manage_voice_chats:** To manage voice chats"
                + "\n- **can_delete_messages:** To delete Bot's Searched Waste"
                + "\n- **can_invite_users**: For inviting assistant to chat."
            )
           return await app.send_sticker(message.chat.id,"CAACAgEAAx0CWu9UpwABHz_tYnz-KhmcOXLNVXdTD_bwR7vd5q4AAtMBAAKcg-hHW5ettUjivtEkBA")
            
        if not a.can_manage_voice_chats:
    await message.reply_text(
                "I don't have the Fackin permission to perform this action....Just give Admin rights alredy (ノ｀Д´)"
                + "\n**Permission:** __MANAGE VOICE CHATS__"
            )
            await app.send_sticker(message.chat.id,"CAACAgEAAx0CWu9UpwABH0AVYn0Eqd5JjWyglYJ_hTnIunT3sXEAAk0DAAITxulHgwa4nEH6gUQkBA")
            
            return
        if not a.can_delete_messages:
    await message.reply_text(
                "I don't have the Fackin required permission to perform this action...Give right (>.<)"
                + "\n**Permission:** __DELETE MESSAGES__"
            )
             await app.send_sticker(message.chat.id,"CAACAgEAAx0CWu9UpwABH0AfYn0FjFN6TQqP4RjZ6z4ibe7bI_MAApICAAKYSOlHvd1h3OfYxA4kBA")
            
            return
        if not a.can_invite_users:
    await message.reply_text(
                "I don't have the Fackin required permission to Invite my Music Assistant. ( ･ั﹏･ั)"
                + "\n**Permission:** __INVITE USERS VIA LINK__"
            )
                await app.send_sticker(message.chat.id,"CAACAgEAAx0CWu9UpwABH0AkYn0GCihMa8Sgmk5xJ1SThPDbR_0AAooCAAJ-5-FHsLJ4QxovBbgkBA")
            
            return
        return await mystic(_, message)

    return wrapper
