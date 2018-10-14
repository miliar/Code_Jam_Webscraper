from math import *
from Queue import Queue

def count(n,c):
	if c is None:
		return 0
	return c[:-1].count(n)*c[2]


T=int(raw_input())
for t in range(1,T+1):
	N,K=map(int,raw_input().split())
	pos=Queue()
	pos.put((N-N//2-1,N//2,1))
	pos.put(None)
	curr=None
	while True:
		#print(N)
		#print(pos.queue)
		c1=pos.get()
		K-=c1[2]
		if K<=0:
			curr=c1
			break

		c2=pos.get()
		if c2 is not None:
			K-=c2[2]
			if K<=0:
				curr=c2
				break

		#find
		m=min(c1[:-1]+(c2[:-1] if c2 is not None else ()))
		cm=count(m,c1)+count(m,c2)

		M=max(c1[:-1]+(c2[:-1] if c2 is not None else ()))
		cM=count(M,c1)+count(M,c2)

		c1New=(M-M//2-1,M//2,cM)
		c2New=(m-m//2-1,m//2,cm) if m!=M else None
		
		pos.put(c1New)
		pos.put(c2New)

	print("Case #%d: %d %d" % (t,max(curr[0],curr[1]),min(curr[0],curr[1])))
