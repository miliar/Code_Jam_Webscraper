#!/usr/bin/env python3

import sys

def solve(line, t):
	pan, K = line.split(" ")
	pan = list(pan)
	K = int(K)
	N = len(pan)
	sol = 0
	for i in range(N-K+1):
		if pan[i] == "-":
			sol += 1
			for j in range(K):
				pan[i+j] = "+" if pan[i+j] == "-" else "-"
	for i in range(K-1):
		if pan[N-i-1] == '-':
			sol = "IMPOSSIBLE"
	
	print("Case #%d: %s" % (t, str(sol)))


lines = [ l.strip() for l in sys.stdin.readlines() ]

T = int(lines[0])

for i in range(T):
	solve(lines[i+1], i+1)
