import discord
import random
import string
from discord.ext import commands
import os
# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"abbiamo fatto l'accesso come {bot.user}")
@bot.command()
async def bidoni(ctx):
    await ctx.send("Carta = Giallo, Plastica = Blu, Vetro = Verde, Indifferenziata = Grigio, Organico = Marrone")
@bot.command()
async def info(ctx):
    info_message = (
        "Comandi disponibili:\n"
        "!bidoni - mostra i colori dei bidoni per la raccolta differenziata (lo sanno tutti pero perche no)\n"
        "!info - mostra questo messaggio informativo (come hai fatto a trovarlo?) >:(\n"
        "!consigli (parametro) - fornisce consigli per ridurre l'inquinamento, bello vero :D (no)\n"
        "!turnoff - spegne il bot (solo admin)\n"
        "!calendario - mostra il calendario della raccolta differenziata\n (solo se sei adulto o hai permesso di andare fuori da solo :)"

    )
    await ctx.send(info_message)
@bot.command()
async def consigli(ctx, parametro: str):
    consigli_dict = {
        "casa": "per ridurre l'inquinamento a casa, puoi spegnere gli apparecchi elettronici quando non li usi e preferire prodotti locali e sostenibili.",
        "scuola": "a scuola, promuovi il riciclo, utilizza materiali didattici digitali per ridurre l'uso della carta e organizza giornate di pulizia dell'ambiente.",
        "lavoro": "al lavoro, riduci gli sprechi di carta e implementa politiche di ufficio verde come il riciclo e l'uso di energie rinnovabili.",
        "carta": "per ridurre l'inquinamento legato alla carta, usa carta riciclata, stampa solo quando necessario e preferisci comunicazioni digitali (pero non giocare a quei giochi stupidi digitali come plants vs. brainrots, per favore).",
        "plastica": "per ridurre l'inquinamento da plastica, utilizza borse riutilizzabili e partecipa a programmi di raccolta differenziata."
    }
    consiglio = consigli_dict.get(parametro.lower(), "mi dispiace, non ho consigli per questo parametro, prova con 'casa', 'scuola' o 'lavoro'.")
    await ctx.send(consiglio)
@bot.command()
async def turnoff(ctx):
    if ctx.author.guild_permissions.administrator:
        await ctx.send("spegnimento del bot perchè l'hai detto tu haha... ciao.")
        await bot.close()
    else:
        await ctx.send("mi dispiace, ma solo gli admin possono spegnere il bot. (ovviamente)")
@bot.command()
async def calendario(ctx):
    with open("bot/calendar/calendar_october.png", 'rb') as f:
        # Memorizziamo il file della libreria di Discord convertito in questa variabile!
        picture = discord.File(f)
    # Possiamo quindi inviare questo file come parametro!
    await ctx.send(file=picture)
    with open("bot/calendar/calendar_november.png", 'rb') as f:
        # Memorizziamo il file della libreria di Discord convertito in questa variabile!
        picture = discord.File(f)
    # Possiamo quindi inviare questo file come parametro!
    await ctx.send(file=picture)
    with open("bot/calendar/calendar_dicember.png", 'rb') as f:
        # Memorizziamo il file della libreria di Discord convertito in questa variabile!
        picture = discord.File(f)
    # Possiamo quindi inviare questo file come parametro!
    await ctx.send(file=picture)
# token: oh cavolo lo stavo per mettere qui :D
bot.run("perche ti darei il token")
# in caso stai vedendo questo su github, scusa ma non ti darei mai accesso al token del bot vero
