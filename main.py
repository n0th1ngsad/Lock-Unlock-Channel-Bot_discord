import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

LOCKED_ROLES = [FIRST ROLE, SECOND ROLE]  # CHANGE TO YOUR ROLE ID, AND YOU CAN ADD AS MANY AS YOU WANT

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.command()
@commands.has_permissions(manage_channels=True)
async def lockc(ctx, channel_id: int):
    channel = client.get_channel(channel_id)
    
    if channel is None:
        await ctx.send("Channel not found.")
        return
    
    for role_id in LOCKED_ROLES:
        role = ctx.guild.get_role(role_id)
        if role is not None:
            await channel.set_permissions(role, send_messages=False)
    
    await ctx.send(f"Channel <#{channel_id}> has been locked.")

client.run('YOUR_TOKEN')
