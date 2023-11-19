import requests
import responses
import discord
from discord.ext import commands
from bot_token import *

client = commands.Bot(command_prefix="!!",  # Prefix to use commands is "!!"
                      intents=discord.Intents.all(), help_command=None)


@client.event
async def on_ready():
    print("-----------------")
    print("B-shaan active")
    print("-----------------")
    await client.change_presence(status=discord.Status.online)


@client.command()
async def hello(ctx):
    await ctx.send("Hello!")


@client.command()
async def complement(ctx, *args):
    '''
    This command takes *args as args, which
    is all text after the prefix.

    If there is an arg give, it will be held
    at the index [0]
    '''
    if len(args) == 0:
        await ctx.channel.send(f'{ctx.author.name} is cool!')
    else:
        await ctx.channel.send(f'{args[0]} is cool!')


@client.command()
async def bye(ctx, *args):
    if len(args) == 0:
        await ctx.channel.send("bye bye everyone :wave: :smile:")
    else:
        await ctx.channel.send(f'bye bye {args[0]}! :smile:')


@client.command()
async def kiss(ctx, *args):
    if len(args) == 0:
        await ctx.channel.send(f":kissing_heart: a kiss for you, {ctx.author.name}")
    else:
        await ctx.channel.send(f':kissing_heart: a kiss for you, {args[0]}')


@client.command()
async def hug(ctx, *args):
    if len(args) == 0:
        await ctx.channel.send(f":people_hugging: I am here for you, {ctx.author.name}")
    else:
        await ctx.channel.send(f':people_hugging: I am here for you, {args[0]}')


@client.command()
async def cookie(ctx, *args):
    if len(args) == 0:
        await ctx.channel.send(f"thanks for the cookie, {ctx.author.name} :cookie: :yum:")
    else:
        await ctx.channel.send(f":cookie: a cookie for you, {args[0]}! :yum:")


@client.command()
async def credits(ctx):
    embed = discord.Embed(title="B-shaan", url="https://github.com/IshaanTakrani",
                          description="Created by Ishaan Takrani\n Version 0.3", color=0xff33cc)
    await ctx.send(embed=embed)


@client.command()
async def suggestion(ctx, *, suggestion):
    with open("suggestions.txt", "a") as f:
        f.write(f'{ctx.author.name}: {suggestion}\n')
    await ctx.send("noted :)")


@client.command()
async def stats(ctx):
    stats = responses.getStats()
    embed = discord.Embed(title="Stats", url="https://www.yourworldoftext.com/ishaanbot",
                          description=f'Good bot: {stats[0]}\nBad bot: {stats[1]}', color=0xff33cc)
    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
    embed = discord.Embed(title="Ishaan", url="https://www.yourworldoftext.com/ishaanbot",
                          description='''
                          hello
                          question
                          affirmation
                          bye <target>
                          kiss <target>
                          hug <target>
                          complement <target>
                          suggestion <suggestion> - Leave a suggestion
                          ''', color=0xff33cc)
    await ctx.send(embed=embed)


@client.command()
async def question(ctx):
    r = requests.get("https://api.truthordarebot.xyz/v1/truth")
    res = r.json()
    await ctx.send(res['question'])


@client.command()
async def name(ctx):
    await ctx.send("Hello! My name is B-shaan :)")


@client.command()
async def affirmation(ctx):
    r = requests.get("https://www.affirmations.dev/")
    res = r.json()
    await ctx.send(res['affirmation'])


@client.event
async def on_message(message):

    await client.process_commands(message)

    try:
        if message.author != client.user:
            response = responses.handle_response(
                message.content, message.author)
            await message.channel.send(response)
    except:
        pass


client.run(bot_token)   # use the token for your bot in place of "bot_token"
