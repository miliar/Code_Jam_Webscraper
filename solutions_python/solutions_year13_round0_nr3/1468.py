import math
import sys

def isSquare(x):
	root = int(math.sqrt(x))
	return ((root * root) == x)

def isFair(x):
	return str(x) == str(x)[::-1]

case = -1

for line in sys.stdin:
	count = 0
	case = case + 1
	if case == 0:
		continue
	if len(line.strip()) == 0:
		break
	(start, finish) = [int(x) for x in line.split()]
	for x in range(start, finish+1):
		if isFair(x) and isSquare(x) and isFair(int(math.sqrt((x)))):
			count = count +1
	print "Case #{0}: {1}".format(case, count)

