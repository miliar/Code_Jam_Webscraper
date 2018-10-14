#!/usr/bin/python

import sys

T = int(sys.stdin.readline().strip())

# C: cost of farm
# F: farm production rate
# X: cookie goal
def optimal_time(C,F,X):
	C = float(C)
	F = float(F)
	X = float(X)

	if C>X: return X/2 # time needed to win

	n = 0. # number of farms
	t = C/2 # time take to reach first milestone (natural prod rate is 2)
	while X/(2+(n+1)*F) < (X-C)/(2+n*F): # while it is better to build farms at milestone
		n += 1 # increment number of farms
		t += C/(2+n*F) # time taken to reach next milestone
	t += (X-C)/(2+n*F) # milestone means I have C cookies so only need X-C to win
	return t

for i in range(1,T+1):
	C,F,X = sys.stdin.readline().strip().split()
	print "Case #%s: %.7f" % (i, optimal_time(C,F,X))
