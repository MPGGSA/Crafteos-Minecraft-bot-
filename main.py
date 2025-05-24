import discord
from discord.ext import commands
import os


intents = discord.Intents.default()
intents.message_content = True  # Agrega esta línea
bot = commands.Bot(command_prefix="?", intents=intents)

# Lista de comandos disponibles
COMANDOS_DISPONIBLES = [
    "Tocadiscos",
    "BloqueMusical",
    "MesaDeEncantamientos",
    "CofreDeEnder",
    "VaraDelEnd",
    "Fogata",
    "Afiladora",
    "CortaPiedras",
    "AltoHorno",
    "Ahumador",
    "Andamio",
    "Nexo",
    "LamparaDeRedstone",
    "Obserbador",
    "Repetidor",
    "Marco",
    "SoporteParaArmaduras"
]


@bot.event
async def on_ready():
    print("Bot conectado correctamente")
    canal = bot.get_channel(1373428257688522797)
    if canal:
        await canal.send('Usa ? antes de cada comando')
        await canal.send("Comandos disponibles:")
        for comando in COMANDOS_DISPONIBLES:
            await canal.send(f"- {comando}")
    else:
        print("No se encontró el canal. Verifica el ID.")


def enviar_imagen(nombre_archivo):
    ruta = f"Crafteos/{nombre_archivo}.png"
    if os.path.exists(ruta):
        return discord.File(ruta)
    else:
        return None


@bot.command()
async def Tocadiscos(ctx):
    archivo = enviar_imagen("tocadiscos")
    if archivo:
        await ctx.send(file=archivo)
    else:
        await ctx.send("No se encontró la imagen de Tocadiscos.")


@bot.command()
async def BloqueMusical(ctx):
    archivo = enviar_imagen("Bloque musical")
    if archivo:
        await ctx.send(file=archivo)
    else:
        await ctx.send("No se encontró la imagen de Bloque Musical.")


@bot.command()
async def MesaDeEncantamientos(ctx):
    archivo = enviar_imagen("MesaDeEncantamientos")
    if archivo:
        await ctx.send(file=archivo)
    else:
        await ctx.send("No se encontró la imagen de Mesa De Encantamientos.")


@bot.command()
async def CofreDeEnder(ctx):
    archivo = enviar_imagen("CofreDeEnder")
    if archivo:
        await ctx.send(file=archivo)
    else:
        await ctx.send("No se encontró la imagen de Cofre De Ender.")


@bot.command()
async def VaraDelEnd(ctx):
    archivo = enviar_imagen("VaraDelEnd")
    if archivo:
        await ctx.send(file=archivo)
    else:
        await ctx.send("No se encontró la imagen de Vara Del End.")


@bot.command()
async def Fogata(ctx):
    archivo = enviar_imagen("Fogata")
    if archivo:
        await ctx.send(file=archivo)
    else:
        await ctx.send("No se encontró la imagen de Fogata.")


@bot.command()
async def Afiladora(ctx):
    archivo = enviar_imagen("Afiladora")
    if archivo:
        await ctx.send(file=archivo)
    else:
        await ctx.send("No se encontró la imagen de Afiladora.")


@bot.command()
async def CortaPiedras(ctx):
    archivo = enviar_imagen("CortaPiedras")
    if archivo:
        await ctx.send(file=archivo)
    else:
        await ctx.send("No se encontró la imagen de Corta Piedras.")


@bot.command()
async def AltoHorno(ctx):
    archivo = enviar_imagen("AltoHorno")
    if archivo:
        await ctx.send(file=archivo)
    else:
        await ctx.send("No se encontró la imagen de Alto Horno.")


@bot.command()
async def Ahumador(ctx):
    archivo = enviar_imagen("Ahumador")
    if archivo:
        await ctx.send(file=archivo)
    else:
        await ctx.send("No se encontró la imagen de Ahumador.")


@bot.command()
async def Andamio(ctx):
    archivo = enviar_imagen("Andamio")
    if archivo:
        await ctx.send(file=archivo)
    else:
        await ctx.send("No se encontró la imagen de Andamio.")


@bot.command()
async def Nexo(ctx):
    archivo = enviar_imagen("Nexo")
    if archivo:
        await ctx.send(file=archivo)
    else:
        await ctx.send("No se encontró la imagen de Nexo.")


@bot.command()
async def LamparaDeRedstone(ctx):
    archivo = enviar_imagen("LamparaDeRedstone")
    if archivo:
        await ctx.send(file=archivo)
    else:
        await ctx.send("No se encontró la imagen de Lampara De Redstone.")


@bot.command()
async def Obserbador(ctx):
    archivo = enviar_imagen("Obserbador")
    if archivo:
        await ctx.send(file=archivo)
    else:
        await ctx.send("No se encontró la imagen de Obserbador.")


@bot.command()
async def Repetidor(ctx):
    archivo = enviar_imagen("Repetidor")
    if archivo:
        await ctx.send(file=archivo)
    else:
        await ctx.send("No se encontró la imagen de Repetidor.")


@bot.command()
async def Marco(ctx):
    archivo = enviar_imagen("Marco")
    if archivo:
        await ctx.send(file=archivo)
    else:
        await ctx.send("No se encontró la imagen de Marco.")


@bot.command()
async def SoporteParaArmaduras(ctx):
    archivo = enviar_imagen("SoporteParaArmaduras")
    if archivo:
        await ctx.send(file=archivo)
    else:
        await ctx.send("No se encontró la imagen de Soporte Para Armaduras.")


bot.run("TOKEN")
