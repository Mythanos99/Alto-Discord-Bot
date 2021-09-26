import discord
import random
import requests
import json
from discord.ext import commands
from names import name

client = commands.Bot(command_prefix='!')

# def get_countries():
#     response=requests.get("https://restcountries.eu/rest/v2/all")
#     json_data=json.loads(response.text)
#     name=json_data[0]['name']


@client.event
async def on_ready():
    print("Ready to go")


@client.command(aliases=['hi', 'bonjour'])
async def hello(ctx):
    await ctx.send('Hello There')

# @client.command
# async def random_countries(ctx):
#         countries=get_countries()
#         await message.channel.send(countries)


@client.command(aliases=['gn', 'bye'])
async def goodnight(ctx):
    await ctx.send('Bye Bye')


@client.command()
async def country(ctx):
     response = random.choice(name)
     await ctx.send(response)


@client.command()
async def play(ctx):
    await ctx.send("Type a country with letter s")

    @client.event
    async def on_message(message):
        first_letter='s'                                                  
        if message.author == client.user:
          return
        if (first_letter).lower() != ((message.content)[0]).lower():
          await message.channel.send("The first letter should be correct!")
          return
        if message.content not in name:
            await message.channel.send("Sorry this country does not exist") 
            
        # if message in append_list :
        #     await message.channel.send("This country is already used ")
     



    # new country here
        word_list = [idx for idx in name if idx[0].lower() == message.content[len(message.content)-1].lower()] 
    # while true:
    
        country_bot = random.choice(word_list)                       
        await message.channel.send(country_bot)
    #    if country_bot not in append_list :                       
    #        return country_bot
    # #    if word_list==append_list :
        # if message.content.startswith("end"): 
        #   return
        # else :
        #  await message.channel.send("Check")
        



           


client.run('ODU2NDg5OTIzNTA1NTUzNDU5.YNByZg.dLq1j_Hi-5w0bNQgujb2143YfM4')
