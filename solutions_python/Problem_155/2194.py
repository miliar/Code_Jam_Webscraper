#!/usr/bin/python

import sys

def solve(S,x):
	s = 0
	r = 0
	for i in xrange(len(x)):
		d = i-s if s < i else 0
		s = s+int(x[i])+d
		r = r+d
	return r

if __name__ == '__main__':
	lines = [line for line in sys.stdin]
	N = int(lines[0])
	for i in xrange(N):
		line = lines[i+1]
		S, s = line.strip().split(' ')
		print 'Case #%s: %s' % (i+1, solve(S,s))

