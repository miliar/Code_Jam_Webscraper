#!/usr/bin/python

import sys

def switches(E, Q):
	ans = 0
	prev = ""
	while Q:
		lost = len(E)
		B = dict([(eng, False) for eng in E])
		if prev:
			lost -= 1
			B[prev] = True

		while Q and lost > 0:
			eng = Q[0]; del Q[0]
			if not B[eng]:
				lost -= 1
				B[eng] = True

		if lost == 0:
			ans += 1
			prev = eng

	return ans

f = open(sys.argv[1])
iters = int(f.readline())

for i in range(0, iters):
	E = []
	n = int(f.readline())
	for j in range(0, n):
		E.append(f.readline())

	Q = []
	n = int(f.readline())
	for j in range(0, n):
		str = f.readline()
		if not Q or str != Q[-1]:
			Q.append(str)

	print "Case #%d:" % (i+1), switches(E, Q)
