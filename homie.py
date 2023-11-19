import os
import random

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

games = ["cs2", "battlebit", "aoe", "lol", "wot"]


@bot.command()
async def game(ctx):
    await ctx.send(random.choice(games))


bot.run(os.environ["HOMIE_TOKEN"])
