import discord
client = discord.Client()
@client.event
async def on_ready():
    print('Client is ready')
@client.event
async def on_message(message):
    if message.author.bot == False:
      if 'my ' in message.content:
        sovietmsg = message.content.replace('my ', '*our* ').replace(
            'My ', '*Our*').replace('I ', '*we* ').replace('i ', '*we* ').replace(
                'mine', '*ours*')
        await message.channel.send(sovietmsg)
      elif 'I ' in message.content:
        sovietmsg = message.content.replace('my ', '*our* ').replace(
            'My ', '*Our* ').replace('I ', '*we* ').replace('i ', '*we* ').replace(
                'mine', '*ours*')
        await message.channel.send(sovietmsg)
      elif 'mine' in message.content:
        sovietmsg = message.content.replace('my ', '*our* ').replace(
            'My ', '*Our* ').replace('I ', '*we *').replace('i ', '*we* ').replace(
                'mine', '*ours*')
        await message.channel.send(sovietmsg)


client.run('NjQ2NTY2NDMwOTgwMDQ2ODQ4.XdVL1w.nYP42XNj0vUnb1uBceBnM1kh0j0')