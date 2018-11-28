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
	D=int(data[0])
	N=int(data[1])
	c_l+=1
	max_a=0
	for n in range(N):
		data=lines[c_l+1].split(' ')
		K=int(data[0])
		S=int(data[1])
		c_l+=1
		a=float(D-K)/float(S)
		if (a>=max_a):
			max_a=a
	print("Case #{}: {}".format(p+1,D/max_a))
			
			
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
