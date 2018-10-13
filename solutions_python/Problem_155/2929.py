import sys
from math import sqrt

sys.stdin = open('input.in')
sys.stdout = open('output.out', 'w')

case = 0
n_cases = input()

for line in sys.stdin:
	d = line.strip().split(' ')

	case = case + 1
	needed = 0
	stood = 0

	for i, val in enumerate(d[1], start=1):
		val = int(val)
		stood = stood + val

		if (i == 0):
			continue

		n_need = i - stood
		if (n_need > 0):
			needed = needed + n_need
			stood = stood + n_need

		if (stood > d[0]):
			break

	print 'Case #' + str(case) + ': ' + str(needed)
