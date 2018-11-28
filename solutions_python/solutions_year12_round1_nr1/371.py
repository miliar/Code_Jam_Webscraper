#!/usr/bin/python3


def read_case(fd):
	
	A, B = [ int(s) for s in fd.readline().strip().split() ]
	p =  [ float(s) for s in fd.readline().strip().split() ]
	
	return (A,B,p)

def prep_tables(p):
	N = len(p)
	ok = [1.0]*(N+1)
	for i in range(N):
		ok[i+1] = ok[i]*p[i]
	ok.reverse()
	return ok
	
def calc_prop(A, ok, n):
	"""
	Calc prob of Ok removing n chars
	"""
	# Remove all ==> sure
	if n==A:
		return 1.0;
	return ok[n]

def calc_expected(A, B, ok, n):
	"""
	Expected keystrokes removing n
	"""
	pOk = calc_prop(A, ok, n)
	base = B-A+1+2*n
	return base + (B + 1)*(1.0-pOk)



import sys

fd = open(sys.argv[1], "r")

T = int(fd.readline().strip())

for i in range(T):
	A, B, p = read_case(fd)
	ok = prep_tables(p)
	hit_enter = B+2
	best = hit_enter
	last = None
	for n in range(A+1):
		keys = calc_expected(A, B, ok, n)
		best = min(best, keys)
		if last is not None and last<keys:
			break
		else:
			last = keys
	print("Case #%d: %.6f" %(i+1, best))
	
	
	
	

	
	
