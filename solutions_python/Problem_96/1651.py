#!/usr/bin/env python
import sys

def main(argv=None):
	if argv is None:
		argv = sys.argv
	
	T = int(sys.stdin.readline())
	for i in xrange(T):
		sin = map(int, sys.stdin.readline().split(" "))
		N = sin[0]
		S = sin[1]
		p = sin[2]
		t = sin[3:]

		# If t_i = 3p - 2, then it may or may not be suprising. Let this be the
		# `cut'-off total score. If t_i = 3p - 3 or 3p - 4, then it is suprising,
		# or it is not surprising with best result less than p.
		Scut = 3 * p - 2
		cutcount = 0
		Scount = 0
		
		# Maximum number with best result p.
		m = 0

		# Trivial case.
		if p == 0:
			m = N
		else:
			for s in t:
				if s > Scut:
					m += 1
				elif s == Scut:
					cutcount += 1
				# To maximise m, if there are surprising numbers remaining, then we
				# include total scores just below the cut-off total score.
				elif s > 0 and s >= Scut - 2 and Scount != S:
					m += 1
					Scount += 1
			m += cutcount
		
		print "Case #%d: %d" % (i + 1, m)

if __name__ == "__main__":
	sys.exit(main())

