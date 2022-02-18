import discord
import os
from dotenv import load_dotenv
from discord.ext.commands import Bot

load_dotenv()
TOKEN = os.getenv('token')
client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0,user}'.format(client))

bot = Bot('!')
@bot.command()
async def test(ctx):
  await ctx.send("This is a tts message", tts=True)

@client.event
async def on_message(message):
  if message.author ==  client.user:
    return
  if message.content.startswith('kawa'):
    await message.channel.send('<@378979413255258132>, você é o cara!', tts=True)

client.run(TOKEN)

