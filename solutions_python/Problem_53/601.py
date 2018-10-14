#! /usr/bin/python

import sys

def snap(N,K):
	mask = (1 << N) - 1
	return K & mask == mask

if __name__ == "__main__":
	testcases = int(sys.stdin.readline())
	for case in xrange(1,testcases+1):
		N,K = map(int, sys.stdin.readline().strip().split())
		if snap(N,K):
			print "Case #%d: ON" % (case,)
		else:
			print "Case #%d: OFF" % (case,)
