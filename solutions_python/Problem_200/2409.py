#!/usr/bin/env python
import re

raw = int(raw_input())

def rollOut(number):
	n = int(number)
	multiplier = 1
	pos = 1
	digits = map(lambda x: x, str(n))
	is_increasing = sorted(digits)==digits

	while not is_increasing:
		n += 1*-multiplier
		digits = map(lambda x: x, str(n))
		is_increasing = sorted(digits)==digits
		
		if digits[-pos]=="9" :
			multiplier *= 10
			pos += 1

	return str(n)

for i in range(raw):
	print "Case #{}: {}".format(i+1, rollOut(raw_input()))
	