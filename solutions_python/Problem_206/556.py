#!/usr/bin/env python3

import sys

lines = [ l.strip() for l in sys.stdin.readlines() ]

T = int(lines[0])
i = 1
for t in range(T):
	D, N = map(int, lines[i].split(' '))
	i += 1

	res = 0
	
	for j in range(N):
		K, S = map(int, lines[i].split(' '))
		i += 1
		
		dest = (D-K)/S
		res = max(res, dest)

	print("Case #%d: %f" % (t+1, D/res))
