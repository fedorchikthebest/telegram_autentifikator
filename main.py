import json

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from whitelist_operations import add_to_whitelist

with open('config.json', 'r') as f:
    data = json.loads(f.read())
bot = Bot(token=data.get('token'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши свой ник в minecraft\n"
                        "(Ник сменить будет нельзя)")


@dp.message_handler()
async def echo_message(msg: types.Message):
    if add_to_whitelist(msg.text, msg.from_user.id):
        await bot.send_message(msg.from_user.id,
                               'Вы были добывлены в вайт лист')
    else:
        await bot.send_message(msg.from_user.id,
                               'Похоже вы уже регистрировались с этого'
                               ' аккаунта или этот ник уже есть на сервере')


if __name__ == '__main__':
    executor.start_polling(dp)