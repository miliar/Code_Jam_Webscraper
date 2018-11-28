from sys import stdin
from math import ceil

t, = map(int, stdin.readline().split())

for i in range(1,t+1):
	l, p, c = map(int, stdin.readline().split())

	pot=c
	res=0
	p=int(ceil(1.0*p/l))
	l=1
	while pot<p:
		if pot==1:
			pot=c
		else:
			pot*=pot
		res+=1
	
	print "Case #{1}: {0}".format(res, i)
