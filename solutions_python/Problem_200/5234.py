import sys, re


def isTidy(value):
	array = list(str(value))
	i = 0
	while (i < len(array)-1):
		if (int(array[i]) > int(array[i+1])):
			return 0
		i+= 1
	return 1

case = 0
for line in sys.stdin:
	if case == 0:
		numCases = line
		case = 1
		continue

	value = int(line)
	while (not isTidy(value)):
		value -= 1
	print("Case #" + str(case) + ": " + str(value))
	case += 1


