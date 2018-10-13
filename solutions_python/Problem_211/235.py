import sys
import time
import math

#def eprint(*args, **kwargs):
#	print(*args, file=sys.stderr, **kwargs)

#start_time=time.time()
lines=[]
for line in sys.stdin:
	lines.append(line.strip('\n'))

nb=int(lines[0])
c_l=0
for problem in range(nb):
	data=lines[c_l+1].split(' ')
	N=int(data[0])
	K=int(data[1])
	c_l+=1
	data=lines[c_l+1].split(' ')
	U=float(data[0])
	c_l+=1
	P=[]
	data=lines[c_l+1].split(' ')
	for d in data:
		P.append(float(d))
	c_l+=1
	P.sort()
	for i,p in enumerate(P):
		if(i<len(P)-1):
			up=min(U/(i+1),P[i+1]-p)
		else:
			up=U/(i+1)
		U-=up*(i+1)
		for j in range(i+1):
			P[j]+=up
		if (U==0):
			break
	sol=1
	for p in P:
		sol*=p
		
	print("Case #{}: {}".format(problem+1,sol))
			
			
#	N=int(lines[j+1])
#	if(N!=0):
#		N2=0
#		d={}
#		for k in range(10):
#			d[str(k)]="no"
#		c=0
#		while [d[str(i)] for i in range(0,10)].count("ok") != 10:
#			c+=1
#			N2+=N
#			for l in list(str(N2)):
#				d[str(l)]="ok"
#		eprint("Case #{}: {}".format(j,N2))
#		print(N,c)
#	else:
#		eprint("Case #{}: INSOMNIA".format(j))	
#print(time.time()-start_time)
