import sys
import time

#def eprint(*args, **kwargs):
#	print(*args, file=sys.stderr, **kwargs)

#start_time=time.time()
lines=[]
for line in sys.stdin:
	lines.append(line.strip('\n'))

nb=int(lines[0])
for j in range(nb):
	data=lines[j+1].split(' ')
	S=list(str(data[0]))
	size=len(S)
	K=int(data[1])
	c=0
	imp=0
	for i,l in enumerate(S):
		if(l=='-'):
			if(i>size-K):
				print("Case #{}: IMPOSSIBLE".format(j+1))
				imp=1
				break
			c+=1
			for k in range(i,i+K):
				if(S[k]=='+'):
					S[k]='-'
				else:
					S[k]='+'
	if(imp==0):
		print("Case #{}: {}".format(j+1,c))
			
			
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
