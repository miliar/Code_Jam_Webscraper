#!/usr/bin/python

import sys
rl = sys.stdin.readline

def fake_sum(args):
	return reduce(lambda x, y: x ^ y, args)

if __name__ == '__main__':
	tests = int(rl())

	for case in xrange(1, tests + 1):
		rl()
		pile, result = sorted(map(int, rl().split())), 0

		if fake_sum(pile):
			result = 'NO'
		else:
			for x in xrange(1, len(pile)):
				a, b = pile[x:], pile[:x]

				if fake_sum(a) == fake_sum(b):
					result = max([result, sum(a), sum(b)])

		print 'Case #%d: %s' % (case, result)

