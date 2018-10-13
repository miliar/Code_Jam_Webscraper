#!/usr/bin/env python
#
# Lars Lindgren <chrono@eeky.net>
#

def is_tidy(n):
	if n < 9:
		return True
	s = str(n)
	if s[0] <= s[-1]:
		x=s[0]
		for c in s:
			if c < x:
				return False	
			else:
				x=c
		return True
	return False

def last_tidy(n):
	for m in range(n, -1, -1):
		if is_tidy(m):
			return m

t = int(raw_input())
for i in xrange(1, t + 1):
	n = int(raw_input())
	print 'Case #%d: %s' % (i, last_tidy(n))
