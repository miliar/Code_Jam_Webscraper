#!/usr/bin/python3.1

import operator

case = 1
for line in open('a.txt').readlines()[1:]:
	a, b = line.strip().split()
	a = int(a)
	b = int(b)
	c = 0
	for n in range(a, b + 1):
		n = str(n)
		l = len(n)
		q = []
		for i in range(1, l):
			perm = n[l - i:l] + n[0:l - i]
			if perm[0] == '0': continue
			if perm in q: continue
			perm = int(perm)
			if int(n) < perm:
				if perm >= a and perm <= b:
					q.append(str(perm))
					c += 1
	print('Case #' + str(case) + ': ' + str(c))
	case += 1
