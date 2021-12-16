import os
import asyncio
import time
import discord
import yaml
from discord.ext import commands

imp = 'Json/'
if os.path.exists(imp + 'BotSettings.yaml'):
	with open(imp + 'BotSettings.yaml') as t:
		t = yaml.load(t, Loader=yaml.FullLoader)
		PREFIX = t.get('Prefix', '')
		TOKEN = t.get('Token', '')
		repo = t.get('Repo', '')
		ver = t.get('version', '')
else:
	PREFIX = '$'
	TOKEN = ''
	repo = ''
	ver = ''

async def get_pre(bot, message):
	return PREFIX

intents = discord.Intents.all()
Bot = discord.Client()
bot = commands.Bot(command_prefix=get_pre, pm_help=None, description="I'm a really boy ...", game=" with Scooby Chan", case_insensitive=True, intents=intents)

bot.repo = repo
bot.res = time.localtime()

@bot.event
async def on_ready():
	print('I have awaken')

@bot.event
async def on_message(message):
	if message.author.bot:
		return

print('PREFIX:', PREFIX if PREFIX != '' else 'missing')
print('TOKEN:', 'Valid' if TOKEN != '' else 'missing')
print('REPO:', repo if repo != '' else 'missing')
print('Git version:', ver if ver != '' else 'missing')

if not TOKEN == '':
	while True:
		try:	
			# Initialise Mass Destruction
			if TOKEN:
				bot.run(TOKEN, bot=True, reconnect=True)
			else:
				print('I have no TOKEN')
				break
		except discord.errors.HTTPException:
			print('Connection issues, waiting 30secs')
			time.sleep(30)

		except RuntimeError:
			print('Shutting down by keyboard')
			break
else:
	input([' ENTER '])