#!/usr/bin/env python
from bisect import bisect
for t in xrange(1,1+int(raw_input())):
	n,x=map(int,raw_input().split())
	a=map(int,raw_input().split())
	a.sort()
	num=0
	while a:
		big=a.pop()
		num+=1
		if a:
			i=bisect(a,x-big)-1
			if 0<=i<len(a):
				if i==len(a)-1:
					if a[i]+big>x:
						continue
				del a[i]
	print"Case #%d:"%t,
	print num
