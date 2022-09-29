#Python Bot
import discord
import random
import time
from asyncio import sleep
import numpy as np
from functools import reduce
from sympy.ntheory import factorint
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import datetime
import yfinance as yf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# import requests
# from lxml import html

client = commands.Bot(command_prefix = ['~','&','stan ','Stan ','Kats ','kats '])

nowSquine = 0
nowBomb = 0
nowClown = 0
nowYes = 0
Connect4Running=False

#### Streak list ############
f = open("days.txt")
days =  eval(f.read())
f.close()
########################

##### 24 list ##########
Playing=[]
f = open("24s7.txt")
Solutions= eval(f.read())
f.close()

Games=list(Solutions.keys())
f = open("Leaderboard.txt")
Rankers =  eval(f.read())
f.close()
#########################

@client.event
async def on_ready():
    print("hello scrubs")
    await client.get_channel(606926321301585920).send("I'm back bois")


@client.command(aliases=["Hi","Hello",'yo','hello'])
async def hi(ctx):
    """say hi to Mr.Kats\n"""
    await ctx.send('Hi kids!')

@client.event
async def on_message(message):
    if "doin" in message.content[-8:].lower():
        await message.channel.send("Doing Your Mom")
    await client.process_commands(message)
    
@client.command()
async def ban(ctx,*,ban):
    """Ban stuff if you have the correct permission\n"""
    await ctx.send(f'sorry you don\'t have permission to ban {ban}')

@client.command()
async def kick(ctx,*,ban):
    """Kick stuff if you have the correct permission\n"""
    await ctx.send(f'sorry you don\'t have permission to kick {ban}')

@client.command()
async def add(ctx):
    """Add to your daily streak\n"""
    global days
    today = datetime.date.today()
    person = ctx.message.author.id
    if person not in days:
        days[person] = [today,1,1]
        await ctx.send(f"First day, good luck")
        f = open("days.txt","w")
        f.write(str(days))
        f.close()
    elif today > days[person][0]:
        days[person][1]+= (today - days[person][0]).days
        days[person][2]=max(days[person][2],days[person][1])
        days[person][0] = today
        f = open("days.txt","w")
        f.write(str(days))
        f.close()
        await ctx.send(f"{days[person][1]} days! Keep it up!")
    elif today == days[person][0]:
        if days[person][1] == 0:
            days[person][1] += 1
            f = open("days.txt","w")
            f.write(str(days))
            f.close()
            await ctx.send(f"First day, good luck")
        else:
            await ctx.send("wait until tmr")


@client.command()
async def fail(ctx):
    """Break your daily streak\n"""
    global days
    today = datetime.date.today()
    person = ctx.message.author.id
    if person not in days:
        await ctx.send("You don't have a streak going")
    else:
        days[person][1]=0
        days[person][0] = today
        f = open("days.txt","w")
        f.write(str(days))
        f.close()
        await ctx.send("Damn you failed, that's sad")
    
@client.command()
async def streak(ctx):
    """Check your daily streak\n"""
    global days
    person = ctx.message.author.id
    if person not in days:
        await ctx.send("You don't have a streak going.")
    else:
        await ctx.send(f"Your current streak is {days[person][1]} day{'s'*(days[person][1]!=1)}. Your longest streak is {days[person][2]} day{'s'*(days[person][2] != 1)}.")

# @client.command(aliases =["Reddit", "Red", "red"])
# async def reddit(ctx, url): 
#     page = requests.get(url)
#     tree = html.fromstring(page.content)
#     title = tree.xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[1]/div/div[3]/div[1]/div/h1")
#     media = tree.xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[1]/div/div[5]/a")
#     print(title)
#     print(media)
    
#     if "pre" in media:
#         media = media[10:media.find("?")]

#     embed = discord.Embed(
#         color = discord.Color.blue(),
#         title = title, 
#         url = url
#     )

#     embed.set_image(url = media)
#     await ctx.send(embed=embed)
#     await ctx.message.delete()

# @client.command(aliases =["Clown"])
# async def clown(ctx):
#     """Hear Mr.Kats' beautiful voice as he discusses high level math"""
#     global nowClown
#     if time.time() - nowClown < 60:
#         await ctx.send('On Cooldown: ' + str(int(60 - (time.time() - nowClown))) + "s")
#     else:
#         channel = ctx.message.author.voice.channel
#         voice = await channel.connect()
#         voice.play(discord.FFmpegPCMAudio("clown.mp3"))
#         await sleep(1.5)
#         if voice and voice.is_connected():
#             await voice.disconnect()
#         nowClown = time.time()

