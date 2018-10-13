import sys
import re

file = open(sys.argv[1])
T = None
Case = 1

def checkTidy(number):
	tmp = str(number)
	if len(tmp) == 1:
		return -1
	for i in range(1, len(tmp)):
		if tmp[i - 1] > tmp[i]:
			return i - 1
	return -1

for row in file:
	if T is None:
		T = int(row)
		continue
	N = int(row)

	while 1:
		check = checkTidy(N)
		if check == -1:
			result = N
			break
		else:
			tmp = str(N)
			if tmp[check] == '0':
				result = int('9' * (len(tmp) - 1))
				break
			else:
				tmp__ = list(tmp)
				tmp__[check] = str(int(tmp__[check]) - 1)
				tmp__[check+1:] = len(tmp__[check+1:]) * '9'
				N = int(''.join(tmp__))

	print("Case #%d: %d" % (Case, result))
	Case = Case + 1
	T = T - 1
	if T == 0:
		break
