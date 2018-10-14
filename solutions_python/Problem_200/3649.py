#!/usr/bin/python

for t in xrange(1, int(raw_input()) + 1):
	s = map(int, list(raw_input()))
	for i in xrange(len(s) - 2, -1, -1):
		if s[i] > s[i + 1]:
			s[i] -= 1
			for i in xrange(i + 1, len(s)):
				s[i] = 9
	while s[0] == 0:
		s.pop(0)
	print "Case #{}: {}".format(t, ''.join(map(str, s)))