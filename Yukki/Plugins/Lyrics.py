import os
import re

import lyricsgenius
from pyrogram import Client, filters
from pyrogram.types import Message
from youtubesearchpython import VideosSearch

from Yukki import MUSIC_BOT_NAME, app

__MODULE__ = "Lyrics"
__HELP__ = """

/Lyrics [Music Name]
- Searches Lyrics for the particular Music on web.

**Note**:
Inline button of Lyrics has some bugs. Searches only 50% results. You can use command instead if you want lyrics for any playing music.

"""


@app.on_callback_query(filters.regex(pattern=r"lyrics"))
async def lyricssex(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    try:
        id, user_id = callback_request.split("|")
    except Exception as e:
        await CallbackQuery.message.edit(
            f"Error Occured\n**Possible reason could be**:{e}"
        )
        return await app.send_sticker(message.chat.id,"CAACAgEAAx0CWu9UpwABH15VYn504DePgj3jctiQYfMrijZ3y7gAAugBAAKvuehHroFJDcriobEkBA")
    url = f"https://www.youtube.com/watch?v={id}"
    print(url)
    try:
        results = VideosSearch(url, limit=1)
        for result in results.result()["result"]:
            title = result["title"]
    except Exception as e:
        await CallbackQuery.answer(
            "Sound not found. Youtube issues.", show_alert=True
        )
        return await app.send_sticker(message.chat.id,"CAACAgEAAx0CWu9UpwABH15VYn504DePgj3jctiQYfMrijZ3y7gAAugBAAKvuehHroFJDcriobEkBA")
    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    t = re.sub(r"[^\w]", " ", title)
    y.verbose = False
    S = y.search_song(t, get_full_info=False)
    if S is None:
        await CallbackQuery.answer(
            "Lyrics not found :p", show_alert=True
        )
        return await app.send_sticker(message.chat.id,"CAACAgEAAx0CWu9UpwABH15VYn504DePgj3jctiQYfMrijZ3y7gAAugBAAKvuehHroFJDcriobEkBA")
    await CallbackQuery.message.delete()
    userid = CallbackQuery.from_user.id
    usr = f"[{CallbackQuery.from_user.first_name}](tg://user?id={userid})"
    xxx = f"""
**Lyrics Search Powered By {MUSIC_BOT_NAME}**

**Searched By:-** {usr}
**Searched Song:-** __{title}__

**Found Lyrics For:-** __{S.title}__
**Artist:-** {S.artist}

**__Lyrics:__**

{S.lyrics}"""
    return await app.send_sticker(message.chat.id,"CAACAgEAAx0CWu9UpwABH15VYn504DePgj3jctiQYfMrijZ3y7gAAugBAAKvuehHroFJDcriobEkBA")
    if len(xxx) > 4096:
        filename = "lyrics.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(xxx.strip()))
        await CallbackQuery.message.reply_document(
            document=filename,
            caption=f"**OUTPUT:**\n\n`Lyrics`",
            quote=False,
        )
        return await app.send_sticker(message.chat.id,"CAACAgEAAx0CWu9UpwABH15VYn504DePgj3jctiQYfMrijZ3y7gAAugBAAKvuehHroFJDcriobEkBA")
        os.remove(filename)
    else:
        await CallbackQuery.message.reply_text(xxx)


@app.on_message(filters.command("lyrics"))
async def lrsearch(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:**\n\n/lyrics [ Music Name]")
    m = await message.reply_text("Searching Lyrics")
    query = message.text.split(None, 1)[1]

    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    y.verbose = False
    S = y.search_song(query, get_full_info=False)
    if S is None:
        await m.edit("Lyrics not found")
        return await app.send_sticker(message.chat.id,"CAACAgEAAx0CZ9BLhAADJ2J--ZcDthxSuYHxU1b2RYO8Kg6EAALCAgACh77pR7xwL6V4JH51JAQ")
    xxx = f"""
{thumb = "Utils/Playlist.jpg"}
**Lyrics Search Powered By {MUSIC_BOT_NAME}**

**Searched Song:-** __{query}__
**Found Lyrics For:-** __{S.title}__
**Artist:-** {S.artist}

**__Lyrics:__**

{S.lyrics}"""
    if len(xxx) > 4096:
        await m.delete()
        filename = "lyrics.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(xxx.strip()))
        await message.reply_document(
            document=filename,
            caption=f"**OUTPUT:**\n\n`Lyrics`",
            quote=False,
        )
        return await app.send_sticker(message.chat.id,"CAACAgEAAx0CWu9UpwABH15VYn504DePgj3jctiQYfMrijZ3y7gAAugBAAKvuehHroFJDcriobEkBA")
        os.remove(filename)
    else:
        await m.edit(xxx)
