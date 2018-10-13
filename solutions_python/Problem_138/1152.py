fin = open("D:\\Users\\Ebrai\\Documents\\NetBeansProjects\\Codejam2014\\in.txt", "r")
t=int(fin.readline())

fout = open("D:\\Users\\Ebrai\\Documents\\NetBeansProjects\\Codejam2014\\out.txt", "w")

for i in xrange(t):
	num=int(fin.readline())
	winDec=0
	loseWar=0

	naomi=sorted([float(temp) for temp in (fin.readline()).split(" ")], reverse=True)
	ken=sorted([float(temp) for temp in (fin.readline()).split(" ")], reverse=True)
	naomiRev=naomi[::-1]
	kenRev=ken[::-1]

	position=0
	for temp in naomi:
		for y in xrange(position, num):
			if ken[y]!=-1 and temp>ken[y]:
				ken[y]=-1
				winDec+=1
				position=y
				break

	position=0
	for temp in naomiRev:
		for y in xrange(position, num):
			if kenRev!=-1 and temp<kenRev[y]:
				kenRev[y]=-1
				loseWar+=1
				position=y
				break

	result=str(winDec)+" "+str(num-loseWar)

	result= "Case #"+str(i+1)+": "+result
	fout.write(result+"\n")

fout.close()
