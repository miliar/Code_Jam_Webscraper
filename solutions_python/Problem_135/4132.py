# coding: utf-8

import os, sys, re, string
import math,random

def main():
	T = int(sys.stdin.readline())
	for i in xrange(T):
		first = int(sys.stdin.readline())
		cards = [[int(x) for x in sys.stdin.readline().split(' ')] for y in xrange(4)]
		second = int(sys.stdin.readline())
		cards2 = [[int(x) for x in sys.stdin.readline().split(' ')] for y in xrange(4)]

		fc = cards[first - 1]
		sc = cards2[second - 1]
		s = set(fc).intersection(set(sc))

		if len(s) == 1:
			print 'Case #%d: %d' % (i + 1, s.pop())
		elif len(s) == 0:
			print 'Case #%d: Volunteer cheated!' % (i + 1)
		else:
			print 'Case #%d: Bad magician!' % (i + 1)


if __name__ == '__main__':
	main()


