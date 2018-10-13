#!/usr/bin/python

import sys, os, string, re

def get_next(s):
	digits = []
	for ch in s:
		digits.append(int(ch))
	n = len(digits)
	pos = -1
	for i in range(n-1, -1, -1):
		for j in range(n-1, i, -1):
			if digits[j] > digits[i]:
				if pos == -1 or digits[j] < digits[pos]:
					pos = j
		if pos != -1:
			t = digits[i]
			digits[i] = digits[pos]
			digits[pos] = t
			pos = i
			break
	if pos == -1:
		return -1
	(head, tail) = (digits[:pos+1], digits[pos+1:])
	tail.sort()
	digits = head+tail
	ret = 0
	for digit in digits:
		ret = 10*ret+digit
	return ret

in_file = sys.stdin
T = int(in_file.readline())
for case_num in range(T):
	s = in_file.readline().strip()

	answer = get_next(s)
	if answer == -1:
		answer = get_next('0'+s)
	
	print('Case #'+str(case_num+1)+': '+str(answer))
