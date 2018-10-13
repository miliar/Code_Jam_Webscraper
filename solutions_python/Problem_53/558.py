#!/usr/bin/python
import sys

def snap():
	inputList = sys.stdin.readlines()
	T = int(inputList[0])
	for i in xrange(1, T + 1):
		(N,K) = [int(v) for v in inputList[i].split()]
		print "Case #%d:" % i,
		if (K + 1) % pow(2, N) == 0:
			print "ON"
		else:
		 	print "OFF"

if "__main__" == __name__:
	snap()
