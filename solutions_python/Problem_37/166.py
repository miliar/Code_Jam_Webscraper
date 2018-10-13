#!/usr/bin/python2

import sys, os, string, re

def make_digits(x, base):
	digits = []
	mask = 1
	while (x > 0):
		rem = x%(mask*base)
		digits.append(rem/mask)
		x -= rem
		mask *= base
	return digits

def happy_base(cand, base):
	x = cand
	seen = []
	while True:
		if x in seen:
			return False
		seen.append(x)
		digits = make_digits(x, base)
		sum = 0
		for digit in digits:
			sum += digit**2
		sum_digits = make_digits(sum, base)
		check_sum = 0
		for digit in sum_digits:
			check_sum += digit
		if check_sum == 1:
			return True
		x = sum

in_file = sys.stdin
T = int(in_file.readline())
for case_num in range(T):
	groups = in_file.readline().strip().split()
	bases = []
	for group in groups:
		bases.append(int(group))

	cand = 1
	while True:
		cand += 1
		happy = True
		for base in bases:
			if not happy_base(cand, base):
				happy = False
				break
		if happy:
			break
	
	print 'Case #%d: %d' % (case_num+1, cand)
