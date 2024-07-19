import wikipedia
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, command

wiki_router: Router=Router()

wikipedia.set_lang("uz")

def wiki_bot(text):
    try:
        result = wikipedia.summary(text)
        return result
    except:
        return "kechirasiz bunday malumot topilmadi"
    
@wiki_router.message()
async def wiki_handler(msg: Message):
    text = msg.text
    await msg.reply(wiki_bot(msg.text))
