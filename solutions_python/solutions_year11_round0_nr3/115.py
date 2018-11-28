import sys


T = int(raw_input())

for tt in xrange(1, T + 1):
	s = int(raw_input())
	a = [int(x) for x in raw_input().split()]
	q = 0
	p = 0
	m = a[0]
	for i in a:
		q ^= i
		p += i
		if i < m:
			m = i
	if q == 0:
		print "Case #%d:" % tt, p - m
	else:
		print "Case #%d: NO" % tt
