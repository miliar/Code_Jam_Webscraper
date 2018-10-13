# coding: utf-8

import os, sys, re, string
import math,random


def check(x):
	tmp, rev = x, 0
	while tmp > 0:
		d = tmp % 10
		rev = rev * 10 + d
		tmp /= 10
	result = x == rev
	return result
	

def all_solve(b):
	s = 1
	targets = []
	while True:
		value = s * s
		s += 1
		if value > b:
			break
		if check(value) and check(s - 1):
			targets.append(value)
	return targets	
	
def solve(a, b, targets):
	return len(filter(lambda x: a <= x and x <= b, targets))

def main():
	targets = all_solve(100000000000000)
	t = int(sys.stdin.readline())
	for i in xrange(1, t + 1):
		a, b = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
		print "Case #%d: %d" % (i, solve(a, b, targets))

if __name__ == '__main__':
	main()


