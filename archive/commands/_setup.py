import discord
from discord.ext import commands

class Setup(commands.Cog, ):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    def Prefix(self, ctx):
        pass

def setup(bot):
    bot.add_cog(Setup(bot))