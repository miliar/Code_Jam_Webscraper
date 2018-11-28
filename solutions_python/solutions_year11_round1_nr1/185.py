import sys
import fractions

T = int(raw_input())

for tt in xrange(1, T + 1):
	(n, pd, pg) = [int(x) for x in raw_input().split()]
	d = 100 / fractions.gcd(pd, 100)
	if d > n or (not pg and pd) or (pg == 100 and pd != 100):
		print 'Case #%d:' % (tt), 'Broken'
	else:
		print 'Case #%d:' % (tt), 'Possible'