# @client.command(aliases =["Yes"])
# async def yes(ctx):
#     """Hear Mr.Kats' beautiful voice as he discusses high level math"""
#     global nowYes
#     if time.time() - nowYes < 60:
#         await ctx.send('On Cooldown: ' + str(int(60 - (time.time() - nowYes))) + "s")
#     else:
#         channel = ctx.message.author.voice.channel
#         voice = await channel.connect()
#         voice.play(discord.FFmpegPCMAudio("yes.mp3"))
#         await sleep(1.5)
#         if voice and voice.is_connected():
#             await voice.disconnect()
#         nowYes = time.time()

# @client.command(aliases =["Squine"])
# async def squine(ctx):
#     """Hear Mr.Kats' beautiful voice as he discusses high level math"""
#     global nowSquine
#     if time.time() - nowSquine < 60:
#         await ctx.send('On Cooldown: ' + str(int(60 - (time.time() - nowSquine))) + "s")
#     else:
#         channel = ctx.message.author.voice.channel
#         voice = await channel.connect()
#         voice.play(discord.FFmpegPCMAudio("squine.mp3"))
#         await sleep(2)
#         if voice and voice.is_connected():
#             await voice.disconnect()
#         nowSquine = time.time()

# @client.command(aliases =["Bomb1", "b1", "B1"])
# @commands.check(lambda ctx: ctx.guild.get_role(742078280265498644) not in ctx.message.author.roles)
# async def bomb1(ctx):
#     """What in holy hell was Abhijeet thinking"""
#     global nowBomb
#     if time.time() - nowBomb < 600:
#         await ctx.send('On Cooldown: ' + str(int(600 - (time.time() - nowBomb))) + "s")
#     else:
#         channel = ctx.message.author.voice.channel
#         voice = await channel.connect()
#         voice.play(discord.FFmpegPCMAudio("bomb1.mp3"))
#         await sleep(2)
#         if voice and voice.is_connected():
#             await voice.disconnect()
#         nowBomb = time.time()

# @client.command(aliases =["Bomb2", "b2", "B2"])
# @commands.check(lambda ctx: ctx.guild.get_role(742078280265498644) not in ctx.message.author.roles)
# async def bomb2(ctx):
#     """Worst command ever created"""
#     global nowBomb
#     if time.time() - nowBomb < 600:
#         await ctx.send('On Cooldown: ' + str(int(600 - (time.time() - nowBomb))) + "s")
#     else:
#         channel = ctx.message.author.voice.channel
#         voice = await channel.connect()
#         voice.play(discord.FFmpegPCMAudio("bomb2.mp3"))
#         await sleep(2)
#         if voice and voice.is_connected():
#             await voice.disconnect()
#         nowBomb = time.time()

@client.command()
async def factor(ctx,number):
    """Brag to your friends that you can factor 20 digit numbers\n"""
    try:
        if "*" in number:
            1/0
        number = eval(number)
        if abs(number)>=1000000000000000000000000:
            1/0
        L=factorint(number)
        Factors='The prime factors are '
        for i in L:
            Factors+= f'{i},'*L[i]
        Factors=Factors.strip(',')
        await ctx.send(Factors)
    except:
        await ctx.send("Asking The Hard Hitting Questions")

# @client.command(name="clear", pass_context=True)
# @has_permissions(manage_messages=True)
# async def clear(ctx,amount=5):
#     """Idk what this does, why don't you try it"""
#     await ctx.channel.purge(limit=min(amount,1000),before=ctx.message)
#     await ctx.message.delete(delay = 1) 

# @clear.error
# async def clear_error(ctx,error):
#     if isinstance(error, MissingPermissions):
#         text = "{}, maybe if you showed up to class".format(ctx.message.author.display_name)
#         await ctx.send(text)

# @client.command(aliases =["cleart", "ClearT", "Cleart"])
# @has_permissions(manage_messages=True)
# async def cleartime(ctx,mins = 1):
#     deltatime=ctx.message.created_at-datetime.timedelta(minutes=min(mins,720))
#     await ctx.channel.purge(before=ctx.message,after=deltatime)
#     await ctx.message.delete(delay = 1) 

