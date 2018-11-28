#!/usr/bin/python

# B. Magicka

import math
import sys

f = sys.stdin
T = int(f.readline())

for lineno in range(1, T+1):
	list = f.readline().split()
	index = 0
	C = int(list[index])
	index += 1
	Clist = [(e[0], e[1], e[2]) for e in list[index:index+C]]
	index += C
	D = int(list[index])
	index += 1
	Dlist = [(e[0], e[1]) for e in list[index:index+D]]
	index += D
	N = int(list[index])
	index += 1
	S = [c for c in list[index]]
	E = []

	for c in S:
		E.append(c)
		if len(E) < 2: continue

		# combine
		for comb in Clist:
			if (comb[0] == E[-1] and comb[1] == E[-2]) or (comb[1] == E[-1] and comb[0] == E[-2]):
				E = E[:-2]
				E.append(comb[2])
				break

		if len(E) < 2: continue
		# opposed
		for dist in Dlist:
			if (E[-1] == dist[0]):
				if dist[1] in E:
					E = []
					break
			elif (E[-1] == dist[1]):
				if dist[0] in E:
					E = []
					break

	s = "Case #%s: %s" % (lineno, E)
	print s.replace('\'', '')
