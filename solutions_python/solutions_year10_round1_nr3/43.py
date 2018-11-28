cutoffs=[]
cutoffs.append(0)
cutoffs.append(1)
cutoffs.append(2)
curtest=2
for idx in range(3,1000001):
	while(cutoffs[curtest]+curtest-1<idx):
		curtest+=1
	cutoffs.append(curtest)

#print cutoffs

##Format for 1 line per test
f=open('C:/Users/Meir/python/codejam/input2.txt', 'r')
g=open('C:/Users/Meir/python/codejam/output2.txt', 'w')
	
Length=0
Dictsize=0
TestSize=0

aline=f.readline()
bline=aline.split(" ")

Testsize=int(bline[0])

for test in range(Testsize):
	aline=f.readline()
	bline=aline.split(" ")
	alower=int(bline[0])
	atop=int(bline[1])
	blower=int(bline[2])
	btop=int(bline[3])
	counter=0
	for idx in range(alower,atop+1):
		for idx2 in range(blower, btop+1):
			if(idx>idx2):
				if(cutoffs[idx]>idx2):
					#print idx, idx2
					counter+=1
			elif(idx2>idx):
				if(cutoffs[idx2]>idx):
					#print idx, idx2
					counter+=1
	##OUTPUT	
	g.write("Case #" + str(test+1)+": " + str(counter)+"\n")
			

	 
