import sys
import math

def solve(a,b, k):
	p = 0
	for i in range(a):
		for j in range(b):
			if i&j < k:
				p+=1
	return p


T = int(sys.stdin.readline().strip())
for t in range(T):
	#print "Problem", t+1
	a, b, k = [int(v) for v in sys.stdin.readline().strip().split(' ')]
	res = solve(a,b, k)	
	
	print "Case #{0}: {1}".format(t+1, res)
