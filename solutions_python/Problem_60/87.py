#!/usr/bin/env python

import sys

T = int(sys.stdin.readline())
for case in xrange(T):
	N,K,B,T = [int(x) for x in sys.stdin.readline().split()]
	
	n = [int(x) for x in sys.stdin.readline().split()]
	vel = [int(x) for x in sys.stdin.readline().split()]
	v = []
	for i in xrange(len(n)):
		if n[i] + T*vel[i] >= B:
			v.append(1)
		else:
			v.append(0)
			
	ret = 0
	madeit = 0
	good = 0
	if K > 0:
		for i in xrange(len(v)):
			j = len(v) - 1 - i
			if v[j] == 1:
				for k in xrange(j+1,len(v)):
					if v[k] == 0:
						ret += 1
				madeit += 1
				if madeit == K:
					good = 1
					break
	else:
		good = 1
	if good:
		print "Case #%d: %d" % (case+1, ret)
	else:
		print "Case #%d: IMPOSSIBLE" % (case+1)
					
			
		
