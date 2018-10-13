#!/usr/bin/env python

t = input()

for ti in range(1, t+1):
	n, x = map(int, raw_input().split())
	s = map(int, raw_input().split())
	s.sort(reverse=True)
	#print n, x, s

	ans = 0
	while s:
		#print s
		ans += 1
		first, s = s[0], s[1:]
		for f in s:
			if first + f <= x:
				s.remove(f)
				break

	print 'Case #' + str(ti) + ':', ans