from math import log
from fractions import gcd
file = open('input', 'r')

problems = int(file.readline())

for z in range(1, problems+1):
	values = file.readline().split("/")
	P = float(values[0])
	Q = float(values[1])
	g = gcd(P, Q)
	Q = Q / g
	P = P / g
	if log(Q)/log(2) % 1 == 0:
		quot = P / Q
		count = 1
		while quot < 0.5:
			quot = quot * 2
			count += 1
		print 'Case #' + str(z) + ': ' + str(count)
	else:
		print 'Case #' + str(z) + ': impossible'

