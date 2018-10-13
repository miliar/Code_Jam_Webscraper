import sys

t = int(raw_input())

for i in xrange(t):
	d, n = map(int, raw_input().split())
	k, s = [], []
	for j in range(n):
		ki, si = map(int, raw_input().split())
		k.append(ki)
		s.append(si)

	slow_index, max_time = -1, -sys.maxint
	for j in range(n):
		time = (d - k[j]) * 1.0 / s[j]
		if time > max_time:
			slow_index = j
			max_time = time
	
	cruise = d * 1.0 / max_time

	print 'Case #%d: %f' % (i+1, cruise)