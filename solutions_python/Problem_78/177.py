#!/usr/bin/python

def okay(n, pd, pg):
	if (pg == 100 and pd < 100) or (pg == 0 and pd > 0): return False
	for d in xrange(1, min(n, 100) + 1):
		z = d * pd / 100
		if z * 100 / d == pd:
			return True
	return False

T = int(raw_input())
for i in xrange(1, T + 1):
	(n, pd, pg) = map(long, raw_input().split())
	print "Case #%d:" % i, 
	if not okay(n, pd, pg):
		print 'Broken'
	else:
		print 'Possible'
