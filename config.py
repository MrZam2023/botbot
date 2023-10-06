from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

PROXY_URL = "http://proxy.server:3128"
storage = MemoryStorage()
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN_ID = 372062006
ANIMATION_PIC = '/Users/HUAWEI/PycharmProjects/telegram_bot/media/chatbot-kiu.gif'
GROUP_ID = -4049093253
DESTINATION_DIR = '/Users/HUAWEI/PycharmProjects/telegram_bot/media'

