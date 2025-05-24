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
        embed = discord.Embed(
            title="¡Bot de Crafteos Activo!",
            description="Usa ?crafteos para ver la lista de crafteos disponibles",
            color=discord.Color.green()
        )
        await canal.send(embed=embed)
    else:
        print("No se encontró el canal. Verifica el ID.")


def enviar_imagen(nombre_archivo):
    ruta = f"Crafteos/{nombre_archivo}.png"
    if os.path.exists(ruta):
        return discord.File(ruta)
    else:
        return None


async def enviar_respuesta(ctx, nombre_archivo, nombre_objeto):
    archivo = enviar_imagen(nombre_archivo)
    embed = discord.Embed(
        title=nombre_objeto,
        description="Crafteo en Minecraft",
        color=discord.Color.green()
    )
    if archivo:
        embed.set_image(url="attachment://"+nombre_archivo+".png")
        await ctx.send(embed=embed, file=archivo)
    else:
        embed.description = f"No se encontró la imagen de {nombre_objeto}"
        embed.color = discord.Color.red()
        await ctx.send(embed=embed)


@bot.command(name="crafteos")
async def lista_crafteos(ctx):
    embed = discord.Embed(
        title="📋 Lista de Crafteos Disponibles",
        description="Usa ? seguido del nombre del crafteo para ver su receta",
        color=discord.Color.blue()
    )
    
    crafteos_texto = ""
    for comando in COMANDOS_DISPONIBLES:
        crafteos_texto += f"• {comando}\n"
    
    embed.add_field(name="Crafteos:", value=crafteos_texto)
    embed.set_footer(text="Ejemplo: ?Tocadiscos")
    await ctx.send(embed=embed)


@bot.command()
async def Tocadiscos(ctx):
    await enviar_respuesta(ctx, "tocadiscos", "Tocadiscos")


@bot.command()
async def BloqueMusical(ctx):
    await enviar_respuesta(ctx, "Bloque musical", "Bloque Musical")


@bot.command()
async def MesaDeEncantamientos(ctx):
    await enviar_respuesta(ctx, "MesaDeEncantamientos", "Mesa De Encantamientos")


@bot.command()
async def CofreDeEnder(ctx):
    await enviar_respuesta(ctx, "CofreDeEnder", "Cofre De Ender")


@bot.command()
async def VaraDelEnd(ctx):
    await enviar_respuesta(ctx, "VaraDelEnd", "Vara Del End")


@bot.command()
async def Fogata(ctx):
    await enviar_respuesta(ctx, "Fogata", "Fogata")


@bot.command()
async def Afiladora(ctx):
    await enviar_respuesta(ctx, "Afiladora", "Afiladora")


@bot.command()
async def CortaPiedras(ctx):
    await enviar_respuesta(ctx, "CortaPiedras", "Corta Piedras")


@bot.command()
async def AltoHorno(ctx):
    await enviar_respuesta(ctx, "AltoHorno", "Alto Horno")


@bot.command()
async def Ahumador(ctx):
    await enviar_respuesta(ctx, "Ahumador", "Ahumador")


@bot.command()
async def Andamio(ctx):
    await enviar_respuesta(ctx, "Andamio", "Andamio")


@bot.command()
async def Nexo(ctx):
    await enviar_respuesta(ctx, "Nexo", "Nexo")


@bot.command()
async def LamparaDeRedstone(ctx):
    await enviar_respuesta(ctx, "LamparaDeRedstone", "Lampara De Redstone")


@bot.command()
async def Observador(ctx):
    await enviar_respuesta(ctx, "Observador", "Observador")


@bot.command()
async def Repetidor(ctx):
    await enviar_respuesta(ctx, "Repetidor", "Repetidor")


@bot.command()
async def Marco(ctx):
    await enviar_respuesta(ctx, "Marco", "Marco")


@bot.command()
async def SoporteParaArmaduras(ctx):
    await enviar_respuesta(ctx, "SoporteParaArmaduras", "Soporte Para Armaduras")


bot.run("TOKEN")