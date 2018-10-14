#!/usr/bin/python
#
# Google Code Jam
#
#

import sys
import os

debug=False

def solve_test_case(N,K,B,T,pos,vel):
	ahead = 0
	ahead_slow = 0
	swaps = 0

	if debug:
		print "T:",T,"K:",K,"B:",B

	if K == 0: return 0

	max = N
	if K > max: return "IMPOSSIBLE"
	
	for i in xrange(N-1,-1,-1):
		if (pos[i] + vel[i]*T) >= B:
			if debug:
				print "pos: %d, vel: %d: fast enough" % (pos[i],vel[i])
			if ahead_slow != 0:
				swaps += ahead_slow
			ahead += 1
			if ahead == K: return swaps
		else:
			max -= 1
			if K > max: return "IMPOSSIBLE"
			if debug:
				print "pos: %d, vel: %d: too slow" % (pos[i],vel[i])
			ahead_slow += 1
	return "IMPOSSIBLE"
		
		
		
	

if __name__ == '__main__':
    input = open(sys.argv[1])
    if len(sys.argv) > 2 and sys.argv[2] == "--debug": debug=True
    test_case_count = int(input.readline().strip())
    test_case = 0
    while test_case < test_case_count:
	N,K,B,T = map(int,input.readline().strip().split())
	pos = map(int, input.readline().strip().split())
	vel = map(int, input.readline().strip().split())
        test_case += 1
        print "Case #%d: %s" % (test_case, solve_test_case(N,K,B,T,pos,vel))


 
            
 
