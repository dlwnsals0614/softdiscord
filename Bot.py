import discord
import datetime
import os
import time
import pytz
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드 봇 이름 : " +client.user.name)
    print("디스코드 봇 ID" +str(client.user.id))
    print("디스코드봇 버전 : " + str(discord.__version__))
    print('------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Visual Studio Code "))

@client.event
async def on_message(message):
    content = message.content
    
    if content.startswith("!준민이 뺨따구 때리기"):
        await message.channel.send("짝짝짝짝짝짝짝짝짝짝짝짝짝짝")
        
    if content.startswith("!시발오류"):
        await message.channel.send("ㅈ같네")

    if content.startswith("!자기소개"):
        embed=discord.Embed(description="응애 나는야 IT소프트웨어과 1-9 반디코 도우미 봇", color=0x00ff56)
        embed.set_author(name="응애 나 아기 디코봇")
        await message.channel.send(embed=embed)

    if content.startswith("!인백이의 드립은"):
        await message.channel.send("개씹노잼입니다")
        
    if content.startswith("!인백이는"):
        await message.channel.send("난쟁이입니다")
        
    if content.startswith("!민혁이의 봇은"):
        await message.channel.send("작동 안되죠? 작동 안되죠? 작동 안되죠? 작동 안되죠? 작동 안되죠? 작동 안되죠? 작동 안되죠? 작동 안되죠?`")

    if content.startswith("!시간표"):
        embed=discord.Embed(title=" ", description=" ", color=0x00ff56)
        embed.set_author(name="```수원정보과학고등학교 1학년 9반 시간표```", url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        await message.channel.send(embed=embed)

    if content.startswith("!월시간표"):
        embed=discord.Embed(description="<1교시>\n프로\n\n<2교시>\n프로\n\n<3교시>\n프로\n\n<4교시>\n프로\n\n<5교시>\n수학\n\n<6교시>\n사회\n이용각선생님", color=0x00ff56)
        embed.set_author(name="1-9 월요일 시간표", url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        await message.channel.send(embed=embed)
    
    if content.startswith("!화시간표"):
        embed=discord.Embed(description="<1교시>\n체육\n\n<2교시>\n컴일\n\n<3교시>\n컴일\n\n<4교시>\n영어\n\n<5교시>\n수학\n\n<6교시>\n음악<7교시>\n사회\n이진경선생님", color=0x00ff56)
        embed.set_author(name="1-9 월요일 시간표", url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        await message.channel.send(embed=embed)

    if content.startswith("!수시간표"):
        embed=discord.Embed(description="<1교시>\n국어\n\n<2교시>\n음악\n\n<3교시>\n수학\n\n<4교시>\n영어\n\n<5교시>\n사회\n이용각선생님\n\n<6교시>\n국어\n\n<7교시>\n진로", color=0x00ff56)
        embed.set_author(name="1-9 월요일 시간표", url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        await message.channel.send(embed=embed)

    if content.startswith("!목시간표"):
        embed=discord.Embed(description="<1교시>\n과학\n\n<2교시>\n프로\n\n<3교시>\n프로\n\n<4교시>\n체육\n\n<5교시>\n국어\n\n<6교시>\n영어\n\n<7교시>\n사회\n이진경선생님", color=0x00ff56)
        embed.set_author(name="1-9 월요일 시간표", url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        await message.channel.send(embed=embed)

    if content.startswith("!금시간표"):
        embed=discord.Embed(description="<1교시>\n미술\n\n<2교시>\n미술\n\n<3교시>\n처리\n\n<4교시>\n처리\n\n<5교시>\n융합\n\n<6교시>\n창체", color=0x00ff56)
        embed.set_author(name="1-9 월요일 시간표", url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        await message.channel.send(embed=embed)
        
    if content.startswith("!도움말"):
        embed=discord.Embed(description="```diff\n-------반디코-------\n!준민이 뺨따꾸 때리기\n!인백이의 드립은\n!자기소개\n!시간\n!청소 (청소할 메시지 개수)\n!투표/(투표항목)/(투표항목)...\n!시간표\n!월시간표\n!화시간표\n!수시간표\n!목시간표\n!금시간표\n!공지 (공지내용)\n\n-------롤체-------\n!롤체지지\n!오피지지\n!악동\n!빛도자\n!용족\n!괴생명체\n!재생술사\n!망각\n!옵지 (닉네임)\n!롤체 (닉네임)\n\n-------이터널 리턴-------\n!닥지 (닉네임)\n!음식지도\n!지도\n!레시피```", color=0x00ff55)
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
                
    if message.content.startswith ("!공지"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel('')
            embed = discord.Embed(title="**공지사항 제목*", description="\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="공지 작성자 : {}".format(message.author))
            await message.channel.send ("@everyone", embed=embed)
            await message.author.send("```*[ BOT 자동 알림 ]* | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}```".format(channel, message.author, notice))
       
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))
    
    if content.startswith("!악동"):
        embed=discord.Embed(description="https://lolchess.gg/builder/set5.5?deck=891e2900e9ea11eb9b07371539a3adea", color=0x00ff56)
        embed.set_author(name="<<6악동  2기병대  2신비술사>>" , url="https://lolchess.gg/builder/set5.5?deck=891e2900e9ea11eb9b07371539a3adea")
        await message.channel.send(embed=embed)

    if content.startswith("!롤체지지"):
        embed=discord.Embed(description="https://lolchess.gg/meta", color=0x00ff56)
        embed.set_author(name="<<롤체지지>>", url="https://lolchess.gg/meta")
        await message.channel.send(embed=embed)

    if content.startswith("!CBT"):
        embed=discord.Embed(description="https://www.comcbt.com/xe/c2/4400733", color=0x00ff56)
        embed.set_author(name="<<CBT>>", url="https://www.comcbt.com/xe/c2/4400733")
        await message.channel.send(embed=embed)
    
    if content.startswith("!오피지지"):
        embed=discord.Embed(description="https://op.gg", color=0x00ff56)
        embed.set_author(name="<<오피지지>>",url="https://op.gg")
        await message.channel.send(embed=embed)

    if content.startswith("!빛도자"):
        embed=discord.Embed(description="https://lolchess.gg/builder/set5.5?deck=32e2fa40e94011ebbfb6fbef3103b627", color=0x00ff56)
        embed.set_author(name="<<7빛의 인도자  2망령  2기원자  3싸움꾼  2재생술사>>",url="https://lolchess.gg/builder/set5.5?deck=32e2fa40e94011ebbfb6fbef3103b627")
        await message.channel.send(embed=embed)
        
    if content.startswith("!용족"):
        embed=discord.Embed(description="https://lolchess.gg/builder/set5.5?deck=5ad9ced0f5ab11eb954c75ec6e5adda9", color=0x00ff56)
        embed.set_author(name="<<5용족 3척후병 3감시자 2싸움꾼>>",url="https://lolchess.gg/builder/set5.5?deck=32e2fa40e94011ebbfb6fbef3103b627")
        await message.channel.send(embed=embed)
    
    if content.startswith("!괴생명체"):
        embed=discord.Embed(description="https://lolchess.gg/builder/set5.5?deck=042b86f0e9ea11ebb5e589e115fb8433", color=0x00ff56)
        embed.set_author(name="<<4괴생명체  3망령  4주문술사  2싸움꾼>>",url="https://lolchess.gg/builder/set5.5?deck=042b86f0e9ea11ebb5e589e115fb8433")
        await message.channel.send(embed=embed)
    
    if content.startswith("!재생술사"):
        embed=discord.Embed(description="https://lolchess.gg/builder/set5.5?deck=527fcb90ef8911eba0c385872c72b794", color=0x00ff56)
        embed.set_author(name="<<4재생술사 2기원자 2빛도자 2악동 3감시자 3>>",url="https://lolchess.gg/builder/set5.5?deck=527fcb90ef8911eba0c385872c72b794")
        await message.channel.send(embed=embed)
        
    if content.startswith("!망각"):
        embed=discord.Embed(description="https://lolchess.gg/builder/set5.5?deck=83fa7470fa5811ebb02167a6298483f0", color=0x00ff56)
        embed.set_author(name="<<6망각 2기병대 2철갑 2>>",url="https://lolchess.gg/builder/set5.5?deck=83fa7470fa5811ebb02167a6298483f0")
        await message.channel.send(embed=embed)
        
    if(message.content == "!시간"):
        await message.channel.send(embed=discord.Embed(title="Time", timestamp=datetime.datetime.utcnow()))
        
    if content.startswith("!옵지"):
        nick = message.content[4:]
        embed=discord.Embed(description="오피지지 {} 바로가기\nhttps://www.op.gg/summoner/userName={}".format(nick,nick), color=0x00ff56)
        embed.set_author(name="<<{}>>".format(nick))
        await message.channel.send(embed=embed)
        
    if content.startswith("!롤체"):
        nick = message.content[4:]
        embed=discord.Embed(description="롤체지지 {} 바로가기\nhttps://lolchess.gg/profile/kr/{}".format(nick,nick), color=0x00ff56)
        embed.set_author(name="<<{}>>".format(nick))
        await message.channel.send(embed=embed)
        
    if content.startswith("!닥지"):
        nick = message.content[4:]
        embed=discord.Embed(description="닥지지 {} 바로가기\nhttps://dak.gg/bser/players/{}".format(nick,nick), color=0x00ff56)
        embed.set_author(name="<<{}>>".format(nick))
        await message.channel.send(embed=embed)
        
    if content.startswith("!음식지도"):
        embed=discord.Embed(title=" ", description=" ", color=0x00ff56)
        embed.set_author(name="```음식 지도```")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/873384193722298398/common.png")
        await message.channel.send(embed=embed)

    if content.startswith("!지도"):
        embed=discord.Embed(title=" ", description=" ", color=0x00ff56)
        embed.set_author(name="```지도```")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/873384713216225341/common.png")
        await message.channel.send(embed=embed)

    if content.startswith("!레시피"):
        embed=discord.Embed(description="```fix\n힐링포션```\n난초 + 유리병\n난초 = 약초 + 꽃\n========================\n```fix\n구급상자```\n지혈제 + 붕대\n지혈제 = 알코올 + 붕대\n========================\n```fix\n생선튀김```\n붕어 + 뜨거운 오일\n뜨거운 오일 = 오일 + 라이터\n========================\n```fix\n감자튀김```\n감자 + 뜨거운 오일\n뜨거운 오일 = 오일 + 라이터\n========================\n```fix\n피쉬앤칩스```\n감자튀김 + 생선튀김\n========================\n```fix\n햄버거```\n고기 + 빵\n========================\n```fix\n감자튀김```\n감자 + 뜨거운 오일\n뜨거운오일 = 라이터 + 오일\n========================\n```fix\n일레븐세트```\n햄버거 + 감자튀김\n========================", color=0x00ff56)
        await message.channel.send(embed=embed)
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
