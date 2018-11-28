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
	R=int(data[1])
	O=int(data[2])
	Y=int(data[3])
	G=int(data[4])
	B=int(data[5])
	V=int(data[6])
	c_l+=1
	uni=[(R,'R'),(O,'O'),(Y,'Y'),(G,'G'),(B,'B'),(V,'V')]
	max_u=max(uni)[0]
	if (max_u > N/2):
		print("Case #{}: IMPOSSIBLE".format(p+1))
	else:
		sol=[]
		l_i=[0 for i in range(max_u)]
		uni.sort()
		i=0
		for u in uni[::-1]:
			nb_u=u[0]
			while (nb_u>0):
				sol.insert(l_i[i],u[1])
				for j in range(i,max_u):
					l_i[j]+=1
				nb_u-=1
				i=(i+1)%max_u
		print("Case #{}: {}".format(p+1,''.join(sol)))
			
			
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
