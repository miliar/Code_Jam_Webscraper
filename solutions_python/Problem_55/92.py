import sys

def ride(g, gi):
	on = 0
	qlen = len(g)
	while on + g[gi] <= k and qlen > 0:	
		on += g[gi]
		gi = (gi + 1) % len(g)
		qlen -= 1
	return gi, on

T=int(sys.stdin.readline())
for case in range(T):
	(R,k,N) = map(int, sys.stdin.readline().split())
	g = map(int, sys.stdin.readline().split())
	seen = [None] * N
	rn = 0
	gi = 0
	sum = 0
	while rn < R:
		if seen[gi] is None:
			seen[gi] = (rn, sum)
			gi, on = ride(g, gi)
			rn += 1
			sum += on
		else:
			orn, osum = seen[gi]
#			print "loop at %d: %d, %d -> %d, %d" % (gi, orn, osum, rn, sum)
			looplen = rn-orn
			loopsum = sum-osum
			loops = (R-rn) / looplen
			rn += loops*looplen
			sum += loops*loopsum
			seen = [None] * N
	print "Case #%d: %d" % (case+1, sum)
