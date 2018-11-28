#!/usr/bin/python

import sys, os

cases = int(sys.stdin.readline())

def check(fintime, n, t):
	s = ""
	swaps = 0
	finishers = 0
	
	#print "checking {0}, {1}, {2}".format(fintime, n, t)
	
	while finishers < n:
		for i in xrange(len(fintime)):
			if fintime[i] <= t:
				#print "Need to perform {0} swaps for {1} to finish".format(i, fintime[i])
				finishers += 1
				swaps += i
				fintime.pop(i)
				break
			elif i == len(fintime) -1:
				return "IMPOSSIBLE"
	return swaps

for case in xrange(cases):
#for case in [0]:
	n, k, b, t = map(int, sys.stdin.readline().strip().split() )
		
	ipos = map(int, sys.stdin.readline().strip().split() )
	ivel = map(int, sys.stdin.readline().strip().split() )
	
	fintime = [ float(b-ipos[i])/float(ivel[i]) for i in range(len(ivel)) ]
	#fintime = [float(b)/float(vel) for vel in ivel]
	
	fintime.reverse()
	
	s = check(fintime, k, t)
	print "Case #{0}: {1}".format( case + 1, s)
	
	
