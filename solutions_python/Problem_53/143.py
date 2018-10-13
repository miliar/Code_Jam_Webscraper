#!/usr/bin/env python

f = open('A-large.in', 'r')
n = int(f.readline())
count = 0
for line in f:
	res = 'OFF'
	count+=1
	(n,k) = line.split()
	n = int(n)
	k = int(k)
	if k>0:
		if k%(2**n) == (2**n-1):
			res = 'ON'
	print 'Case #' + str(count) + ': '+ res
