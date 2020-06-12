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
    raika = random.randint(1,4)
    me = message.content.startswith
    # 「おはよう」で始まるか調べ
    if me == "おはよう" or "おは":
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送りま
            await message.channel.send(m)

    elif me == "はやおき" or "早起き":
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "早起きですね" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m) 

    elif me == "RRR":
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "RRRRRRRR"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)
    elif me == "ゲームランダム" or "ランダム":       
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            if raika == 1:
                r = "ヴァロラント"
            elif raika == 2:
                r = "オーバーウォッチ"
            elif raika == 3:
                r = "シージ"
            elif raika == 4:
                r = "lol"
        
            m = r
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)

            youbi = ["月","火","水","木","金","土","日"]
            ima = datetime.datetime.now()
            week = ima.weekday()
            kyou = youbi[week]
        
    elif me == "曜日":

        if client.user != message.author:
             
             m = kyou
             await message.channel.send(m)

client.run("NzE4MzM4MDg1MjUwNzkzNTAy.Xt85dA.a_rePmYZFOUwqlA3ONAFNgnsQnA")