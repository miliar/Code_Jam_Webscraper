#!/usr/bin/python

import sys, re, string, math

def c(n, r):
	if n * r == 0:
		return 1
	else:
		return c(n, r - 1) * (n - r + 1) / r

def calc(i, k, n):
	if k == n:
		return 1
	if 2 * k - i >= n + 1:
		return 0
	
	s = 0
	for k2 in range(2 * k - i, n + 1):
		s += c(k2 - k - 1, k - i - 1) * calc(k, k2, n)
	
	return s

def do_one_case(cnum):
	(n) = int(sys.stdin.readline())
	ans = calc(0, 1, n)
	print "Case #%d: %d" % (cnum, ans % 100003)


def main():
	T = int(sys.stdin.readline().strip())
	for i in range(T):
		do_one_case(i+1)


if __name__ == "__main__":
	main()
