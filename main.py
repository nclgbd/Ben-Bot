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
DYLAN_ID = "127611871003017218"
ZAE_ID = "108299700599271424"
CAIT_ID = "210001707814354945"
DATA = "data/ben_data.json"
client = commands.Bot(command_prefix = PREFIX)
nlp = None
DYLAN = f'<@!{DYLAN_ID}>'
ZAE = f'<@!{ZAE_ID}>'
CAIT = f'<@!{CAIT_ID}>'
global dylan_count
dylan_count = 0
global zae_count
zae_count = 0


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
    
    
@client.command(name='cait',
                description='simply says happy birthday to cait')
async def happy_birthday_cait(ctx):
    await ctx.send(f'Happy Birthday {CAIT}')
    
    
@client.command(name='ben',
                description='says a random thing that ben has said in this server')
async def ben_says(ctx):
    resp = random.choice(list(ben_data.values()))
    await ctx.send(resp)
    
    if DYLAN in resp:
        global dylan_count
        await ctx.send(f"Dylan streak has been broken! Ben Bot messages since last ping: {dylan_count}")
        dylan_count = 0
        
    if ZAE in resp:
        global zae_count
        await ctx.send(f"Zaenia streak has been broken! Ben Bot messages since last ping: {zae_count}")
        zae_count = 0
        
    dylan_count += 1
    zae_count += 1
    
 
@client.command(name='dylan',
                description="returns how long it's been since ben bot inadvertently pings dylan")
async def ping_dylan(ctx):
    await ctx.send(f"Dylan hasn't been inadvertently pinged in {dylan_count} commands")
    
    
@client.command(name='zae',
                description="returns how long it's been since ben bot inadvertently pings dylan")
async def ping_dylan(ctx):
    await ctx.send(f"Zaenia hasn't been inadvertently pinged in {zae_count} commands")
 
    
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