import nextcord
from nextcord.ext import commands
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

import altcoin_watcher_bot

prefix = "*"
bot = commands.Bot(command_prefix = prefix, intents = nextcord.Intents.all())

cg_api_url = "https://api.coingecko.com/api/v3/coins/markets?"

#https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name= "ticker")
@bot.slash_command(name = "ticker")
async def ticker():
    pass


bot.run(altcoin_watcher_bot.token)