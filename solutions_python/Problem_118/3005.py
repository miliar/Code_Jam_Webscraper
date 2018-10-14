#!/usr/bin/env python
#coding=utf-8

# Last Change: 2010-05-08 14:55:00

import sys
import math

def p(num):
	s = str(num)
	#print s, 
	for i in range(len(s)/2):
		#print s[i], s[-(i+1)]
		if s[i] != s[-(i+1)]:
			return False
	return True

f = file(sys.argv[1])
ncase = int(f.readline())

for nncase in range(ncase):
	(A,B) = [ int(x) for x in f.readline().split()]
	#print A,B

	a = int(math.sqrt(A))
	b = int(math.sqrt(B))

	if a*a < A:
		a += 1


	#print a,b
	count = 0
	for i in range(a, b+1):
		if p(i) and p(i*i):
			count += 1

	print "Case #%d: %d"%(nncase+1, count)
f.close()

