#!/usr/bin/env python
import sys

def main(argv=None):
	if argv is None:
		argv = sys.argv
	
	T = int(sys.stdin.readline())
	for t in xrange(T):
		buf = sys.stdin.readline().rstrip("\n").split(" ")
		maxShyness = int(buf[0])
		shyGuys = map(int, list(buf[1]))
		friends = 0

		for i in xrange(1, maxShyness + 1):
		  deficit = i - sum(shyGuys[:i])
		  if deficit >= 1:
		    shyGuys[0] += deficit
		    friends += deficit
		
		print "Case #%d: %d" % (t + 1, friends)

if __name__ == "__main__":
	sys.exit(main())

