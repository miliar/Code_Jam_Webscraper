#!/usr/bin/env python

import sys

def main():
	with open(sys.argv[1]) as f:
		solve(f)

def solve(f):
	lines = f.readlines()
	C = int(lines[0])
	for i in range(1, C+1):
		R, k, N = map(int, lines[2*i-1].split())
		g = map(int, lines[2*i].split())
		answer = solve_real(R, k, g)
		print "Case #%d: %s" % (i, answer)

def solve_real(R, k, g):
	r = 0
	for i in range(R):
		q, g = fill(k, g)
		r += q
	return r

def fill(k, g):
	rem = k
	seated = []
	while len(g):
		if g[0] > rem:
			break
		else:
			rem -= g[0]
			seated.append(g[0])
			g = g[1:]
	g = g + seated
	return k - rem, g

if __name__ == '__main__':
	main()