def check():
	count=0


	for i in xrange(len(farright)):
		if farright[i]>i:
			count+=1
			
		
		
	if count==0:
		return True
	else:
		return False

f=open("A-large.in")

g=open("A-out","w")
T=int(f.readline())
for case in xrange(1,T+1):
	N=int(f.readline())
	farright=[]
	counter=0
	for i in xrange(N):
		rawr2=f.readline()
		rawr=[]
		for j in xrange(N):
			rawr.append(int(rawr2[j]))
		
		farrigh=-1
		for j in xrange(N):
			if rawr[j]==1:
				farrigh=j
		farright.append(farrigh)
	while not check():
		best=10000
		for i in xrange(len(farright)-1,-1,-1):
			if farright[i]<=0:
				best=i
		counter+=best
		print best,farright
		farright.pop(best)
		for i in xrange(len(farright)):
			if farright[i]>=1:
				farright[i]-=1
	g.write("Case #"+str(case)+": "+str(counter)+"\n")
	
g.close()
f.close()	

