import discord
from discord.ext import commands
import random
import os
from model import *

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command()
async def subtract(ctx, number1: int, number2: int):
    await ctx.send(number1 - number2)

@bot.command()
async def meme(ctx):
    Imagenes = random.choice(os.listdir("Imágenes"))
    with open(f"Imágenes/{Imagenes}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def recicleadvice(ctx):
    recicle_advice = ["Organiza tu día para poder saber cuándo haces qué.", "Lleva tu propia bolsa al supermercado.", "Recuerda apagar las luces y cerrar el agua de los grifos cuando no las estés utilizando."]
    await ctx.send(random.choice(recicle_advice))

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url

            await attachment.save(f"./{file_name}")
            clase=get_class("keras_model.h5" , "labels.txt" , f"./{file_name}")
            await ctx.send(f"Imagen guardada en./{file_url}")

            if clase[0] == "Battle Cats":
                await ctx.send("Esto es un gato.")
            elif clase[0] == "Battle Dogs":
                await ctx.send("Esto es un perro.")
    else:
        await ctx.send("No has subido ninguna imagen:(")