# @client.command()
# async def clearmy(ctx,amount=5):
#     """A family friendly clear function
#     Removes only your own mistakes in the last x messages\n"""
#     await ctx.channel.purge(limit=min(amount,1000),before=ctx.message,check=lambda msg:msg.author==ctx.author)
#     await ctx.message.delete(delay = 1) 

# @client.command(aliases =["clearnmy"])
# @has_permissions(manage_messages=True)
# async def clearnotmy(ctx,amount=5):
#     """Removes others mistakes and keeps your messages"""
#     await ctx.channel.purge(limit=min(amount,1000),before=ctx.message,check=lambda msg:msg.author!=ctx.author)
#     await ctx.message.delete(delay = 1)

# @client.command(aliases =["clearmyt", "ClearMyT", "Clearmyt"])
# async def clearmytime(ctx,mins=1):
#     """A family friendly clear function
#     Removes only your own mistakes in the last x minutes"""
#     deltatime=ctx.message.created_at-datetime.timedelta(minutes=min(mins,720))
#     await ctx.channel.purge(before=ctx.message, after=deltatime, check=lambda msg:msg.author==ctx.author)
#     await ctx.message.delete(delay = 1) 

# @client.command(aliases =["clearnmyt", "ClearNMyT", "Clearnmyt"])
# @has_permissions(manage_messages=True)
# async def clearnotmytime(ctx,mins=1):
#     """Removes others mistakes and keeps your messages"""
#     deltatime=ctx.message.created_at-datetime.timedelta(minutes=min(mins,720))
#     await ctx.channel.purge(before=ctx.message, after=deltatime, check=lambda msg:msg.author!=ctx.author)
#     await ctx.message.delete(delay = 1) 

(r,b,e) = ("<:C4r:742840235490148352>", "<:C4b:742841396607844464>", "<:C4w:742841644616908874>")

#####PUT YOUR CODE FOR CHECKING IF IT'S A WIN
#####Takes in a 7 by 6 array
#####Returns A bool
def CheckWin(arr, c, r):
    #h = 6 
    #w = 7
    color = arr[r][c]
    vert = 1
    hori = 1
    ldia = 1
    rdia = 1

    # vertical
    y = r
    while y < 5: # up
        y += 1
        if arr[y][c] == color:
            vert += 1
        else:
            break
    y = r
    while y > 0: # down
        y -= 1
        if arr[y][c] == color:
            vert += 1
        else:
            break
    if vert >= 4: # check win
        return True

    # horizontal
    x = c
    while x < 6: # right
        x += 1
        if arr[r][x] == color:
            hori += 1
        else:
            break
    x = c
    while x > 0: # left
        x -= 1
        if arr[r][x] == color:
            hori += 1
        else:
            break
    if hori >= 4: # check win
        return True

    # left diagonal
    y = r
    x = c
    while x > 0 and y < 5: # up and to the left
        x -= 1
        y += 1
        if arr[y][x] == color:
            ldia += 1
        else:
            break
    y = r
    x = c
    while x < 6 and y > 0: # down and to the right
        x += 1
        y -= 1
        if arr[y][x] == color:
            ldia += 1
        else:
            break
    if ldia >= 4: # check win
        return True

    # right diagonal
    y = r
    x = c
    while x < 6 and y < 5: # up and to the right
        x += 1
        y += 1
        if arr[y][x] == color:
            rdia += 1
        else:
            break
    y = r
    x = c
    while x > 0 and y > 0: # down and to the left
        x -= 1
        y -= 1
        if arr[y][x] == color:
            rdia += 1
        else:
            break
    if rdia >= 4: # check win
        return True
    return False # no win


