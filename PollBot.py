import discord
from discord import app_commands
import settings

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id = settings.GUILD))
            self.synced = True
        print(f"Connecté en tant que {self.user}\n")
        print(f"discord.py {discord.__version__}\n")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(guild = discord.Object(id=settings.GUILD), name="source", description="check mon code")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message("mon papa c'est s0ca et voila son boulot https://github.com/s0ca")

@tree.command(guild = discord.Object(id=settings.GUILD), name="ping", description="pong!")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"pong!")

@tree.command(guild = discord.Object(id=settings.GUILD),name="purge",description="la grande purge messagère")
async def purge(interaction: discord.Interaction, nbr: int= 1 ):
    if interaction.user.id == settings.OWNER:
        #await interaction.channel.purge(limit=nbr)
        await interaction.response.send_message(f"T'as buté {nbr} messages, je suis fier de toi", ephemeral=True)
        await interaction.channel.purge(limit=nbr)
    else:
        await interaction.response.send_message("Wow t'as cru que t'avais le droit de faire ça?! Bouge de la enfoiré de traitre!", ephemeral=True)

@tree.command(guild=discord.Object(id=settings.GUILD), name="poll", description="Sondage rapide")
async def poll(interaction: discord.Interaction, question: str):
    poll_message = await interaction.channel.send(f"**Sondage :** {question}")
    reac1 = "👍"
    reac2 = "👎"
    reac3 = "🤷"
    await poll_message.add_reaction(reac1)
    await poll_message.add_reaction(reac2)
    await poll_message.add_reaction(reac3)
    await interaction.response.send_message("Sondage créé avec succès!", ephemeral=True)


client.run(settings.TOKEN)
