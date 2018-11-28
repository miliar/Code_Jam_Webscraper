#!/usr/bin/python3

from math import log

lines = int(input())

for attempt in range(1,lines+1):
	N = int(input())
	digits = int(log(N, 10))

	for place in range(0,digits+1):
		digit = (N % (10 ** (place + 1)) // (10 ** place))
		next_digit = (N % (10 ** (place + 2)) // (10 ** (place + 1)))
		if digit < next_digit:
			N -= (N % (10 ** (place + 1)) + 1)
	
	print('Case #' + str(attempt) + ': ' + str(N))
