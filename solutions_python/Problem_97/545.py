#!/usr/bin/python

import bisect

def recycled(x):
	s = str(x)
	emitted = {}
	for i in xrange(1, len(s)):
		n = int(s[i:] + s[:i])
		if n > x and n not in emitted:
			yield n
			emitted[n] = True

pairs = []

for i in xrange(1, 2000001):
	for j in recycled(i):
		pairs.append((i,j))

for i in xrange(int(raw_input().strip())):
	a,b = map(int, raw_input().strip().split(" "))
	j = bisect.bisect_left(pairs, (a, 0))
	
	ans = 0
	
	while j < len(pairs) and pairs[j][0] < b:
		if pairs[j][1] <= b:
			ans += 1
		j += 1
	
	print "Case #%d: %d" % (i + 1, ans)

