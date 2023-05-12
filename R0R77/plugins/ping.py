import os

from telethon import Button, events

from R0R77 import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/68a7ca5269cc0144832af.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@Aemoli"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@R0R77.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("المطور", "https://t.me/Aemoli")]]
    await R0R77.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
