import sys

def readinputs():
	return list(map(int, sys.stdin.readline().strip().split(' ')))

def ride(gs, k):
	on = 0
	
	inside = []
	outside = []
	inappend = inside.append
	outappend = outside.append
	
	full = False
	for g in gs:
		p = on + g
		if p <= k and not full:
			on = p
			inappend(g)
		else:
			full = True
			outappend(g)
	
	return [outside + inside, on]

def do(case):
	R, k, N = readinputs()
	gs = readinputs()
	
	total = 0
	for i in xrange(R):
		gs, money = ride(gs, k)
		total = total + money
	
	print "Case #%d: %d" % (case + 1, total)


if __name__ == "__main__":
	T = readinputs()[0]
	map(do, range(T))