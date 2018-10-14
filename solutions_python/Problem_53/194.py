#!/usr/bin/python
TT=input()
for T in range(1,TT+1):
	res="Case #"+str(T)+": O"
	ll=raw_input().split();
	n=int(ll[0])
	k=int(ll[1])
	p=1<<n
	q=k%p
	if (q == p-1):
		res=res+"N"
	else:
		res=res+"FF"
	
	print res

