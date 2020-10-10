import discord
import random
import datetime
import json
# import spacy
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import CommandNotFound

with open("config/config.json", "r") as config:
    data = json.load(config)
    
with open("data/ben_data.json", "r") as f:
    ben_data = json.load(f)
    
TOKEN = data["token"]
PREFIX = data["prefix"]
BEN_ID = "213501169077583884"
DATA = "data/ben_data.json"
client = commands.Bot(command_prefix = PREFIX)
nlp = None



@client.event
async def on_ready():
    # await client.change_presence(game = Game(name = "with RESTful API's"))
    print('Logged in as')
    print(client.user.name)
    print('------')
    '''
    nlp = spacy.load('en_core_web_lg')
    print('Modules Loaded:')
    if nlp: print('\tSpacy')
    '''
    await client.change_presence(activity=discord.Game(name='!help for bot info', type=1))
    
    
    
@client.command(name='ben',
                description='says a random thing that ben has said in this server')
async def ben_says(ctx):
    await ctx.send(random.choice(list(ben_data.values())))
    
 
    
@client.command(name='ping',
                description='pong')
async def ping(ctx):
    await ctx.send('pong')
   
   
    
# @client.command(name='scrub',
#                 description='scrub for ben\'s messages')
# async def scrub(ctx):
#     messages = {}
#     count = -1
#     for channel in ctx.guild.text_channels:
#         async for message in channel.history(limit=1000000):
#             if str(message.author.id) == BEN_ID and message.content:
#                 count += 1
#                 messages[count] = message.content
#                 print(message.content)
    
#     # print(messages)   
#     with open(DATA, "w") as f:
#         json.dump(messages, f)
        
#     print("Done")
#     await client.close()
    
 
client.run(TOKEN)