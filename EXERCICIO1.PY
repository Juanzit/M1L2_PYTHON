import discord
import random  

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Você logou como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(f'Olá! eu sou um bot {client.user}!')

    elif message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)

    elif message.content.startswith('$dado'):
        partes = message.content.split()
        
        if len(partes) > 1:
            lados = int(partes[1]) 
        else:
            lados = 6 
            
        numero = random.randint(1, lados)
        await message.channel.send(f'Você rolou um d{lados} e tirou: {numero}')
#Blabla
client.run("insira seu token agui")
