import discord
from discord.ext import commands
import datetime
import time
import sys
import asyncio
import os
from cogs.utils import launcher
import json
import logging
import random
from cogs.utils.paginator import Pages
import io
import textwrap
import traceback
from contextlib import redirect_stdout

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


##launcher.check()
 
if 'TOKEN' in os.environ:
    heroku = True
    TOKEN = os.environ['TOKEN']
 
info = launcher.bot()
owner = '300396755193954306'



startup_extensions = [
 
 
    'cogs.mod',
    'cogs.misc',
    'cogs.util',
    'cogs.info',
    'cogs.fun'
    
 
 
]

Client = discord.Client()
description = ('Bot made with discord.py by -= shadeyg56 =-#1702. '
'Made by shadeyg56 \n')


async def get_pre(bot, message):
    with open('cogs/utils/t_config.json') as f:
        config = json.loads(f.read())
    try:
        if message.server.id not in config:
            return 'd.'
    except:
        pass
    else:
        return config[message.server.id]['prefix']

bot = commands.Bot(description=description, command_prefix='d.', pm_help=None)
bot.remove_command('help')

@bot.event
async def on_ready():
    print('------------------------------------')
    print('THE BOT IS ONLINE')
    print('------------------------------------')
    print("Name: {}".format(bot.user.name))
    print('Author: shadeyg56')
    print("ID: {}".format(bot.user.id))
    print('DV: {}'.format(discord.__version__))
    bot.uptime = datetime.datetime.now()
    embed=discord.Embed(title='Good Morning', description='Up and at em', color=0xed)   
    embed.set_footer(text='Darkness ready for use')
    server = len(bot.servers)
    channel = bot.get_channel('356599668739670049')
    users = sum(1 for _ in bot.get_all_members())
    await bot.send_message(channel, embed=embed)
    while 1 == 1:
        await bot.change_presence(game=discord.Game(name='with {} servers'.format(server)))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name='with {} users'.format(users)))
        await asyncio.sleep(10)                         
        await bot.change_presence(game=discord.Game(name='PREFIX = d.'))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name='Currently WIP | Darkness'))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name='d.support | d.invite'))
        await asyncio.sleep(25)
    
                            
    


@bot.command(pass_context=True)
async def help(ctx):
    try:
        await bot.delete_message(ctx.message)
    except:
        pass

    msg = open('cogs/utils/help.txt').read().replace('\\u200b','\u200b').splitlines()
    for i, line in enumerate(msg): 
        if line.strip().startswith('.'):
            x = line.strip().strip('.')
            x = ctx.prefix + x
            msg[i] = '`' + x + '`'
    try:
        p = Pages(bot, message=ctx.message, entries=msg)
        p.embed.set_author(name='Help - Darkness Commands', icon_url=bot.user.avatar_url)
        p.embed.color = 0x00FFFF
        await p.paginate()
    except:
        embed = discord.Embed(title='Darkness Commands', color=0xed)
        embed.add_field(name='Moderation:', value='kick, ban, unban, softban, warn, purge')
        embed.add_field(name='Information:', value='info, serverinfo, userinfo, avatar')
        embed.add_field(name='Miscellaneous:', value='ping, suggest, invite, support')
        embed.add_field(name='Utilities:', value='calc, remind, addrole, removerole')
        embed.add_field(name='Fun:', value='8ball, cat')
        embed.set_footer(text='Bot Dev: -= shadeyg56 =-#1702')
        await bot.say(embed=embed)
    

def owner_only():
    return commands.check(lambda ctx: ctx.message.author == ctx.message.server.owner)

def is_owner():
    return commands.check(lambda ctx: ctx.message.author.id == owner)


