#!/usr/bin/env python3

for i in range(int(input())):
	n, s, p, *t = map(int, input().strip().split())
	m = 0
	if p == 0:
		m = n
	else:
		for g in t:
			if g >= 3*p - 2:
				m += 1
			elif g >= 3*p-4 and p >= 2 and s > 0:
				m += 1
				s -= 1
	print('Case #%d: %d' % (i+1, m))
