import sys
import math
import re
line_number = 0

RE_ONES = re.compile("^1+0.*$")

def isPowerOfTen (num):
	"Source: http://stackoverflow.com/a/15352628"
	testnum = 10
	while testnum < num:
		testnum = testnum * 10
	return testnum == num

def algo(line):
	"""
	7 -> 7
	124 -> 124
	132 -> 129
	999999999999999997 -> 899999999999999999
	899999999999999997 -> 799999999999999999
	789999999999999997 -> 788999999999999999
	78993 -> 78899
	"""
	line = line.rstrip()
	# special case: value in [1000,1110]
	if RE_ONES.match(line):
		return "9" * (len(line)-1)
	digits = list(line)
	digits.append("/") # since ASCII
	value = int(line)
	# step along input digits
	i = 0
	while digits[i] <= digits[i+1]:
		i += 1
	# now digits[i] is last tidy digit
	if (i+1) == len(line):
		return line # base case
	drop = int(line[i+1:]) + 1
	return algo(str(value - drop))

for line in sys.stdin:
	if line_number:
		x = algo(line)
		print("Case #%d: %s" % (line_number, x))
	line_number += 1
