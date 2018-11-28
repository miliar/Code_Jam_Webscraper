from math import fabs

def solve(A, B, K):
	c = 0
	for x in xrange(A):
		for y in xrange(B):
			if x & y < K:
				#print x,y
				c += 1
	return c

caseCount = int(raw_input())

for case in xrange(caseCount): 
	data = raw_input().split(" ")
	print "Case #%d: %s" % (case+1,solve(int(data[0]), int(data[1]), int(data[2])))
