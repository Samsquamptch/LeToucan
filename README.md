# LeToucan
A simple Discord bot which produces buttons on any channel called "toucan" in a server. Pressing a button will cause the bot to post the appropriate ASCII art stored in toucan.py. Le Toucan is configured to run concurrently on multiple servers, provided the relevant channel exists. Users may also praise Le Toucan by saying "praise him" (this is not case sensitive), which will cause the bot to respond.

Messages sent by the bot either via button interactions on praising le toucan will all automatically be deleted after 5 seconds. If any user other than the bot owner says anything other than "praise him", these will be instantly deleted and the bot will direct message the user telling them to only praise Le Toucan. if the bot owner says anything else, the messages will simply be deleted.

COMMANDS:
There is only one command for the bot, which is `!refresh`. This purges the messages in the channel and reposts the buttons, however as the buttons are set to never timeout and the bot will automatically refesh itself on restart, this should be unnecessary.

PLEASE NOTE: The bot is currently configured to run on Replit, which means you'll need to store a secret with the key TOKEN and the value as your Discord bot token (more information here https://docs.replit.com/programming-ide/workspace-features/secrets). You'll also need to configure a keepalive function if you want the bot to be constantly running. Finally, Replit currently uses Python 3.10.8 and there are differences in positional arguments when defining buttons compared to earlier versions.

in 3.10.8, defining the 'toucan' button is as follows:
```python
@discord.ui.button(label="Summon le toucan", emoji="🪶", style=discord.ButtonStyle.blurple)
async def toucan(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(content=TOUCAN, delete_after=5)
```

On earlier versions of Python, you may need to change this to:
```python
@discord.ui.button(label="Summon le toucan", emoji="🪶", style=discord.ButtonStyle.blurple)
async def toucan(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(content=TOUCAN, delete_after=5)
```

Please keep this in mind if you get an AttributeError about missing arguments!
