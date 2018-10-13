import os
import linecache
fidin=os.open("B-large.in",os.O_RDONLY);
fidout=os.open("p2large.output",os.O_WRONLY|os.O_CREAT);
T=os.read(fidin,3)
T=int(T)
print T
for i in range(T):
	inp=linecache.getline('B-large.in',i+2)
	print inp
	inp=inp.replace('\n','')
	inp=inp.split()
	C=float(inp[0])
	F=float(inp[1])
	X=float(inp[2])
	rate=2.0
	tim=0.0
	flag=False
	while(not flag):
		t1=float(X/rate)
		t2=float(C/rate)+float(X/(rate+F))
		if( t1 < t2 ):		
			tim+=t1
			flag=True
			break
		else:
			t3=float(C/rate)
			rate+=F
			tim+=t3
	if flag is True:
		A="Case #"+str(i+1)+": "+str(tim)+"\n"
		os.write(fidout,A)

