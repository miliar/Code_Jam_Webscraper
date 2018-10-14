#!/usr/bin/env python

import sys

def solve(raw):
	_, seq = raw.strip().split(' ')
	n = ret = 0
	for i in xrange(len(seq)):
		num = int(seq[i])
		if i > n:
			ret += i - n
			n = i
		n += num
	return ret

if __name__ == '__main__':
	result = map(solve, sys.stdin.readlines()[1:])
	for i in xrange(len(result)):
		print 'Case #%d: %d' % (i + 1, result[i])
