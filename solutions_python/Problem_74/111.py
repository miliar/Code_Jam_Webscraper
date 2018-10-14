import sys


T = int(raw_input())

for tt in xrange(1, T + 1):
	s = raw_input().split()
	n = int(s[0])
	a = 1
	b = 1
	t = 0
	for j in xrange(0, n):
		x = -1
		y = -1
		for k in xrange(j + 1, n):
			if x == -1 and s[1 + k * 2] == 'O':
				x = int(s[2 + k * 2])
			if y == -1 and s[1 + k * 2] == 'B':
				y = int(s[2 + k * 2])
		z = int(s[2 + j * 2])
		if s[1 + j * 2] == 'O':
			d = abs(z - a) + 1
			t += d
			a = z
			if b != y and y != -1:
				d = min(d, abs(y - b))
				b += ((y - b) / abs(y - b)) * d
		else:
			d = abs(z - b) + 1
			t += d
			b = z
			if a != x and x != -1:
				d = min(d, abs(x - a))
				a += ((x - a) / abs(x - a)) * d
	print "Case #%d: %d" % (tt, t)