@bot.event
async def on_member_join(member):
   darkness = bot.get_channel('356599668739670049')
   if member.server.id == '356599668739670048':
       await bot.send_message(darkness, 'Welcome {0.mention} to {}. Please read #info-and-rules and enjoy your stay. Do d.help to check out the bot'.format(member, server))
   kats = bot.get_channel('313863292126756864')
   if member.server.id == '294262760752152576':
       await bot.send_message(kats, '{0.mention} Welcome to **Dragons and Kats**! Have a great time here and enjoy yourselves!!!:wink: !'.format(member))
   else:
        print('Member joined {}, but message not sent'.format(member.server))


@bot.event
async def on_command(command, ctx):
    if str(command) == 'eval':
        return
    print('------------------------------------')
    print('Command > {}{} < invoked with > {} <\nServer: {} | {}\nUser: {} | {}'
        .format(ctx.prefix,
            command,
            ctx.invoked_with,
            ctx.message.server.name, 
            ctx.message.server.id, 
            ctx.message.author.name, 
            ctx.message.author.id))

@bot.event
async def on_member_remove(member):
    server = member.server
    with open('cogs/utils/t_config.json') as f:
        data = json.loads(f.read())
    status = data[server.id]["leave"]["status"]
    if status:
        msg = data[server.id]["leave"]["msg"]
        channel = data[server.id]['leave']['channel']
        if channel == 'default':
            channel = server
        else:
            channel = discord.utils.get(server.channels, id=channel)

        await bot.send_message(channel, msg.format(member, server))

@bot.event
async def on_server_join(server):
    embed = discord.Embed(title='Darkness Info', color=0xed)
    owner = server.owner
    servers = len(bot.servers)                    
    embed.add_field(name='Author', value='<@300396755193954306>')
    embed.add_field(name='Servers', value=servers)    
    embed.add_field(name='Prefix', value='d.')
    embed.set_footer(text='Powered by discord.py')
    embed.set_thumbnail(url='http://data.whicdn.com/images/150102219/large.gif')
    embed.add_field(name='Invite', value='https://discordapp.com/oauth2/authorize?client_id=355189919410421760&scope=bot&permissions=66186303')
    embed.add_field(name='Support', value='https://discord.gg/Jjdp8hf')
    embed.add_field(name='GitHub', value='https://github.com/shadeyg56/darkness')
    await bot.send_message(owner, embed=embed)
        
def fmt_help(page):
    cmd = ''
    for line in page.splitlines():
        if line.startswith('.'):
            cmd = line.strip('.')
            break
    em = discord.Embed(color=0x00FFFF)
    em.set_author(name='Help - {}'.format(cmd))

async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        pages = bot.formatter.format_help_for(ctx, ctx.invoked_subcommand)
        for page in pages:
            # page = page.strip('```css').strip('```')


            await bot.send_message(ctx.message.channel, page)
        print('Sent command help')
    else:
        pages = bot.formatter.format_help_for(ctx, ctx.command)
        for page in pages:
            await bot.send_message(ctx.message.channel, page)
        print('Sent command help')

@bot.event
async def on_command_error(error, ctx):
   print(error)
   channel = ctx.message.channel
   if isinstance(error, commands.MissingRequiredArgument):
       await send_cmd_help(ctx)
       print('Sent command help')
   elif isinstance(error, commands.BadArgument):
       await send_cmd_help(ctx)
       print('Sent command help')
   elif isinstance(error, commands.DisabledCommand):
       await bot.send_message(channel, "That command is disabled.")
       print('Command disabled.')
   elif isinstance(error, commands.CommandInvokeError):
       # A bit hacky, couldn't find a better way
       no_dms = "Cannot send messages to this user"
       is_help_cmd = ctx.command.qualified_name == "help"
       is_forbidden = isinstance(error.original, discord.Forbidden)
       if is_help_cmd and is_forbidden and error.original.text == no_dms:
           msg = ("I couldn't send the help message to you in DM. Either"
                  " you blocked me or you disabled DMs in this server.")
           await bot.send_message(channel, msg)
           return

