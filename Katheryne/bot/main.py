import discord
import nest_asyncio
import datetime
import youtube_dl
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio

nest_asyncio.apply()

client = commands.Bot(command_prefix = '.')

import ctypes
import ctypes.util
 
print("ctypes - Find opus:")
a = ctypes.util.find_library('opus')
print(a)
 
print("Discord - Load Opus:")
b = discord.opus.load_opus(a)
print(b)
 
print("Discord - Is loaded:")
c = discord.opus.is_loaded()
print(c)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
    
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    
@client.command()
async def hello(ctx):
    await ctx.send('Ad Astra Abyssosque!')

@client.command()
async def hutao(ctx, amount=5):
    embedVar = discord.Embed(description='"Hu Tao is the 77th Director of the Wangsheng Funeral Parlor, a person vital to managing Liyue\'s funerary affairs. She does her utmost to flawlessly carry out a person\'s last rites and preserve the world\'s balance of yin and yang. Aside from this, she is also a talented poet whose many "masterpieces" have passed around Liyue\'s populace by word of mouth."', timestamp=datetime.datetime.utcnow(), color=0xB75E40)
    embedVar.set_author(name='Hu Tao',url='https://genshin.honeyhunterworld.com/db/char/hutao/?lang=EN',icon_url='https://cdn2.steamgriddb.com/file/sgdb-cdn/logo_thumb/62e81b7815b24e46b69fcfa197aea837.png')
    embedVar.set_image(url='https://genshin.honeyhunterworld.com/img/char/hutao.png')
    #embedVar.add_field(name="test", value="https://genshin.honeyhunterworld.com/img/cardicon/i_7055_party_70.png", inline=True)
    #embedVar.add_field(name="Field2", value="hi2", inline=False)
    embedVar.set_thumbnail(url="https://genshin.honeyhunterworld.com/img/cardicon/i_7055.png")
    embedVar.set_footer(text='\u200b',icon_url="https://genshin.honeyhunterworld.com/img/icons/element/pyro_35.png")
    await ctx.send(embed=embedVar)
    
@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info('https://www.youtube.com/watch?v=ldBgmGlqEug&ab_channel=RaiRye', download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL))
        voice.is_playing()
    
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

# command to play sound from a youtube URL
@client.command()
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL))
        voice.is_playing()
        await ctx.send('Katheryne is playing~. Queue feature not yet implemented ehe~')

# check if the bot is already playing
    else:
        await ctx.send("Error. Katheryne is already playing~")
        return

client.run('token')