import discord
import datetime
import os

client = discord.Client()

@client.event
async def on_ready():
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드 봇 이름 : " +client.user.name)
    print("디스코드 봇 ID" +str(client.user.id))
    print("디스코드봇 버전 : " + str(discord.__version__))
    print('------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("준민이 뺨때리기"))

@client.event
async def on_message(message):
    content = message.content
    
    if content.startswith("!준민이 뺨따구 때리기"):
        await message.channel.send("짝짝짝짝짝짝짝짝짝짝짝짝짝짝")

    if content.startswith("!자기소개"):
        embed=discord.Embed(description="응애 나는야 IT소프트웨어과 1-9 반디코 도우미 봇", color=0x00ff56)
        embed.set_author(name="응애 나 아기 디코봇")
        await message.channel.send(embed=embed)

    if content.startswith("!인백이의 드립은"):
        await message.channel.send("개노잼입니다")

    if content.startswith("!시간표"):
        embed=discord.Embed(title=" ", description=" ", color=0x00ff56)
        embed.set_author(name="```수원정보과학고등학교 1학년 9반 시간표```", url="https://cdn.discordapp.com/attachments/832047766817210388/832047839440928818/unknown_5.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/832047766817210388/832047839440928818/unknown_5.png")
        await message.channel.send(embed=embed)

    if content.startswith("!월시간표"):
        embed=discord.Embed(description="<1교시>\n프로그래밍\n\n<2교시>\n프로그래밍\n\n<3교시>\n프로그래밍\n\n<4교시>\n프로그래밍\n\n<5교시>\n체육\n\n<6교시>\n사회\n이용각선생님", color=0x00ff56)
        embed.set_author(name="1-9 월요일 시간표", url="https://cdn.discordapp.com/attachments/832047766817210388/832047839440928818/unknown_5.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/832047766817210388/832047839440928818/unknown_5.png")
        await message.channel.send(embed=embed)
    
    if content.startswith("!화시간표"):
        embed=discord.Embed(description="<1교시>\n사회\n이진경선생님\n\n<2교시>\n컴퓨터일반\n\n<3교시>\n컴퓨터일반\n\n<4교시>\n과학\n\n<5교시>\n진로\n\n<6교시>\n수학\n\n<7교시>\n영어", color=0x00ff56)
        embed.set_author(name="1-9 월요일 시간표", url="https://cdn.discordapp.com/attachments/832047766817210388/832047839440928818/unknown_5.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/832047766817210388/832047839440928818/unknown_5.png")
        await message.channel.send(embed=embed)

    if content.startswith("!수시간표"):
        embed=discord.Embed(description="<1교시>\n체육\n\n<2교시>\n음악\n\n<3교시>\n국어\n\n<4교시>\n과학\n\n<5교시>\n영어\n\n<6교시>\n수학\n\n<7교시>\n사회\n이진경선생님", color=0x00ff56)
        embed.set_author(name="1-9 월요일 시간표", url="https://cdn.discordapp.com/attachments/832047766817210388/832047839440928818/unknown_5.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/832047766817210388/832047839440928818/unknown_5.png")
        await message.channel.send(embed=embed)

    if content.startswith("!목시간표"):
        embed=discord.Embed(description="<1교시>\n음악\n\n<2교시>\n프로그래밍\n\n<3교시>\n프로그래밍\n\n<4교시>\n영어\n\n<5교시>\n국어\n\n<6교시>\n수학\n\n<7교시>\n사회\n이용각선생님", color=0x00ff56)
        embed.set_author(name="1-9 월요일 시간표", url="https://cdn.discordapp.com/attachments/832047766817210388/832047839440928818/unknown_5.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/832047766817210388/832047839440928818/unknown_5.png")
        await message.channel.send(embed=embed)

    if content.startswith("!금시간표"):
        embed=discord.Embed(description="<1교시>\n미술\n\n<2교시>\n미술\n\n<3교시>\n처리\n\n<4교시>\n처리\n\n<5교시>\n융합\n\n<6교시>\n창체", color=0x00ff56)
        embed.set_author(name="1-9 월요일 시간표", url="https://cdn.discordapp.com/attachments/832047766817210388/832047839440928818/unknown_5.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/832047766817210388/832047839440928818/unknown_5.png")
        await message.channel.send(embed=embed)

    if(message.content == "!시간"):
        await message.channel.send(embed=discord.Embed(title="Time", timestamp=datetime.datetime.utcnow()))
        
    if content.startswith("!=명령어"):
        embed.set_author(name="")
        embed.set_author(name="!준민이 뺨따꾸 때리기\n!인백이의 드립은\n!자기소개\n!시간\n!시간표\n!월시간표\n!화시간표\n!수시간표\n!목시간표\n!금시간표")
        await message.channel.send(embed=embed)

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
