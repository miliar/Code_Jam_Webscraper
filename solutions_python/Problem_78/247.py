from fractions import Fraction
import math

def solve(N, PD, PG):
	if PG == 1:
		return "Broken" if PD != 1 else "Possible"
	if PG == 0:
		return "Broken" if PD != 0 else "Possible"
		
	#print "%s %s %s" % (N, PD, PG)
	#times = 1
	if  PD.denominator <= N:
		return "Possible"
#		D = PD.denominator * times
#		won = PD.numerator * times		
#		tot = PG.numerator
#		G = PG.denominator
#		
#		if G > D:
#			A = G - D
#			B = tot - won
#			
#			if B < A:
#				return "Possible"
#		else:
#			frac = Fraction(D, G + 1)
#			mul = int(math.ceil(frac))
#
#			A = G * mul - D
#			B = tot * mul - won
#
#			print "D = %s, G = %s, W = %s, TW = %s" % (D, G *mul, won, tot * mul)
#			if B < A:
#				return "Possible"
#
#		times += 1
		
	return "Broken"
		
	
T = int(raw_input())
for case in xrange(1, T + 1):
	#print "Case %d" % case
	line = raw_input().split()
	N = int(line[0])
	PD = Fraction(int(line[1]), 100)
	PG = Fraction(int(line[2]), 100)
	ans = solve(N, PD, PG)
	print "Case #%d: %s" % (case, ans)