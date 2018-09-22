from discord.ext import commands

class SubfolderSampleCog:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def foo(self, ctx):
        '''Sends bar'''
        await ctx.send('bar')

def setup(bot):
    bot.add_cog(SubfolderSampleCog(bot))