@client.command(aliases = ["connect4","c4","C4"])
async def Connect4(ctx):
    """@anyone to challenge them to a game of connect4
        only usable in the Connect-4 Channel
        If you reacted too quickly, you can just unreact and react again.\n"""
    global Connect4Running
    if len(ctx.message.mentions)==1 and ctx.channel.name=="connect4-and-24" and not Connect4Running:
        Connect4Running=True
        players = {'red':ctx.message.author,'blue':ctx.message.mentions[0]} # players are author and mentioned
        turn=random.choice(('red','blue')) # randomly choose person to go first
        array=[0,0,0,0,0,0,0] # index of where to put next token in each column
        current=[[e,e,e,e,e,e,e],[e,e,e,e,e,e,e],[e,e,e,e,e,e,e],[e,e,e,e,e,e,e],[e,e,e,e,e,e,e],[e,e,e,e,e,e,e]] # image, row by row

        await ctx.send (":one::two::three::four::five::six::seven:\n") # preliminary image
        msg1 = await ctx.send(e*7+'\n'+e*7+'\n'+e*7)
        msg2 = await ctx.send(e*7+'\n'+e*7+'\n'+e*7)
        await msg2.add_reaction('1\N{COMBINING ENCLOSING KEYCAP}') # add reactions
        await msg2.add_reaction('2\N{COMBINING ENCLOSING KEYCAP}')
        await msg2.add_reaction('3\N{COMBINING ENCLOSING KEYCAP}')
        await msg2.add_reaction('4\N{COMBINING ENCLOSING KEYCAP}')
        await msg2.add_reaction('5\N{COMBINING ENCLOSING KEYCAP}')
        await msg2.add_reaction('6\N{COMBINING ENCLOSING KEYCAP}')
        await msg2.add_reaction('7\N{COMBINING ENCLOSING KEYCAP}')
        prompt=await ctx.send(f"It's {turn}'s turn. GO {players[turn].display_name}!") # first player told to go
        try:
            reaction,user = await client.wait_for('reaction_add',check=lambda reaction, user: user==players[turn], timeout=120) # some regulatory shit
        except:
            await ctx.send(f"Sad... Timed out. {players[turn].display_name} loses...") # timeout exception
            Connect4Running=False
        else:
            decision= list(filter(lambda x: f'{x}\N{COMBINING ENCLOSING KEYCAP}'==reaction.emoji, range(1,8)))[0]-1 # get column
            try:
                spot=array[decision] # get row
                array[decision]+=1 # update index in array for where to put token later
                current[spot][decision]={'red':r,'blue':b}[turn] # change image
            except:
                await ctx.send(f"No Funny Business, you're out, {players[turn].display_name}") # in case of illegal move
                Connect4Running = False
            await msg2.remove_reaction(reaction, players[turn]) # reset reactions
            turn={'red':'blue','blue':'red'}[turn] # update turn

        while Connect4Running:
            await msg1.edit(content=("".join(current[5])+'\n'+"".join(current[4])+'\n'+"".join(current[3]))) # first 3 block edited
            await msg2.edit(content=("".join(current[2])+'\n'+"".join(current[1])+'\n'+"".join(current[0]))) # second 3 block edited
            await prompt.edit(content=f"It's {turn}'s turn. GO {players[turn].display_name}!") # next player told to go
            try:
                reaction,user = await client.wait_for('reaction_add',check=lambda reaction, user: user==players[turn], timeout=120) # some regulatory shit
            except:
                await ctx.send(f"Sad... Timed out. {players[turn].display_name} loses...") # timeout exception
                Connect4Running=False
            else:
                decision= list(filter(lambda x: f'{x}\N{COMBINING ENCLOSING KEYCAP}'==reaction.emoji, range(1,8)))[0]-1 # get column
                try:
                    spot=array[decision] # get row
                    array[decision]+=1 # update index in array for where to put token later
                    current[spot][decision]={'red':r,'blue':b}[turn] # change image
                except:
                    await ctx.send(f"No Funny Business or you're out, {players[turn].display_name}") # in case of illegal move
                    Connect4Running = False
                if CheckWin(current, decision, spot): # if someone won
                    Connect4Running = False
                    await msg1.edit(content=("".join(current[5])+'\n'+"".join(current[4])+'\n'+"".join(current[3]))) # first 3 block edited
                    await msg2.edit(content=("".join(current[2])+'\n'+"".join(current[1])+'\n'+"".join(current[0]))) # second 3 block edited
                    await prompt.edit(content=f"{players[turn].display_name} wins!!!") # winner declared

                elif array[0] == array[1] == array[2] == array[3] == array[4] == array[5] == array[6] == 6: # full and no win
                    await ctx.send("Congrats, you both suck and no one won")
                await msg2.remove_reaction(reaction, players[turn]) # reset reaction
                turn={'red':'blue','blue':'red'}[turn] # change turn for next player
    elif Connect4Running:
        await ctx.send("Another Game is Running")
    elif len(ctx.message.mentions)!=1:
        await ctx.send("You didn't include a name")
    else:
        await ctx.send("You might have done it in the wrong channel, you might not have,\nbut you are kinda dumb")

