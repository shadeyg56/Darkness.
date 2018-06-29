import discord
from discord.ext import commands
import json

class Economy():
	def __init__(self, bot):
		self.bot = bot
		

	@commands.command()
	async def register(self, ctx):
		with open('cogs/utils/economy.json') as f:
			data = json.load(f)
		if str(ctx.author.id) not in data:
			await ctx.send("Thanks for joining the National Darkness Bank. As a welcome gift we have given you 200 Darkness chips <:Darkness:411673568170999808> in this server")
			data[str(ctx.author.id)] = {}
			data[str(ctx.author.id)]["name"] = str(ctx.author)
			data[str(ctx.author.id)]["servers"] = {}
			data[str(ctx.author.id)]["servers"][ctx.guild.name] = {}
			data[str(ctx.author.id)]["servers"][ctx.guild.name]["id"] = ctx.guild.id
			data[str(ctx.author.id)]["servers"][ctx.guild.name]["balance"] = 200
		else:
			await ctx.send("You've already opened an account.")
		data = json.dumps(data, indent=4)
		with open('cogs/utils/economy.json', 'w') as f:
			f.write(data)

	@commands.command()
	async def bal(self, ctx):
		with open('cogs/utils/economy.json') as f:
			data = json.load(f)
		if str(ctx.author.id) in data:
			if ctx.guild.name in data[str(ctx.author.id)]['servers']:
				embed = discord.Embed(title="Balance", description=f"{data[str(ctx.author.id)]['servers'][ctx.guild.name]['balance']} Darkness Chips <:Darkness:411673568170999808>", color=discord.Color.blue())
				await ctx.send(embed=embed)
			else:
				embed = discord.Embed(title="Balance", description=f"0 Darkness Chips <:Darkness:411673568170999808>", color=discord.Color.blue())
				await ctx.send(embed=embed)
		else:
			await ctx.send("You haven't opened an account yet. Repeat this command after doing d.register")


def setup(bot):
	bot.add_cog(Economy(bot))
