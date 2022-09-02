import discord
import os
import config
from twython import Twython, TwythonError

token = Twython(config.TOKEN)

client = discord.client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!!')

client.run(os.getenv('TOKEN'))
