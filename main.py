import discord
import random
import datetime
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content in ["おはよう","おはようございます"]:
        await message.channel.send('おはようございます' + message.author.name + "さん！")
    elif message.content in ["はやおき","早起き"]:
        await message.channel.send('早起きですね' + message.author.name + "さん！")
    elif message.content in ["ゲームランダム","ランダム"]:
        game = random.randint(1, 4)
        if game == 1:
            await message.channel.send('ヴァロラント')
        elif game == 2:
            await message.channel.send('オーバーウォッチ')
        elif game == 3:
            await message.channel.send('シージ')
        elif game == 4:
            await message.channel.send('LOL')

            
client.run("NzE4MzM4MDg1MjUwNzkzNTAy.Xt85dA.a_rePmYZFOUwqlA3ONAFNgnsQnA")