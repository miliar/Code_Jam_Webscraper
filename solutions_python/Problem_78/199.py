# coding: utf8

import os, sys, re, string

def calc(N, Pd, Pg):
	if Pd == 0 and Pg == 0:
		return 'Possible'
	if (Pg == 100 and Pd < 100) or (Pg == 0 and Pd > 0) or (Pd == 0 and Pg > 0):
		return 'Broken'
	for D in xrange(1, N+1):
		xmin, xmax = 0, D
		for i in xrange(7):
			xc = (xmin + xmax) / 2
			v = xc * 100 / D
			if v < Pd:
				xmin = xc
			elif v > Pd:
				xmax = xc
			else:
				break
		if len(filter(lambda x: x * 100 % D == 0 and x * 100 / D == Pd, xrange(xmin, xmax + 1))) > 0:
			return 'Possible'
	return 'Broken'

def main():
	T = int(sys.stdin.readline())
	for i in xrange(1, T+1):
		N, Pd, Pg = map(int, sys.stdin.readline().split(" "))
		print "Case #%d: %s" % (i, calc(N, Pd, Pg))

if __name__ == '__main__':
	main()


