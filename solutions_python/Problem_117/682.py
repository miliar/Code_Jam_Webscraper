#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from numpy import empty, array, reshape, zeros

def read_pattern(m,n):
	ar = array(map(int, sum([sys.stdin.readline().strip().split(' ') for a in range(m)],[])))

	return reshape(ar, (m,n))

def solve(n):
	m, n = map(int, sys.stdin.readline().split(' '))

	pattern = read_pattern(m,n)
	lawn = zeros((m,n), dtype=int)
	lawn.fill(100)

	# lines
	for j in range(m):
		if pattern[j,:].max() <= lawn[j,:].min():
			lawn[j,:] = lawn[j,:].clip(0, pattern[j,:].max())

	for j in range(n):
		if pattern[:,j].max() <= lawn[:,j].min():
			lawn[:,j] = lawn[:,j].clip(0, pattern[:,j].max())

	if (pattern == lawn).all():
		return True

	return False

if __name__ == "__main__":
	N = int(sys.stdin.readline())
	
	for n in range(N):
		if solve(n):
			print "Case #{n}: YES".format(n=n+1)
		else:
			print "Case #{n}: NO".format(n=n+1)
