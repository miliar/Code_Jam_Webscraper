#!/usr/bin/env python

import sys

def main():
	with open(sys.argv[1]) as f:
		solve(f)

def solve(f):
	lines = f.readlines()
	T = int(lines[0])
	for i in range(1, T+1):
		N, K = map(int, lines[i].split())
		answer = solve_real(N, K)
		print "Case #%d: %s" % (i, answer)

def solve_real(N, K):
	base = 2**N
	if (K % base) == base-1:
		return "ON"
	else:
		return "OFF"

if __name__ == '__main__':
	main()