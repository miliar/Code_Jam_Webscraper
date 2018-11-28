#!/usr/bin/python

import sys
import bisect

lim=10**100
pals=[]

def doit(s,off):
	p=int(s+s[-1-off::-1])
	r=p*p
	if r>lim:
		return
	rs=str(r)
	if rs!=rs[::-1]:
		return
	pals.append(r)
	for d in xrange(4):
		doit(s+str(d),off)

for d0 in xrange(1,4):
	doit(str(d0),0)
	doit(str(d0),1)

pals.sort()

tc=int(sys.stdin.readline())
for qq in xrange(1,tc+1):
	a,b=sys.stdin.readline().split()
	a=int(a)
	b=int(b)
	i=bisect.bisect_left(pals,a)
	j=bisect.bisect_right(pals,b)
	print 'Case #'+str(qq)+':',j-i
