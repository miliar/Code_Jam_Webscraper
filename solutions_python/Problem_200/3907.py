import os
import sys


def cases():
	count = int(sys.stdin.readline())
	for i in range(count):
		yield (i + 1, int(sys.stdin.readline()))

def last_tidy(num):
	digits = list(str(num))

	for i, digit in reversed(list(enumerate(digits))):
		if i == len(digits) - 1: continue

		d1 = int(digit)
		d2 = int(digits[i + 1])

		if d1 > d2:
			digits[i] = str(d1 - 1)
			
			for i2 in range(i + 1, len(digits)):
				if digits[i2] == "9": break
				
				digits[i2] = "9"

	start = None
	for i, d in enumerate(digits):
		if d != "0":
			start = i
			break;

	return "".join(digits[start:])

for i, case in cases():
	print "Case #%d: %s" % (i, last_tidy(case))
	# break