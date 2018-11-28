
def PrintRes(Res,num):
	if Res==-1:
		fdOut.write("Case #"+str(num+1)+": Volunteer cheated!\r\n")
	elif Res==-2:
		fdOut.write("Case #"+str(num+1)+": Bad magician!\r\n")
	else:
		fdOut.write("Case #"+str(num+1)+":"+" "+str(Res)+"\r\n")

def CheckCard(RowNums1,RowNums2):
	Count={}
	for val in RowNums1+RowNums2:
		if val in Count:
			Count[val]=Count[val]+1
		else:
			Count[val]=1
	Res=[]
	for val in Count:
		if Count[val]>1:
			Res.append(val)
	if len(Res)==1:
		return Res[0]
	elif len(Res)==0:
		return -1
	else:
		return -2

fdIn = open("/home/aviv/Desktop/Code/CodeJam/2014/Magic/A-small-attempt0.in","rb")
fdOut = open("/home/aviv/Desktop/Code/CodeJam/2014/Magic/A-small-attempt0.out","w")

LinesNum=int(fdIn.readline().strip())
for num in xrange(LinesNum): 
	Row1=int(fdIn.readline().strip())
	for i in xrange(1,5):
		if i == Row1:
			RowNums1=map(int,fdIn.readline().strip().split())
		else:
			fdIn.readline()
	Row2=int(fdIn.readline().strip())
	for i in xrange(1,5):
		if i == Row2:
			RowNums2=map(int,fdIn.readline().strip().split())
		else:
			fdIn.readline()
	Res = CheckCard(RowNums1,RowNums2)
	PrintRes(Res,num)
	

fdIn.close()
fdOut.close()		
		

	
	
	
