from pyrogram import filters
from UsuMusic import app


@app.on_message(filters.command("advice"))
async def advice(_, message):
    A = await message.reply_text("...")
    res = await utils.TheApi.get_advice()
    await A.edit(res)


__MODULE__ = "Advice"
__HELP__ = """<blockquote>/advice - Get random advice</blockquote>"""