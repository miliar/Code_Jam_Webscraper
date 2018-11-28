#!/usr/bin/env python3

import sys
import math

lines = [ l.strip() for l in sys.stdin.readlines() ]

T = int(lines[0])
j = 1
for t in range(T):
	N, P = map(int, lines[j].split(' '))
	G = list(map(int, lines[j+1].split(' ')))
	j += 2

	if P == 2:
		G.sort(key=lambda a: a % 2)
		sol = 0
		delta = 0
		for i in G:
			if i % 2 == 0:
				sol += 1
				continue
			if delta == 0:
				sol += 1
			delta = (delta + i) % 2
		print("Case #%d: %d" % (t+1, sol))

	if P == 3:
		MOD0 = list(filter(lambda x: x % 3 == 0, G))
		MOD1 = list(filter(lambda x: x % 3 == 1, G))
		MOD2 = list(filter(lambda x: x % 3 == 2, G))

		if len(MOD1) == len(MOD2):
			sol = len(MOD0) + len(MOD1)
		if len(MOD1) > len(MOD2):
			sol = len(MOD0) + len(MOD2) + (len(MOD1) - len(MOD2)+2) / 3
		if len(MOD1) < len(MOD2):
			sol = len(MOD0) + len(MOD1) + (len(MOD2) - len(MOD1)+2) / 3
		print("Case #%d: %d" % (t+1, sol))
