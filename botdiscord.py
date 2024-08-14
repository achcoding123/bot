import discord
from discord.ext import commands
import asyncio
intents = discord.Intents.default()
intents.message_content = True  # Enable privileged intent
client = commands.Bot(command_prefix='i.', intents=intents)

token = "токен сюда"

curseWord = ['ты', 'я']

@client.listen('on_message')
async def whatever_you_want_to_call_it(message):
    msg_content = message.content.lower()
    if any(word in msg_content for word in curseWord):
        await message.delete()
        await message.channel.send(f"{message.author.mention} ты ахуел печатать на мое сообщение? на гифке кстати ты https://tenor.com/view/yukleniyor-gif-18955750")
        await message.channel.send(f"{message.author.mention} я запрещаю вам какать")
        await message.channel.send(f"{message.author.mention} https://tenor.com/view/pornhub-logo-click-gif-15797009 это то что ты смотришь ночью в 3 часа ночи когда твои родители родаки отказались от тебя")
        await message.channel.send(f"{message.author.mention} https://tenor.com/view/patrick-bateman-sigma-yes-gif-26992928 это я")
        await message.channel.send(f"{message.author.mention} ты хуй")
        await message.channel.send(f"{message.author.mention} https://cdn.discordapp.com/attachments/854356203505451081/1088485991779684352/a1f2fc775cce630c.gif?ex=66bad453&is=66b982d3&hm=e6a52f20324a35fb49fb174e4c7a9162447425d5c2a284b8f3b641d0775eb418& вылитый ты")
        await message.channel.send(f"{message.author.mention} https://tenor.com/view/brainlet-gif-22807865 ыыыыыыыыыыыыыы смотри как они на тебя похожи, прям точь в точь, принтер, это твои друзья кстати, я забыл упомянуть")
        await message.channel.send(f"{message.author.mention} https://tenor.com/view/bike-head-ding-ding-gif-14702293 дзинь дзинь")
        await message.channel.send(f"{message.author.mention} https://tenor.com/view/dumb-wojak-brainlet-hamster-gif-25308901 смотри какой красавец, прям на тебя похож")
        await message.channel.send(f"{message.author.mention} https://tenor.com/view/dumb-stupid-brainlet-wojak-meme-gif-17170021 это ты")
        await message.channel.send(f"{message.author.mention} https://tenor.com/view/wojak-blocks-dumb-gif-25774850 смотри какой умный челик, прям как ты, прям на тебя похож, один в один")
        await message.channel.send(f"{message.author.mention} не угрожай или я не дам ключ деадлок и отменю буст на сервере через неделю")
        await message.channel.send(f"{message.author.mention} https://tenor.com/view/ras-lmixeur-bahloul-gif-18258457 крута")
        await message.channel.send(f"{message.author.mention} https://tenor.com/view/brainlet-windmill-gif-20767515 я слышал ты любишь воду, и с помощью этой информации я тебя сватнул докснул сдеанонил и даже заказал спортиков это вода если чё, и вот твое лицо хахахахахахха")
        await message.channel.send(f"{message.author.mention} https://tenor.com/view/flipping-off-flip-off-middle-finger-smile-happy-gif-4746862")
        
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
