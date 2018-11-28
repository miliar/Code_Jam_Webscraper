import math

def interpret(p, s, scores):
	adjustedScores=[]
	#sUsed=0
	tally=0
	for x in scores:
		if(x/3==math.floor(x/3)):
			adjustedScores.append([x/3, x/3, x/3])
		elif(x/3-math.floor(x/3)>=.5):
			adjustedScores.append([math.ceil(x/3), math.ceil(x/3), math.floor(x/3)])
		elif(x/3-math.floor(x/3)<.5):
			adjustedScores.append([math.ceil(x/3), math.floor(x/3), math.floor(x/3)])
	print(adjustedScores)
	while s>0:
		for x in adjustedScores:
			if(x[0]==p-1 and x[0]>0 and x[2]>0 and x[0]==x[1] and s>0):
				x[0]=x[0]+1
				x[1]=x[1]-1
				s=s-1
				print(s)
			#break
		break
	print(adjustedScores)
	for x in adjustedScores:
		if(x[0]>=p):
			tally=tally+1
	print("AIMING FOR = "+str(p))
	print("TALLY = "+str(tally))
	if(lineNum<expectedlineNum):
		outputFile.write("Case #"+str(lineNum)+": "+str(tally)+"\n")
	else:
		outputFile.write("Case #"+str(lineNum)+": "+str(tally))
	return tally

def parse(input):
	lastSpace = 0
	n, s, p = "", "", ""
	scores =[]
	for x in range(0, len(line[:])):
		if(line[x]==' '):
			n = line[0:x]
			lastSpace = x
			break;
	for x in range(lastSpace+1, len(line[:])):
		if(line[x]==' '):
			s = line[lastSpace+1:x]
			lastSpace = x
			break;
	for x in range(lastSpace+1, len(line[:])):
		if(line[x]==' '):
			p = line[lastSpace+1:x]
			lastSpace = x
			break;
	while lastSpace<len(line[:]):
		for x in range(lastSpace+1, len(line[:])):
			if(line[x]==' '):
				scores.append(int(line[lastSpace:x]))
				lastSpace = x
				#break;
			if(line[x]=='\n'):
				scores.append(int(line[lastSpace:x]))
				lastSpace = x
				#break;
		break
	if(line[lastSpace:]!="\n"):
		scores.append(int(line[lastSpace:]))
	#print("n = "+str(n))
	#print("s = "+str(s))
	#print("p = "+str(p))
	#print("scores = "+str(scores))
	return interpret(int(p), int(s), scores)


print("Start.")
lineNum = 1
inputFile = open('input')
expectedlineNum = int(inputFile.readline()[:-1])
outputFile = open('output', 'w')
lastSpace = 0
for line in (inputFile.readlines()):
	parse(line)
	lineNum=lineNum+1

outputFile.close()