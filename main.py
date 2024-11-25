import random

import discord
import aiohttp
import ssl
import certifi
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = "MTI5NTM0NDc2NTU2MjUxOTYwNQ.G4wgPG.17TnCp71Qn6BBeI2Fftcbh38NpZ7VysUebrBno"

@bot.command()
async def set_nick(ctx, member: discord.Member, *, new_nickname: str):
    """Change the nickname of a member."""
    try:
        await member.edit(nick=new_nickname)  # Attempt to change the nickname
        await ctx.send(f'Successfully changed nickname to {new_nickname} for {member.mention}. I dont get paid enough for this')
    except discord.Forbidden:
        await ctx.send("I don't have permission to change that user's nickname. Doofus")
    except discord.HTTPException as e:
        # Handle general HTTP errors
        await ctx.send(f"Failed to change nickname: {e.status} - {e.text}. You goofed up")
    except Exception as e:
        # Handle any other unexpected errors
        await ctx.send(f"An unexpected error occurred: {str(e)}. Have fun fixing that bro!")


@bot.command()
async def set_all(ctx, *, new_nickname: str):
    """Change the nickname for all members in all guilds."""
    try:
        for guild in bot.guilds:
            for member in guild.members:
                try:
                    await member.edit(nick=new_nickname)
                except discord.Forbidden:
                    await ctx.send(f'I do not have permission to change {member.display_name}\'s nickname. Stupid meat bag')
                except discord.HTTPException as e:
                    await ctx.send(f'Failed to change nickname for {member.display_name}: {e.status} - {e.text}. Get good.')
                except Exception as e:
                    # Handle unexpected exceptions
                    await ctx.send(f'An unexpected error occurred for {member.display_name}: {str(e)}. Get good.')
        await ctx.send('Donezo. I take payment in cash or credit')
    except Exception as e:
        await ctx.send(f'An error occurred while trying to change nicknames: {str(e)}. Get good.')

@bot.command()
async def moe_track(ctx):
    channel = bot.get_channel(757394688390070325)
    cities = ["Paris", "Tokyo", "Gotham City", "Cape Town", "Metropolis", "Sydney", "Ulaanbaatar",
              "Atlantis", "Berlin", "Lima", "Wakanda", "Dubai", "Antananarivo", "Nairobi", "Rivendell",
              "Toronto", "Rapture", "Luanda", "Seoul", "Vienna", "Manaus", "Vientiane", "Miami", "Asgard",
              "Stockholm", "Vilnius", "Casablanca", "Kuala Lumpur", "Dublin", "San Jose", "Tbilisi", "Arkham",
              "Budapest", "Atlantis", "King's Landing", "El Paso", "New New York", "Metru Nui", "Tallinn",
              "Emerald City", "Springfield"]
    i = random.randint(0, len(cities) - 1)
    city = cities[i]
    enemies = ["taxes", "the government", "his father", "Batman", "a pack of street dogs", "the marine corp", "Sir Crunchy", "his evil twin Boe Mamba", "capitalism", "the power"]
    e = random.randint(0, len(enemies) - 1)
    enemy = enemies[e]
    await channel.send(f'Moe Bamba is current off fighting {enemy} in {city}!')


@bot.event
async def on_ready():
    channel = bot.get_channel(757394688390070325)
    await channel.send(f'Did somebody call for me, the legendary {bot.user}?')
    print(f'Did somebody call for me, the legendary {bot.user}?')

@bot.event
async def on_disconnect():
    channel = bot.get_channel(757394688390070325)
    await channel.send(f'Bravo six, going dark')
    print(f'Bravo six, going dark')

def main() -> None:
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
