# Fate

import discord

from colorama import init, Fore, Style
from random import randint as throw

client = discord.Client()
init(autoreset=True)
TOKEN = open('token.txt', 'r').read()
welcome = open('welcome.txt', 'r')

for line in welcome: print(Fore.BLUE + line, end="")
print()

@client.event
async def on_ready():
    print(f"{Fore.GREEN + Style.BRIGHT}bot is ready")

@client.event
async def on_connect():
    print(f"{Fore.GREEN + Style.BRIGHT}bot is connected to discord")

@client.event
async def on_disconnect():
    print(f"{Fore.RED + Style.BRIGHT}bot has disconnected from discord")

@client.event
async def on_message(message):
    if message.content.startswith('roll'):
        split = message.content.split(' ')
        result = str(throw(1, int(split[1])))
        print(f"{Fore.LIGHTCYAN_EX + message.author.name + Fore.BLUE} rolled a {Fore.LIGHTCYAN_EX + split[1] + Fore.BLUE} sideddie and got a {Fore.LIGHTCYAN_EX + result}")
        await message.channel.send(f"**{message.author.name}** rolled a **{split[1]}** sided die and got a __**{result}**__ from the throw")

client.run(TOKEN)
TOKEN.close()
welcome.close()