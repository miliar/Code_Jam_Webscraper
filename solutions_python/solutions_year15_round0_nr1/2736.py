#!/usr/bin/env python

for tc in xrange(input()):
	m, s = raw_input().strip().split()
	m = int(m)
	t, ans = 0, 0
	for i in xrange(len(s)):
		if t < i:
			f = i-t
			t += f
			ans += f
		t += int(s[i])
	print "Case #%d: %d" % (tc+1, ans)
