f=open('C:/Users/Meir/python/codejam/Cinput3.txt', 'r')
g=open('C:/Users/Meir/python/codejam/Coutput3.txt', 'w')	
TestSize=0

aline=f.readline()
bline=aline.split(" ")

Testsize=int(bline[0])

for test in range(Testsize):
	aline=f.readline()
	bline=aline.split(" ")
	rides=int(bline[0])
	capacity=int(bline[1])
	numgroups=int(bline[2])
	aline=f.readline()
	bline=aline.split(" ")
	groups=[]
	for idx in range(numgroups):
		groups.append(int(bline[idx]))
	adict={}
	counter=0
	nextidx=0
	for agroup in range(numgroups):
		if(counter+groups[nextidx]<=capacity):
			counter+=groups[nextidx]
			nextidx= (nextidx+1) % numgroups
		while(counter+groups[nextidx]<=capacity and nextidx !=agroup):
			counter+=groups[nextidx]
			nextidx= (nextidx+1) % numgroups
		adict[agroup]=[nextidx,counter]
		counter-=groups[agroup]
	payout=0
	curgroup=0
	#print adict
	for ride in range(rides):
		payout+=adict[curgroup][1]
		curgroup=adict[curgroup][0]
	g.write("Case #" + str(test+1)+": " + str(payout)+"\n")

	 
