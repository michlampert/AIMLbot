# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')



import aiml
from utils import *

sessionId = 12345

kernel = aiml.Kernel()
kernel.learn("data/*")

todo_list = []

kernel.setPredicate("list", make_ul(todo_list), sessionId)
kernel.setPredicate("func", "", sessionId)
kernel.setPredicate("arg", "", sessionId)
kernel.setPredicate("topic", "DEFAULT", sessionId)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.lower()

    respond = kernel.respond(content, sessionId)

    func = kernel.getPredicate("func", sessionId)

    if func == "google":
        arg = kernel.getPredicate("arg", sessionId)
        info = get_info(arg)
        respond = respond.replace("#", info)
        kernel.setPredicate("func", "", sessionId)
        kernel.setPredicate("arg", "", sessionId)
    elif func == "weather":
        arg = kernel.getPredicate("arg", sessionId)
        info = get_weather(arg)
        respond = respond.replace("#", info)
        kernel.setPredicate("func", "", sessionId)
        kernel.setPredicate("arg", "", sessionId)
    elif func == "add":
        arg = kernel.getPredicate("arg", sessionId)
        add_task(todo_list, arg)
        kernel.setPredicate("list", make_ul(todo_list), sessionId)
        kernel.setPredicate("func", "", sessionId)
        kernel.setPredicate("arg", "", sessionId)
    elif func == "delete":
        arg = kernel.getPredicate("arg", sessionId)
        delete_task(todo_list, arg)
        kernel.setPredicate("list", make_ul(todo_list), sessionId)
        kernel.setPredicate("func", "", sessionId)
        kernel.setPredicate("arg", "", sessionId)
    elif func == "reset":
        reset(todo_list)
        kernel.setPredicate("list", make_ul(todo_list), sessionId)
        kernel.setPredicate("func", "", sessionId)
        kernel.setPredicate("arg", "", sessionId)

    if respond:
        for line in respond.split("€"):
            if line.strip(): await message.channel.send(line)

client.run(TOKEN)

# respond = kernel.respond("edytuj")
# print(respond)

# respond = kernel.respond("dodaj dupa")
# print(respond)

# respond = kernel.respond("pokaz liste")
# print(respond)