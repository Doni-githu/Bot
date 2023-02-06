import math

from aiogram import Bot, Dispatcher, executor, types
import requests

token = '6127784633:AAF-jj_p-jGKLaSffb-W86DdnkYQPfTuBLI'

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def hello(message: types.Message):
    await message.answer("Привет я бот")


@dp.message_handler()
async def get_info(message: types.Message):
    API_KEY = "fed36d5b11391ccf093a50d12b5d59c0"
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={message.text}&appid={API_KEY}"
    response = requests.get(url)
    asd = response.json()
    for i in asd:
        lon = i['lon']
        lat = i['lat']
        url_2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
        response = requests.get(url_2)
        zxc = response.json()
        main = zxc['main']
        temp = main['temp']
        s = temp - 273.15
        await message.answer(f'Градус {math.ceil(s)}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
