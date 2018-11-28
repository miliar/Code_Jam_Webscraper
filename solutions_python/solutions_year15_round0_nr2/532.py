#!/usr/bin/env python

import sys
import os

def solve(D, P):
	ans = 10000000
	max_p = max(P)
	for n in range(max(P), 0, -1):
		d = 0
		for p in P:
			d += (p - 1) // n
		if ans > d + n:
			ans = d + n
	return ans

def main(args):
	f = file(args[1])
	T = int(f.readline().strip())
	for i in range(T):
		D = int(f.readline().strip())
		P = map(int, f.readline().strip().split())
		print "Case #%d: %d" % (i + 1, solve(D, P))

if __name__ == "__main__": main(sys.argv)
