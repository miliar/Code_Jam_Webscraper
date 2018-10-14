import sys
from operator import xor

T = int(sys.stdin.readline())

for case in range(T):
	print "Case #%d:" % (case+1),
	
	N = int(sys.stdin.readline())
	vals = map(int, sys.stdin.readline().split(' '))
	vals = sorted(vals)
	p = reduce(xor, vals)
	if p == 0:
		print sum(vals[1:])
	else:
		print "NO"