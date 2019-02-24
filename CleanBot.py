import discord
from discord.ext import commands

TOKEN = ""
client = commands.Bot(command_prefix = "./")
filename = "dirtyWords.txt"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command(pass_context = True)
async def clean(ctx):
    textChannels = getTextChannels()
    dirtyWords = getDirtyWords()
    for channel in textChannels:
        print(channel)
        await deleteMessages(channel, dirtyWords)


def getTextChannels():
    textChannels = []
    for server in client.servers:
        for channel in server.channels:
            if ("text" in str(channel.type)):
                textChannels.append(channel)
    return textChannels

def getDirtyWords():
    file = open(filename, "r")
    return [line.strip() for line in file]


async def deleteMessages(channel, dirtyWords):
    msgs =[msg async for  msg  in client.logs_from(channel, limit = 100000)]
    for m in msgs:
        content = str(m.content)
        for word in dirtyWords:
            if word in content.lower():
                await client.delete_message(m)
                break



client.run(TOKEN)
