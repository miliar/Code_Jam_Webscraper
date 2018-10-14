inp = open("input.txt")
outp = open("output.txt","w")

T=int(inp.readline())
i=0

while (i<T):
	line = inp.readline()
	seq = line.split(" ")
	N = int(seq[0])
	totalTime=0
	botTime=0
	Pos=1
	othPos=1
	j=0
	curBot = line[1]
	
	outp.write("Case #"+str(i+1)+": ")
	while (j<N):
		Bot=seq[j*2+1]
		
		if (Bot==curBot):
			time=abs(int(seq[j*2+2])-Pos)+1
			Pos=int(seq[j*2+2])
			botTime+=time
			totalTime+=time
		
		else:
			tempPos=Pos
			Pos=othPos
			othPos=tempPos
			
			time=abs(int(seq[j*2+2])-Pos)+1
			Pos=int(seq[j*2+2])
			if (time>botTime):
				time=time-botTime
				botTime = time
			else:
				time=1
				botTime=1
			totalTime+=time
			curBot = Bot
			
		j+=1
	outp.write(str(totalTime)+"\n")
	i+=1
