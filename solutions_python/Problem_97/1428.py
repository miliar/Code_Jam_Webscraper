from math import *

def is_recycled(a, b):
	a = str(a)
	b = str(b)
	if sorted(a) == sorted(b):
		for x in all_rotations(a):
			if x == b:
				return True
	return False

def rotate_left(n):
	return n[-1] + n[0:-1]

def all_rotations(n):
	digits = len(n)
	for i in xrange(0, digits):
		n = rotate_left(n)
		yield n


testcases = int(raw_input())

for x in xrange(0, testcases):
	a, b = [ int(n) for n in raw_input().split()]
	recycled = set()
	for i in xrange(a,b+1):
		for j in xrange(i+1, b+1):
			if is_recycled(i, j):
				recycled.add((i,j))
	print "Case #%d: %d" % ( x + 1, len(recycled))


