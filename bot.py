import os

import discord
from discord.ext import commands

from toucan import ELEPHANT, SHREK, TOUCAN

toucanToken = os.environ['TOKEN']


class AsciiArtButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Summon le toucan", emoji="🪶",
                       style=discord.ButtonStyle.blurple)
    async def toucan(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(content=TOUCAN, delete_after=5)

    @discord.ui.button(label="Summon elephant", emoji="🐘",
                       style=discord.ButtonStyle.red)
    async def elephant(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(content=ELEPHANT, delete_after=5)

    @discord.ui.button(label="Summon SHREK", emoji="🧅",
                       style=discord.ButtonStyle.green)
    async def shrek(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(content=SHREK, delete_after=5)


def find_channel(server):
    channel = discord.utils.get(server.channels, name="toucan")
    if channel:
        print(f'channel found {channel.id}')
    else:
        channel = 0000000000000000000
        print(f'channel "toucan" does not exist for server: {server}')
    return channel


async def produce_buttons(channel):
    await channel.purge()
    await channel.send(content="Le toucan bot has arrived")
    await channel.send(view=AsciiArtButton())


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        for server in bot.guilds:
            channel = find_channel(server)
            await produce_buttons(channel)
        print('bot now running!')

    @bot.command()
    async def refresh(ctx):
        channel = find_channel(ctx.guild)
        if ctx.message.channel == channel and bot.is_owner:
            await produce_buttons(channel)

    @bot.listen()
    async def on_message(message):
        if message.author == bot.user:
            return

        server_channel = find_channel(message.guild)
        channel = bot.get_channel(server_channel.id)
        user_message = str(message.content)

        if message.channel != channel:
            pass
        elif "praise him" in user_message.lower():
            await message.channel.send(content="All praise le great toucan", delete_after=5)
            await message.delete(delay=5)
        elif bot.is_owner:
            await message.delete()
        else:
            await message.author.send(
                'The toucan channel is only for praising le toucan. Type "praise him" and nothing else.')
            await message.delete()

    bot.run(toucanToken)
