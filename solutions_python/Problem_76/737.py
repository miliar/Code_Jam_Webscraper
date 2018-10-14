#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

ans = []

def p_add(x, y):
	return (x | y) & (~(x & y))

def solve(c, sean):
	sum_sean = 0
	sum_patrick = 0
	sum_true = 0
	for i in range(len(c)):
		if sean[i]:
			sum_sean = p_add(sum_sean, c[i])
			sum_true += c[i]
		else:
			sum_patrick = p_add(sum_patrick, c[i])
	if sum_sean == sum_patrick and sum_true != 0 and sum_true != sum(c):
		global ans
		ans.append(sum_true)

def solve_recursion(n, c, sean):
	if n < len(c):
		sean[n] = True
		solve_recursion(n+1, c, sean)
		sean[n] = False
		solve_recursion(n+1, c, sean)
	else:
		solve(c, sean)

def solve_c(infile):
	global ans
	f = open(infile)
	ntest = int(f.readline())
	for i in range(ntest):
		ans = []
		n = int(f.readline())
		c = map(int, f.readline().rstrip().split())
		sean = [False] * n
		solve_recursion(0, c, sean)
		if ans:
			print "Case #%d: %d" % (i+1, max(ans))
		else:
			print "Case #%d: NO" % (i+1)

def main():
	if len(sys.argv) > 1:
		solve_c(sys.argv[1])
	else:
		print "no input file."

if __name__ == '__main__':
	sys.setrecursionlimit(2000)
	main()