@bot.command(pass_context=True,name='cog')
@owner_only()
async def _reload(ctx,*, module : str):
    """Reloads a module."""
    channel = ctx.message.channel
    module = 'cogs.'+module
    try:
        bot.unload_extension(module)
        x = await bot.send_message(channel,'Successfully Unloaded.')
        bot.load_extension(module)
        x = await bot.edit_message(x,'Successfully Reloaded.')
    except Exception as e:
        x = await bot.edit_message(x,'\N{PISTOL}')
        await bot.say('{}: {}'.format(type(e).__name__, e))
    else:
        x = await bot.edit_message(x,'Done. \N{OK HAND SIGN}')

@bot.command(name='presence')
async def _set(Type=None,*,thing=None):
    """Change the bot's discord game/stream!"""
    server = len(bot.servers)
    if Type is None:
            await bot.say('Usage: `.presence [game/stream] [message]`')
    else:
        if Type.lower() == 'stream':
            await bot.change_presence(game=discord.Game(name=thing,type=1,url='https://www.twitch.tv/a'),status='online')
            await bot.say('Set presence to. `Streaming {}`'.format(thing))
        elif Type.lower() == 'game':
            await bot.change_presence(game=discord.Game(name=thing))
            await bot.say('Set presence to `Playing {}`'.format(thing))
        elif Type.lower() == 'clear':
            await bot.change_presence(game=None)
            await bot.say('Cleared Presence')
        elif Type.lower() == 'servers':
            await bot.change_presence(game=discord.Game(name='with {} servers'.format(server)))
            await bot.say('**Im now playing with {} servers.**'.format(server))
        else:
            await bot.say('Usage: `.presence [game/stream] [message]`')
        

@bot.command(pass_context=True)
@is_owner()
async def _leave_all_servers_(ctx):
    for server in bot.servers:
        await bot.leave_server(server)
        await bot.say('I left `{}`'.format(server.name))

@bot.command(pass_context=True)
async def servers(ctx):
    servers = ', '.join([i.name for i in bot.servers]).strip(', ')
    await bot.say('**Current list of servers:**\n ```bf\n{}```'.format(servers))

@bot.command(pass_context=True)
@is_owner()
async def _leave_server(ctx, server):
    to_leave = discord.utils.get(bot.servers, id=str(server))
    try:
        await bot.leave_server(to_leave)
    except:
        await self.bot.say('Failed.')
    else:
        await self.bot.say('Successfully left {}'.format(to_leave.name))

@bot.command(pass_context=True)
async def register(ctx):
    server = ctx.message.server
    channel = discord.utils.get(server.channels, name='server-event')
    user = ctx.message.author
    with open('cogs/utils/registrations.txt') as f:
        data = f.read()
        print(data )

    if ctx.message.channel != channel:
        await bot.say('You can only register in {}'.format(channel.mention))
        return
    
    if str(user) in data:
        await bot.delete_message(ctx.message)
        await bot.send_message(user, "You can't register more than once.")
        return
    with open('cogs/utils/registrations.txt','a') as f:
        f.write(str(user)+'\n')
    role = discord.utils.get(server.roles, name='4row')
    await bot.add_roles(user, role)
    await bot.add_reaction(ctx.message, '\u2705')
   
@bot.command(pass_context = True)
@is_owner()
async def shutdown(ctx):
    timestamp = ctx.message.timestamp                         
    embed=discord.Embed(title='Good Night', description='See you tomorrow', color=0xed, timestamp=timestamp)
    embed.set_footer(text='Darkness no longer online')
    await bot.say(embed=embed)
    await bot.logout()
 
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            print('Loaded: {}'.format(extension))
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Error on load: {}\n{}'.format(extension, exc))
           
def cleanup_code( content):
    """Automatically removes code blocks from the code."""
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    # remove `foo`
    return content.strip('` \n')        
           
