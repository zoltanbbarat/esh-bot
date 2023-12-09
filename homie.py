import os
import random
import re
import logging

import discord
from discord.ext import commands

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

game_list = ["cs2", "battlebit", "aoe", "lol", "wot"]


class EmotionalSupportHomieBot(commands.Bot):
    def __init__(self, *, intents: discord.Intents):
        super().__init__("/", intents=intents)

        @self.command()
        async def game(ctx):
            logging.info(f"Game command called by {ctx.author}")

            exclude_list = re.findall(r"(?<=-)[^\s]+", ctx.message.content)
            random_game = random.choice([x for x in game_list if x not in exclude_list])

            try:
                await ctx.send(random_game)
            except Exception as e:
                logging.error(e)

        @self.command()
        async def add(ctx):
            logging.info(f"Add command called by {ctx.author}")
            game = ctx.message.content.split(" ")[1]
            game_list.append(game)
            try:
                await ctx.send(f"Added {game} to the game list.")
            except Exception as e:
                logging.error(e)

        @self.command()
        async def remove(ctx):
            logging.info(f"Remove command called by {ctx.author}")
            game = ctx.message.content.split(" ")[1]
            game_list.remove(game)
            try:
                await ctx.send(f"Removed {game} from the game list.")
            except Exception as e:
                logging.error(e)

    async def on_ready(self):
        logging.info(f"We have logged in as {self.user}")


if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True

    try:
        esh = EmotionalSupportHomieBot(intents=intents)
        esh.run(os.environ["HOMIE_TOKEN"])
    except Exception as e:
        logging.error(e)
