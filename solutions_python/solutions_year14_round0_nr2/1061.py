#!/usr/bin/python

import sys

def lin2(C,F,X):
	buyTime=0
	rate = 2.0
	next = buyTime + X / rate
	last = next + 1
	while next < last:
		last = next
		buyTime += C/rate
		rate += F
		next = buyTime + X / rate
	return last

def eval(C, F, X):
	return lin2(C,F,X)

T = int(sys.stdin.readline())
for i in range(1,T+1):
	(C, F, X) = [float(elem) for elem in sys.stdin.readline().split()]
	print 'Case #' + str(i) + ': ' + str(eval(C,F,X))
