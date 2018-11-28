#!/usr/bin/env python
import sys, math

def main(argv=None):
	if argv is None:
		argv = sys.argv
	
	T = int(sys.stdin.readline())
	for c in xrange(T):
		r, t = map(long, sys.stdin.readline().split(" "))

		rings = long((-2.0 * r - 3.0 + math.sqrt(((4.0 * r * r) - (4.0 * r) + 1.0)
				+ 8.0 * (t)) ) / 4.0) + 1

		print "Case #%d: %s" % (c + 1, rings)

if __name__ == "__main__":
	sys.exit(main())