## 24 game #############################################################


##Takes in a list of length 4 and a expression to see if
##The person one a game of 24
def check24(numbers,msg):
    dummythicc = list(filter(lambda x: x not in "*+-/)( ", msg))
    area = list(map(lambda x: str(x),numbers))
    if sorted(area)==sorted(dummythicc):
        try:
            return eval(msg) == 24
        except:
            return False
    else:
        return False

##Leaderboard update
def Lupdate(player,Win,timer): # {player: w, l, time, currentStreak, prevHighStreak}
    global Rankers
    if player in Rankers:
        if Win:
            Rankers[player][0] += 1
            Rankers[player][2] += timer
            Rankers[player][3] += 1
            Rankers[player][4] = max(Rankers[player][3],Rankers[player][4])
        else:
            Rankers[player][1] += 1
            Rankers[player][3] = 0
    else:
        if Win:
            Rankers[player] = [1,0,timer,1,1]
        else:
            Rankers[player] = [0,1,0,0,0]

    f = open("Leaderboard.txt","w")
    f.write(str(Rankers))
    f.close()

@client.command(aliases =["twentyfour", "24"])
@commands.check(lambda ctx: ctx.message.author.id not in Playing)
async def Twentyfour(ctx):
    """Play 24 with us
    all deals are solvable
    only allowed in the Connect4-and-24 channel\n
    """
    global Playing
    if ctx.channel.type == discord.ChannelType.private or ctx.channel.name=="connect4-and-24":
        Playing.append(ctx.message.author.id)
        name=ctx.message.author.display_name
        Win=False
        game=random.choice(Games)           #game
        cut = eval(game)                    #randomized game
        random.shuffle(cut)
        numbers= await ctx.send(f"{name}, Your numbers are {cut[0]}, {cut[1]}, {cut[2]}, {cut[3]}.")
        try:
            timer=time.time()
            message = await client.wait_for('message',check=lambda message: message.author==ctx.message.author, timeout=45) #checks for message within 45 seconds from the player
        except:
            await ctx.send(f"{name}, I'm not waiting 2 years. A possible solution was {Solutions[game]}") # timeout exception
        else:
            if check24(cut,message.content):
                await ctx.send(f"You got it, {name}. Here's a cookie :cookie:")
                Win=True
                timer=time.time()-timer
            else:
                await ctx.send(f"{name}, That's a NO from me Dawg. A possible solution was {Solutions[game]}")
        Lupdate(ctx.message.author.id,Win,timer*Win)
        Playing.remove(ctx.message.author.id)
    else:
        await ctx.send("Do this in the Connect4-and-24 Channel")


