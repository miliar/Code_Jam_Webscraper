#!/usr/bin/python

import sys

f = open(sys.argv[1])
casenum = int(f.readline())

for casei in xrange(casenum):
	temp = f.readline().split()
	N = int(temp[0])
	K = int(temp[1])
	if K % (1 << N) == (1 << N) - 1:
		res = 'ON'
	else:
		res = 'OFF'
	print 'Case #%d: %s' % (casei+1,res)

			
		
