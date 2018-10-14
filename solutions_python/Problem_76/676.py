# coding: utf8

import os, sys, re, string

def solve(N, c):
	t = 0
	for v in c:
		t ^= v
	if t != 0:
		return 'NO'
	m = min(c)
	s = sum(c)
	return s - m

def main():
	T = int(sys.stdin.readline())
	for i in xrange(T):
		N = int(sys.stdin.readline())
		c = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
		print 'Case #%d: %s' % (i + 1, solve(N, c))

if __name__ == '__main__':
	main()


