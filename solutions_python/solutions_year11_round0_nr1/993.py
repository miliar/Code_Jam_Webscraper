#!/usr/bin/python

T = int(raw_input())
for test in xrange(T):
	line = raw_input().split()[1:]
	t = [0, 0]
	p = [1, 1]
	time = 0
	for r, b in map(lambda x: (x[0], int(x[1])), zip(line[0::2], line[1::2])):
		i, j = 0, 1
		if r == 'B':
			i, j = 1, 0
		_t = max(0, abs(p[i] - b) - t[j]) + 1
		time += _t
		t[i] += _t
		t[j] = 0
		p[i] = b
	print "Case #%d: %d" % (test + 1, time)
