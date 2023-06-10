import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
import os
token = os.getenv("TOKEN")  


intents = discord.Intents().all()

bot = commands.Bot(command_prefix=":", intents=intents, help_command=None, status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name=":help"))

@bot.event
async def on_ready():
    print(f"ONLINE AS {bot.user}")

@bot.command()
async def say(ctx, msg: str):
    await ctx.channel.send(msg)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="commands", color=discord.Colour.red())

    embed.add_field(name="say", value=":say {arg}", inline=False)
    await ctx.send(embed=embed)

bot.run(token)
