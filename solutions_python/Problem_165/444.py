import math
input=open("BS_s.in","r")
out=open("BS`_s.out","w")
T=int(input.readline())
for t in range(1,T+1):
	R,C,W=map(int,input.readline().split())
	rem=math.ceil(1.0*C/W)
	count=(R-1)*rem + rem+W-1
	print "Case #"+str(t)+": "+str(int(count))		
	out.write("Case #"+str(t)+": "+str(int(count))+"\n")		
	
	