
def PrintRes(CDW,CW,num):
	fdOut.write("Case #"+str(num+1)+":"+" "+str(CDW)+" "+str(CW)+"\r\n")

def CountW(Naomi,Ken,P):
	N=Naomi[:]
	K=Ken[:]
	Count=0
	for i in xrange(P):
		if N[-1] > K[-1]:
			Count=Count+1
			del N[-1]
			del K[0]
		else:
			index=0			
			for val in K:
				if val>N[-1]:
					del K[index]
					break
				index=index+1
			del N[-1]
	return Count
				
				

def CountDW(Naomi,Ken,P):
	N=Naomi[:]
	K=Ken[:]
	Count=0
	for i in xrange(P):
		index=0
		deleted=0
		for val in N:
			if val>K[0]:
				del N[index]
				del K[0]
				Count=Count+1
				deleted=1
				break
			index=index+1
		if deleted==0:
			del N[0]
			del K[-1]
	return Count


fdIn = open("/home/aviv/Desktop/Code/CodeJam/2014/War/D-large.in","rb")
fdOut = open("/home/aviv/Desktop/Code/CodeJam/2014/War/D-large.out","w")

LinesNum=int(fdIn.readline().strip())
for num in xrange(LinesNum):
	N=int(fdIn.readline().strip())
	Naomi=sorted(map(float,fdIn.readline().strip().split()))
	Ken=sorted(map(float,fdIn.readline().strip().split()))
	CW= CountW(Naomi,Ken,N)
	CDW=CountDW(Naomi,Ken,N)
	PrintRes(CDW,CW,num)
				
	
	

fdIn.close()
fdOut.close()		
		

	
	
	
