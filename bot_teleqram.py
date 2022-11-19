from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot('5661889481:AAF-NOlg7eGAyHtOFLuFXy48__wBiDn1KMM')
dp = Dispatcher(bot)

async  def on_startup(_):
    print('Бот вышел онлайн')


# **********************klient part***********************
@dp.message_handler(commands = ['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного Аппетита!')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, НАПИШИТЕ ему:\nhttps:/t.me/custom_pizza_bot')

@dp.message_handler(commands = ['Режим_Работы'])
async def pizza_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9 до 20, Пн-Сб с 10 до 23')

@dp.message_handler(commands = ['Адрес'])
async def pizza_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Улица Самед Вургуна 55')

# **********************admin part part***********************

# **********************general part***********************



       
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp, skip_updates = True, on_startup=on_startup)

