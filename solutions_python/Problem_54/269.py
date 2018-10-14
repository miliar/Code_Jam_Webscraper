from itertools import combinations
from nzmath.gcd import gcd
		
def solve(t):
	diff = [abs(t[j+1]-t[j]) for j in xrange(len(t)-1)]
	if not diff:
		g = t[0]
		extra = 0
	else:
		g = reduce(gcd, diff)
		err = t[0]%g
		if err:
			extra = g-t[0]%g
		else:
			extra = 0

	for x in t:
		assert( (x + extra)%g == 0 )
	return extra
	
for i in xrange(input()):
	v = map(int, raw_input().split())
	t = v[1:]
	assert(len(t) == v[0])
	print "Case #%d:"%(i+1), solve(t)	
