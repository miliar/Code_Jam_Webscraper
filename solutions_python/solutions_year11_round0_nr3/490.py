#! /usr/bin/env python

from sys import stdin
import operator

if __name__=='__main__':
	T=int(stdin.readline())
	for case in xrange(1,T+1):
		stdin.readline() #discard N
		data=map(int,stdin.readline().split())
		data.sort()
		if reduce(operator.xor,data)!=0:
			answer="NO"
		else:
			answer=str(sum(data[1:]))
		print "Case #%d: %s"%(case,answer)
