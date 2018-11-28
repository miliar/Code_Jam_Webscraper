import codejam
from math import *

for (number, line) in enumerate(codejam.input("C")):
	(n, k) = map(int, line.split(" "))
	l = ceil(log2(k + 1) - 1)
	space = n
	(s, smaller, larger) = (n, 1, 0)
	for i in range(l):
		space = (space - 1) // 2
		if s % 2 == 0:
			larger = smaller + 2 * larger
		else:
			smaller = 2 * smaller + larger
		s = (s - 1) // 2
	larger = 2 ** l - smaller
	if k - 2 ** l < larger:
		space += 1
	codejam.case(str(space // 2), str((space - 1) // 2))

codejam.finish()