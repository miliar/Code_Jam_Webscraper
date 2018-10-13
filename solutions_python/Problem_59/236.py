#!/usr/bin/env python3

t = int(input())
for x in range(t):
	y = 0
	n, m = map(int, input().strip().split())
	e = {}
	for i in range(n):
		d = input().strip().split('/')[1:]
		p = e
		for z in d:
			if z not in p:
				p[z] = {}
			p = p[z]
	for i in range(m):
		d = input().strip().split('/')[1:]
		p = e
		for z in d:
			if z not in p:
				p[z] = {}
				y += 1
			p = p[z]
	print('Case #%d: %d' % (x + 1, y))
