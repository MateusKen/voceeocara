import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('token')
client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0,user}'.format(client))

@client.event
async def on_message(message):
  if message.author ==  client.user:
    return
  if message.content.startswith('kawa'):
    await message.channel.send('<@378979413255258132> você é o cara!')

client.run(TOKEN)

