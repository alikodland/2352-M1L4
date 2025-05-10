import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hai! Saya adalah bot {bot.user}!')

@bot.command()
async def selamatpagi(ctx):
    await ctx.send("Halo, selamat pagi juga kamu.")

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

bot.run("MTM2ODIwNjMzMzYzOTEzNTI3NQ.G1OS_t.gh_ibEjM4DWC6_uBHCUMrrYMJYimcLaHyD91oo")


