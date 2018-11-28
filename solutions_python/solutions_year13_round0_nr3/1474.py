#!/usr/bin/env python

from sys import stdin
from math import sqrt, ceil, floor

def is_palidrome(n):
	chars = list(str(n))
	x = 0
	y = len(chars) - 1
	while x <= y:
		if chars[x] != chars[y]:
			return False
		x = x + 1
		y = y - 1
	return True

num_cases = int(stdin.readline().rstrip())

for case in range(num_cases):
	urange = stdin.readline().rstrip().split(" ")
	low = int(urange[0])
	high = int(urange[1])

	fs = 0

	# Only look at numbers within the range that are squares
	low_sqrt = int(ceil(sqrt(low)))
	high_sqrt = int(floor(sqrt(high)))
	#print(low, high)
	#print(low_sqrt, high_sqrt)
	for num_sqrt in range(low_sqrt, high_sqrt + 1):
		num = num_sqrt ** 2
		pal = is_palidrome(num)
		spal = is_palidrome(num_sqrt)
		#print num, num_sqrt, pal, spal

		if pal and spal:
			fs = fs + 1

	print("Case #{}: {}".format(case + 1, fs))

