import math

T=int(raw_input())
a=0
e=[]
while a<T:
	b=[int(x) for x in raw_input().split()]
	e.append(b)
	a=a+1

def sfloor(x): return int(math.floor((x-1.0)/2))
def sceil(x): return int(math.ceil((x-1.0)/2))

a=0
while a<T:
	c=e[a][0]
	d=e[a][1]
	f=bin(d)
	g=len(f)-1
	while g>2:
		if int(f[g])==1: c=sfloor(c)
		if int(f[g])==0: c=sceil(c)
		g=g-1
			
	q=a+1
	r="Case #"+str(q)+": "+str(sceil(c))+" "+str(sfloor(c))
	print r
	a=a+1





 