# coding: utf-8

import os, sys, re, string
import math,random

def next_int():
	return int(sys.stdin.readline())
def next_ints():
	return map(int, sys.stdin.readline().split())


def solve(N, P):
	prized = [0] * (2 ** N)
	def f(ary):
		result = [[0, i] for i in xrange(len(ary))]
		for r in xrange(N):
			win, lose = [], []
			for i in xrange(0, len(ary), 2):
				x, y = ary[i], ary[i+1]
				if x < y:
					t = y
					y = x
					x = t
				if x > y:
					result[y][0] = (result[y][0] << 1) + 1
					result[x][0] <<= 1
					win.append(y)
					lose.append(x)
			ary = win + lose
		result.sort(lambda x, y: y[1] - x[1])
		for i in xrange(P):
			prized[result[i][0]] += 1	
	ary = [i for i in xrange(len(prized))]
	f(ary)
	a, b = 0, 0
	for i in xrange(1, len(prized)):
		if prized[0] == prized[i]:
			a = i
		else:
			break
	for i in xrange(1, len(prized)):
		if prized[i] > 0:
			b = i
	return a, b

def main():
	for i in xrange(next_int()):
		N, P = next_ints()
		result = solve(N, P)
		print "Case #%d: %d %d" % (i + 1, result[0], result[1])

if __name__ == '__main__':
	main()


