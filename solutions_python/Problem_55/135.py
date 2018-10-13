#!/usr/bin/python
import sys

s = sys.stdin.readline ()
tests = int (s)
for test in range (tests):
	s = sys.stdin.readline ()
	r, k, n = [int (x) for x in s.split ()]
	s = sys.stdin.readline ()
	a = [int (x) for x in s.split ()]
	assert len (a) == n

	b = [0] + a + a
	cur = 0
	c = []
	d = []
	j = 1
	for i in range (1, n + 1):
		cur -= b[i - 1]
		while j < i + n and cur + b[j] <= k:
			cur += b[j]
			j += 1
		c += [cur]
		d += [j - i]

	t = [-1] * n
	sum = 0
	sums = [0]
	t[0] = 0
	q = 0
	p = 0
	while q < r:
		q += 1
		sum += c[p]
		sums += [sum]
		p = (p + d[p]) % n
		if t[p] != -1:
			break
		t[p] = q

	if q < r:
		v = q - t[p]
		u = r - q
		u /= v
		sum += (sums[q] - sums[t[p]]) * u
	        u *= v
	        q += u

	while q < r:
		q += 1
		sum += c[p]
		p = (p + d[p]) % n

	sys.stdout.write ('Case #%d: %d\n' % (test + 1, sum))
