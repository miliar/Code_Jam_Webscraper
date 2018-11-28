import math


def PrintRes(Res,num):
		fdOut.write("Case #"+str(num+1)+": %.7f\r\n" % Res)



fdIn = open("/home/aviv/Desktop/Code/CodeJam/2014/Cookie/B-large.in","rb")
fdOut = open("/home/aviv/Desktop/Code/CodeJam/2014/Cookie/B-large.out","w")

LinesNum=int(fdIn.readline().strip())
for num in xrange(LinesNum): 
	Vals = map(float,fdIn.readline().strip().split())
	C=Vals[0]
	F=Vals[1]
	X=Vals[2]
	k = 1
	TOld=X/2
	Sum=0
	while True:
		Sum=Sum+C/(2+(k-1)*F)
		TNew=Sum+X/(2+k*F)
		if TNew>TOld:
			PrintRes(TOld,num)
			break 
		k=k+1
		TOld=TNew
	
	

fdIn.close()
fdOut.close()		
		

	
	
	