def get_syntax_error(e):
    if e.text is None:
        return '```py\n{0.__class__.__name__}: {0}\n```'.format(e)
    return '```py\n{0.text}{1:>{0.offset}}\n{2}: {0}```'.format(e, '^', type(e).__name__)

async def to_code_block(ctx, body):
    if body.startswith('```') and body.endswith('```'):
        content = '\n'.join(body.split('\n')[1:-1])
    else:
        content = body.strip('`')
    await bot.edit_message(ctx.message, '```py\n'+content+'```')
           
           
@bot.command(pass_context=True, name='eval')
@is_owner()
async def _eval(ctx, *, body: str):
    '''Run python scripts on discord!'''
    env = {
        'bot': bot,
        'ctx': ctx,
        'channel': ctx.message.channel,
        'author': ctx.message.author,
        'server': ctx.message.server,
        'message': ctx.message,
    }

    env.update(globals())

    body = cleanup_code(content=body)
    stdout = io.StringIO()

    to_compile = 'async def func():\n%s' % textwrap.indent(body, '  ')
    try:
        exec(to_compile, env)
    except SyntaxError as e:
        return await bot.say(get_syntax_error(e))

    func = env['func']
    try:
        with redirect_stdout(stdout):
            ret = await func()
    except Exception as e:
        value = stdout.getvalue()
        x = await bot.say('```py\n{}{}\n```'.format(value, traceback.format_exc()))
        try:
            await bot.add_reaction(x, '\U0001f534')
        except:
            pass
    else:
        value = stdout.getvalue()
        
        if TOKEN in value:
            value = value.replace(TOKEN,"[EXPUNGED]")
            
        if ret is None:
            if value:
                try:
                    x = await bot.say('```py\n%s\n```' % value)
                except:
                    x = await bot.say('```py\n\'Result was too long.\'```')
                try:
                    await bot.add_reaction(x, '\U0001f535')
                except:
                    pass
            else:
                try:
                    await bot.add_reaction(ctx.message, '\U0001f535')
                except:
                    pass
        else:
            try:
                x = await bot.say('```py\n%s%s\n```' % (value, ret))
            except:
                x = await bot.say('```py\n\'Result was too long.\'```')
            try:
                await bot.add_reaction(x, '\U0001f535')
            except:
                pass

@bot.command(pass_context = True)
async def devcontact(ctx, *, msg: str):
    dev = '@-= shadeyg56™ =-#1702'
    user = ctx.message.author
    await bot.send_message(dev, '{} sent the following message: {}'.format(user, msg))
    await bot.say('Your message has been sent. It will be checked by the dev asap. If your message was a troll or you keep resending/spamming a message you will be blacklisted from the command')
    await bot.delete_message(ctx.message)
                           
@bot.command(pass_context = True)
async def dm(ctx, user: discord.Member, *, msg: str):
    if ctx.message.author.id == '300396755193954306':
        await bot.send_message(user, '{}'.format(msg))
        await bot.delete_message(ctx.message)
    else:
         message = await bot.say('Only the bot dev can use this command')
         await asyncio.sleep(5)
         await bot.delete_message(message)
         await bot.delete_message(ctx.message)
         
@bot.command(pass_context=True)
@is_owner()
async def blacklist(ctx, user_id: str):
    with open('cogs/utils/blacklists.json') as f:
        data = json.loads(f.read())
        data = data[user_id] = "blacklisted"
        data = json.dumps(data, indent=4, sort_keys=True)
    with open('cogs/utils/blacklists.json', 'w') as f:
        f.write(data)
        await bot.say('Succesfully blacklisted id {}'.format(user_id))
        
    

             
             
@asyncio.coroutine
async def on_message(message):
    channel = bot.get_channel('356602525740433408')
    if message.channel.id == '356602525740433408':
        await bot.send_message(channel, 'test')
        await bot.process_commands(message)
   




   
bot.run(TOKEN)
