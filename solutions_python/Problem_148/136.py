
from bisect import bisect_right

t = int(raw_input())
for ti in range(t):
	(n, x) = map(int,raw_input().split())
	s = map(int,raw_input().split())
	s = sorted(s)
	b = 0
	while len(s)>0 and s[len(s)-1] == x:
		s.pop()
		b = b+1
	while len(s) > 1:
		q = s.pop()
		c = bisect_right(s,x-q)
		if c > 0:
			del s[c-1]
		b = b+1
	if len(s) > 0:
		b = b+1

	print "Case #%d: %d" % ( ti+1, b )

