fp = open("C-small-attempt1.in","r")
fw = open("C-small-attempt1.out","w")
T=int(fp.readline())
for i in range(1,T+1,1):
	firstLine=fp.readline()
	R=int(firstLine[0:firstLine.find(" ")])
	firstLine=firstLine[firstLine.find(" ")+1:]
	K=int(firstLine[0:firstLine.find(" ")])
	firstLine=firstLine[firstLine.find(" ")+1:]
	N=int(firstLine)
	secondLine=fp.readline()
	group=[]
	for j in range(0,N-1):
		group.append(int(secondLine[0:secondLine.find(" ")]))
		secondLine=secondLine[secondLine.find(" ")+1:]
	group.append(int(secondLine))
	Euros=0
	for r in range(0,R):
		temp=j=0
		while(temp<=K and j<N):
			if(temp+group[0]>K):
				break
			temp=temp+group[0]
			group.append(group[0])
			del group[0]
			j=j+1
		Euros=Euros+temp
	fw.write("Case #"+str(i)+": "+str(Euros)+"\n")
fp.close()
fw.close()
