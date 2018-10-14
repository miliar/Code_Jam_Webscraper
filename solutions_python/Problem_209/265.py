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
for p in range(nb):
	data=lines[c_l+1].split(' ')
	N=int(data[0])
	K=int(data[1])
	c_l+=1
	R=[]
	H=[]
	S={}
	for n in range(N):
		data=lines[c_l+1].split(' ')
		R.append(int(data[0]))
		H.append(int(data[1]))
		if(int(data[0]) not in S or S[int(data[0])] < int(data[1])):
			S[int(data[0])] = int(data[1])
		c_l+=1
	sol=0
	curR=0
	for j in range(K):
		T=[(2*math.pi*R[i]*H[i]+(R[i]>curR)*(math.pi*(R[i]**2-curR**2)),i) for i in range(N)]
		t=max(T)
		i=t[1]
		sol+=t[0]
		if (R[i] > curR):
			curR = R[i]
		R[i]=0
		H[i]=0
	print("Case #{}: {}".format(p+1,sol))
			
			
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
