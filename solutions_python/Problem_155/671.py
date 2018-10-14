#!/usr/bin/env python

import sys
import os

def solve(aud):
	ans = 0
	crap = 0
	n = 0
	for i in range(len(aud)):
		if i > crap:
			n = i - crap
			ans += n
		crap += aud[i] + n
	return ans

def main(args):
	f = file(args[1])
	N = int(f.readline().strip())
	for i, l in enumerate(f):
		smax, aud = l.strip().split()
		smax = int(smax)
		aud = map(int, aud)
		#print smax, aud
		print "Case #%d: %d" % (i + 1, solve(aud))

if __name__ == "__main__": main(sys.argv)
