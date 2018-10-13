#!/usr/bin/env python2
import sys

def tidy(N):
	n = "%d" % N
	for x in xrange(0,len(n)-1):
		if int(n[x]) > int(n[x+1]):
			return False
	return True

def tidyfy(N):
	n = [ int(x) for x in "%d" % N ]
	N = len(n)

	for x in xrange(0,N-1):
		if( n[x] > n[x+1]):
			n[x] -= 1 
			for y in xrange(x+1,N):
				n[y] = 9

			return tidyfy(int(''.join([ "%d" % x for x in n])))


	return int(''.join([ "%d" % x for x in n]))

def solve(N):
	res = N

	for res in xrange(N,1,-1):
		if tidy(res):
			break

	return res

cases = int(sys.stdin.readline())

for case in range(cases):
	N = int(sys.stdin.readline()[:-1])
	print ("Case #%d: %d" % (case+1,tidyfy(N)))
