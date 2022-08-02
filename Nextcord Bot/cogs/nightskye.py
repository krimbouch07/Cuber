#-----Imports-----
import nextcord
import random
import asyncio
import aiohttp

import string


from nextcord.ext import commands
from nextcord import Interaction

#-----Commands-----  
class nightsky(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	#Nightsky
	@nextcord.slash_command(name = 'nightsky', description = '🌕Send a Nightskye for you (Exaple: /nightsky)')
	async def nightsky(self, ctx: Interaction):
		await ctx.send("\n".join(['.\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000 ✦ \u3000\u3000\u3000\u3000\u2002\u2002 \u3000', 
			'\u3000\u3000\u3000˚\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000*\u3000\u3000\u3000\u3000\u3000\u3000\u2008',
			'\u2008\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000.\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000.', 
			'\u3000\u3000\u2008\u3000\u3000\u3000\u3000\u3000\u3000\u3000 ✦ \u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000 \u3000 \u200d \u200d \u200d \u200d \u3000\u3000\u3000\u3000 \u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000,\u3000\u3000\u2002\u2002\u2002\u3000',
			'', '.\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000.\u3000\u3000\u3000ﾟ\u3000\u2002\u2002\u3000\u3000\u3000.\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000.',
			'', '\u3000\u3000\u3000\u3000\u3000\u3000,\u3000\u3000\u3000\u3000\u3000\u3000\u3000.\u3000\u3000\u3000\u3000\u3000\u3000\u2008\u2008\u2008\u2008\u3000\u3000\u3000\u3000:alien:', 
			'\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u2008\u2008',
			'\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000:sunny:\u3000\u3000\u2008\u2008\u200a\u200a\u3000\u2008\u2008\u2008\u2008\u2008\u200a\u3000\u3000\u3000\u3000\u3000\u2008\u2008\u200a\u200a\u2008\u2008\u200a\u200a\u3000\u3000\u3000\u3000*\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000.', 
			'\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000.\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000.', 
			'\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u200a\u200a\u200a\u2008\u2008\u200a\u200a\u3000\u2008\u2008\u2008\u3000\u3000\u3000\u3000', 
			'\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u200a\u200a\u200a\u2008\u2008\u200a\u200a\u3000\u2008\u2008\u2008\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u200a\u200a\u200a\u2008\u2008\u200a\u200a\u3000\u2008\u2008\u2008 ✦', 
			'\u3000\u2002\u2002\u2002\u3000\u3000\u3000,\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000*\u3000\u3000\u2008\u200a\u200a\u200a \u3000\u3000\u3000\u3000 \u3000\u3000,\u3000\u3000\u3000 \u200d \u200d \u200d \u200d \u3000 \u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000.\u3000\u3000\u3000\u3000\u3000\u2008\u3000\u3000', 
			'\u3000\u3000\u3000.\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u2008\u3000\u200a\u200a\u2008\u2008\u2008\u2008\u2008\u2008\u2008\u200a\u200a\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000˚\u3000\u3000\u3000', 
			'\u3000 \u2002\u2002\u3000\u3000\u3000\u3000,\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u200a\u200a\u200a\u200a\u200a\u200a\u200a\u3000\u200a\u2008\u2008\u2008:rocket:\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000.\u3000\u3000\u3000', 
			'\u2008\u3000\u3000\u2002\u2002\u2002\u2002\u3000\u3000\u3000\u3000\u3000\u2008\u3000\u3000\u3000\u3000\u3000.\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000.\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000*', 
			'\u3000\u3000 \u2002\u2002\u3000\u3000\u3000\u3000\u3000 ✦ \u3000\u3000\u3000\u3000\u3000\u3000\u3000\u200a\u200a\u200a\u200a\u200a\u200a\u200a\u200a\u200a\u3000\u2008\u2008\u2008\u2008\u2008\u2008\u2008\u2008\u3000\u3000\u3000\u3000', 
			'\u3000\u3000\u2008\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u2008\u3000\u3000\u3000\u3000\u3000.\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000.\u3000\u3000\u3000\u3000\u3000\u2002\u2002\u2002\u2002\u3000\u3000.', 
			'\u3000\u2008\u3000\u3000\u3000\u3000\u3000.\u3000\u3000\u3000\u3000 \u3000\u3000\u3000\u3000\u3000\u200a\u200a\u200a\u3000\u3000\u3000\u3000\u3000.\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000.\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u2002\u2002 \u3000', 
			'', '\u3000˚\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000ﾟ\u3000\u3000\u3000\u3000\u3000.\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000.', 
			'\u3000\u3000\u2008\u3000', '\u200d \u200d \u200d \u200d \u200d \u200d \u200d \u200d \u200d \u200d ,\u3000 \u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000*', 
			'.\u3000\u3000\u3000\u3000\u3000\u2008\u3000\u3000\u3000\u3000:full_moon: \u3000\u3000\u3000\u3000\u3000\u3000\u3000:earth_americas: \u3000\u3000\u3000.\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000 ✦ \u3000\u3000\u3000\u3000\u2002\u2002 \u3000', 
			'\u3000\u3000\u3000˚\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000*\u3000\u3000\u3000\u3000\u3000\u3000\u2008', 
			'\u2008\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000.\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000.', 
			'\u3000\u3000\u2008\u3000\u3000\u3000\u3000\u3000\u3000\u3000 ✦ \u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000 \u3000 \u200d \u200d \u200d \u200d \u3000\u3000\u3000\u3000 \u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000,', '']), ephemeral=True)

#-----Run-----
def setup(bot):
	bot.add_cog(nightsky(bot))