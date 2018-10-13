import sys
from fractions import Fraction

T = int(sys.stdin.readline())
for t in range(1,T+1):
	print "Case #%d:" % t,

	P, Q = [int(x) for x in sys.stdin.readline().split('/')]
	for g in range(1, 40+1):
		F = Fraction(P, Q)
		E = Fraction(1, 2 ** g)
		if F < E:
			continue
		F -= Fraction(1, 2 ** g)
		if (2 ** (40-g)) % F.denominator == 0:
			print g
			break
	else:
		print "impossible"

