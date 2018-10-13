#!/usr/bin/python

a=[]
for i in range(1,10**7+1):
	p=str(i)
	q=str(i*i)
	if p==p[::-1] and q==q[::-1]:
		a.append(i*i)

t = int(raw_input())
for j in range(t):
	[x,y] = [int(x) for x in raw_input().split()]
	v=0
	for i in a:
		if(x<=i<=y):
			v=v+1
	print "Case #%d: %d" % (j+1, v)
