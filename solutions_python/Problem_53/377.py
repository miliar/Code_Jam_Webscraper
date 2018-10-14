#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Google Code Jam: Qualification Round 2010
# Problem A: Snapper Chain

T = int(input()) # number of test cases

for t in range(1,T+1):
	print('Case #{0}: '.format(t), end='')
	N,K = [ int(x) for x in input().split(' ') ]

	# para estar encendida la bombilla, K ha de ser un número de la forma
	# K mod (2^N) = 1

	K -= (2**N) -1
	if K >= 0 and K%(2**N) == 0:
		print('ON')
	else:
		print('OFF')

