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
    for i in range(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Visual Studio Code "))
        time.sleep(7)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Bot Made By. 원찬,준민"))
        time.sleep(7)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Dev C++"))
        time.sleep(7)

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
        await message.channel.send("개씹노잼입니다")
        
    if content.startswith("!민혁이의 봇은"):
        await message.channel.send("작동 안되죠? 작동 안되죠? 작동 안되죠? 작동 안되죠? 작동 안되죠? 작동 안되죠? 작동 안되죠? 작동 안되죠?`")

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
        
    if content.startswith("!도움말"):
        embed=discord.Embed(description="!준민이 뺨따꾸 때리기\n!인백이의 드립은\n!자기소개\n!시간\n!청소 (청소할 메시지 개수)\n!시간표\n!월시간표\n!화시간표\n!수시간표\n!목시간표\n!금시간표", color=0x00ff56)
        embed.set_author(name="<<명령어>>", url="")
        await message.channel.send(embed=embed)
    
    if message.content.startswith ("!청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님에 의해 삭제 되었습니다".format(amount, message.author), color=0x00ff56)
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))

        if message.content.startswith("!투표"):
            vote = message.content[4:].split("/")
            await message.channel.send("투표 - " + vote[0])
            for i in range(1, len(vote)):
                choose = await message.channel.send("" + vote[i] + "")
                await choose.add_reaction(':check:')
            
access_token = os.environ['BOT_TOKEN']
client.run(access_token)
