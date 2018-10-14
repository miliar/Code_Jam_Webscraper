#!/usr/bin/python

# Constants definition
MINFLOAT = 1e-6

def isEqual(float_a, float_b):
	if abs(float(float_a) - float(float_b)) < MINFLOAT: return True
	else: return False



for case in xrange(input()):
	raw_input()
	a = map(int,raw_input().split())
	b = map(int,raw_input().split())

	a.sort()
	b.sort(reverse=True)
	sol = 0

	for i in xrange(len(a)):
		sol += a[i]*b[i]
	
	#print "Case #%d:\n%s\n%s" % (case + 1, a, b)
	print "Case #%d: %d" % (case + 1, sol)
