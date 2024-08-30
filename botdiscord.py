import discord
from discord.ext import commands
import asyncio
intents = discord.Intents.default()
intents.message_content = True  # Enable privileged intent
client = commands.Bot(command_prefix='i.', intents=intents)

token = "сюда токен бота"

curseWord = ['бот', 'привет', 'гей', 'скибиди', 'свинья', 'бонзи', 'аш', 'родаки', 'дискорд', 'жестко', 'жёстко', 'украина', 'россия', 'Спокойной ночи', 'споки', 'петух', 'хуй', 'БЛИЯ' 'спать' 'ссылка', 'споки', 'ссылкам', 'чо', 'аяко' 'Спокойной!', 'сво', 'UwU', 'OwO', 'линукс', 'виндовс', 'да', 'нет', 'что', 'кто', 'как' 'почему', 'какой', 'ку', 'когда', 'бота', 'добавил', 'ебало', 'похуй', 'ноль', 'пиздец', 'пидор', 'пидорас', 'пидорасы','пидоры','сука', 'нахуй', 'нахер', 'нахуя', 'нафиг', 'нафига', 'мусор', 're', 'лох','король', 'хохол', 'хай' ]


@client.listen('on_message')
async def whatever_you_want_to_call_it(message):
    msg_content = message.content.lower()
    if any(word in msg_content for word in curseWord):

        await message.channel.send(f"{message.author.mention} ты ахуел печатать на мое сообщение? на гифке кстати ты https://tenor.com/view/yukleniyor-gif-18955750")


    else:
        return

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('```Укажите аргументы```')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("```Вы не имеете права```")


@client.event
async def on_ready():
    print("start")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="i.info"))

@client.command()
async def info(ctx):
    await ctx.send('test_info')

client.run(token)
