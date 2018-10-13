#!/usr/bin/env python
# encoding: utf-8
"""
Denis Sokolov
Google Code Jam 2010
"""

def solve(n, k):
	a = str(bin(k))
	if len(a)-2 >= n:
		for i in xrange(1, n+1):
			if a[-i] == '0':
				return 'OFF'
		return 'ON'
	return 'OFF'

def main():
	with open('A-large.in') as f:
		t = int(f.readline())
		for case in range(t):
			n, k = map(int, f.readline().split(' '))
			print 'Case #%d: %s' % (case + 1, solve(n, k))

if __name__ == '__main__':
	main()
