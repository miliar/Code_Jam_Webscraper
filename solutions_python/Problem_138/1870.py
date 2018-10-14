import sys
T=int(sys.stdin.readline())
buffern=[]
bufferk=[]
number_of_blocks=[]
for i in xrange(T):
	N=int(sys.stdin.readline())
	number_of_blocks.append(N)
	Naomi=[float(x) for x in sys.stdin.readline().strip('\n').split()]
	buffern.append(Naomi)
	ken=[float(x) for x in sys.stdin.readline().strip('\n').split()]
	bufferk.append(ken)


#print bufferk   
#print min(bufferk[1])


for j in xrange(T):
	count=0
	w=0
	buffern[j].sort()
	bufferk[j].sort(reverse=True)
	min_in_ken=min(bufferk[j])
	dw=sum(x>min_in_ken for x in buffern[j] )
	#print dw
	#print buffern[j]
	#print number_of_blocks[j]
	#print bufferk[j]
	z=len(buffern[j])
	z1=len(bufferk[j])
	while z!=0 and z1!=0:
		#print len(buffern[j])
		wc=0
		k=0
		max_in_ken=max(bufferk[j])
		wc=sum(y>max_in_ken for y in buffern[j])
		print "wc" +str(wc)
		w=w+wc
		
		print "n"+str(buffern[j])
		print "k"+str(bufferk[j])
		bufferk[j].pop()
		if(wc!=number_of_blocks[j] and wc!=0):
			for k in xrange(wc):
				buffern[j].pop()
				
				z-=1
			for k in xrange(wc):
				bufferk[j].pop()	
		elif(wc==number_of_blocks[j]):
			z=0
				
	#print w		
	print "Case #"+str(j+1)+": "+str(dw)+" "+str(w)


	

