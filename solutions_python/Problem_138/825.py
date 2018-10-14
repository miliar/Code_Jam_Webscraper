inp = open("D-large.in", "r")
testcase=int(inp.readline())
# print testcase

out = open("./largeOut.txt", "w")

for i in xrange(testcase):
	num=int(inp.readline())
	winDec=0
	loseWar=0

	naomi=sorted([float(temp) for temp in (inp.readline()).split(" ")], reverse=True)
	ken=sorted([float(temp) for temp in (inp.readline()).split(" ")], reverse=True)
	naomi2=naomi[::-1]
	ken2=ken[::-1]

# DecWar
	position=0
	for temp in naomi:
		for y in xrange(position, num):
			if ken[y]!=-1 and temp>ken[y]:
				ken[y]=-1
				winDec+=1
				position=y
				break

# war
	position=0
	for temp in naomi2:
		for y in xrange(position, num):
			if ken2!=-1 and temp<ken2[y]:
				ken2[y]=-1
				loseWar+=1
				position=y
				break

	result=str(winDec)+" "+str(num-loseWar)

	result= "Case #"+str(i+1)+": "+result
	out.write(result+"\n")

out.close()