@Twentyfour.error
async def twenty_error(ctx,error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You're already playing, clown")
    else:
        await ctx.send(str(error))

@client.command()
async def fix24(ctx):
    """Use this if Stan Kats won't let you play 24\n"""
    global Playing
    if ctx.author.id in Playing: Playing.remove(ctx.author.id)

@client.command(aliases =["Top24", "L24", "l24"])
@commands.check(lambda ctx: ctx.message.author.id not in Playing)
@commands.cooldown(1,60, type = discord.ext.commands.BucketType.member)
async def Leaderboard24(ctx):
    """Check your standing in the leaderboard\n"""
    if ctx.channel.name=="connect4-and-24":
        Board= "```diff\nLeaderboard\n+ Rank:             Name              -:- Wins -:- Fails -:- Streak -:- Accuracy -:- Avg. Time\n-"
        L = []
        for each in Rankers:
            if client.get_user(each) != None:
                Pre=Rankers[each]
                win=Pre[0]
                loss=Pre[1]
                streak=Pre[4]
                timer= 0.0 if win == 0 else Pre[2]/win
                acc=win/(win+loss)
                L.append(((acc*np.log10(win+1)/np.log(timer+2)),client.get_user(each).name,win,loss,acc,timer,streak))#tuple in this order(PP,name,win,loss,acc,time)
                L.sort(key = lambda x: x[0], reverse = True)
        for i in range(len(L)):
            info=L[i]
            #                     name                wins            losses            Streak              Accuracy                     Average time
            Board += f" {i+1:>3} {info[1]:^32.32}-:- {info[2]:^5}-:- {info[3]:^6}-:- {info[6]:^7}-:- {str(info[4]* 100):0<6.6} % -:- {info[5]:<10.8}\n+" # add entries to board
        Board=Board.rstrip('+-')+"```"
        await ctx.send(Board)
    else:
        await ctx.send("Do this in the Connect4-and-24 Channel")

@Leaderboard24.error
async def L24_error(ctx,error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You're already playing, clown")
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'{int(error.retry_after)}s left')
    else:
        await ctx.send(str(error))

@commands.cooldown(1,30, type = discord.ext.commands.BucketType.member)
@client.command(aliases =["pp"])
async def PP(ctx):
    """Check your PP"""
    if ctx.channel.name=="connect4-and-24":
        if len(ctx.message.mentions) == 1:
            person = ctx.message.mentions[0].id
            if person not in Rankers:
                person = ctx.message.author.id
        else:
            person = ctx.message.author.id
        win = Rankers[person][0]
        loss = Rankers[person][1]
        timer=0 if win == 0 else Rankers[person][2]/win
        acc = win/(win+loss)
        PP = int(round(1000*(acc*np.log10(win+1)/np.log(timer+2))))
        await ctx.send(f"{client.get_user(person).name}'s PP : {PP}")

@PP.error
async def PP_error(ctx,error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'{int(error.retry_after)}s left')
    else:
        await ctx.send(str(error))



@commands.cooldown(1,86400, type = discord.ext.commands.BucketType.member)
@client.command(aliases =["restart, refresh"])
async def reset(ctx):
    """Reset your PP"""
    global Rankers
    if ctx.channel.name=="connect4-and-24":
        person = ctx.message.author.id
        del Rankers[person]
        f = open("Leaderboard.txt","w")
        f.write(str(Rankers))
        f.close()
        await ctx.send(f"{ctx.author.display_name} restarted, what a tryhard")

@reset.error
async def reset_error(ctx,error):
    if isinstance(error, commands.CommandOnCooldown):
        s = int(error.retry_after)
        h = s//3600
        m = (s % 3600)//60
        seconds = s % 60

        await ctx.send(f'{h}h {m}m {seconds}s left')
    else:
        await ctx.send(str(error))

@commands.cooldown(1,5, type = discord.ext.commands.BucketType.member)
@client.command(aliases = ["gstock", "graph", "gst"])
async def graphstock(ctx, name):
    """Graph any stock's daily price"""
    price_history = yf.Ticker(name).history(period='1d', # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                                   interval='1m', # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                                   actions=False)
    time_series = price_history['Close']
    dt_list = price_history.index
    matplotlib.rcParams.update({
        "lines.color": "#00FF00",
        "patch.edgecolor": "white",
        "text.color": "white",
        "axes.facecolor": "#36393E",
        "axes.edgecolor": "lightgray",
        "axes.labelcolor": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "grid.color": "lightgray",
        "figure.facecolor": "black",
        "figure.edgecolor": "lightgray",
        "savefig.facecolor": "#36393E",
        "savefig.edgecolor": "black"})
    ax = plt.figure().gca()
    ax.set_yticks(np.arange(min(time_series), max(time_series)+0.01, (1/12)*(max(time_series) - min(time_series))))
    myFmt = mdates.DateFormatter('%H:%M')
    ax.xaxis.set_major_formatter(myFmt)
    plt.grid()
    day = f"{dt_list[0].month}/{dt_list[0].day}"
    plt.title(f"{name.upper()}: {day}")
    plt.xlabel("Time")
    plt.ylabel("Price")
    image = discord.File("graph.png")
    plt.plot(dt_list, time_series, linewidth=1.5, color = "#00FF00")
    plt.savefig("graph.png", bbox_inches='tight', dpi = 200)
    plt.close()
    await ctx.send(file=image)
    await ctx.send(f"{name.upper()}: ${time_series[-1] : .2f}")
@graphstock.error
async def graphstock_error(ctx,error):
    await ctx.send(str(error))

@client.command(aliases = ["stock", "st", "price"])
async def stockprice(ctx, name):
    """Get any stock's current price"""
    price_history = yf.Ticker(name).history(period='1d', # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                                   interval='1m', # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                                   actions=False)
    price = price_history["Close"][-1]
    await ctx.send(f"{name.upper()}: ${price : .2f}")

@stockprice.error
async def stockprice_error(ctx,error):
    
    await ctx.send(str(error))




client.run('')
