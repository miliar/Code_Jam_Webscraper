#! /usr/bin/python
from sys import *

if __name__=='__main__':
	T=int(stdin.readline().strip())
	for case in xrange(1,T+1):
		n=int(stdin.readline().strip())
		v1=map(int, stdin.readline().split())
		v2=map(int, stdin.readline().split())
		v1.sort()
		v2.sort()
		v2.reverse()
		product=0
		for i in xrange(n):
			product+=v1[i]*v2[i]
		print "Case #%d: %d"%(case,product)
