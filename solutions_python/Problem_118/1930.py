import sys
import math

def is_pal(n):
	s = str(n)
	return s == s[::-1]

cases = sys.stdin.readline()

for case in range(0,int(cases)):	
	A,B = [int(v) for v in sys.stdin.readline().split()]
	res = 0

	As = int(math.floor(A**.5)-0.5)
	Bs = int(math.ceil(B**.5)+0.5)
	p = 0

	for v in range(As, Bs+1):
		p = v*v
		if is_pal(v) and is_pal(p) and A<=p<=B:
			res += 1

	print "Case #%d: %d" % (case+1, res)
