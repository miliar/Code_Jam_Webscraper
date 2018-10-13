from fractions import Fraction as F
T = input()
for t in xrange(T):
	N, P_D, P_G = map(int, raw_input().split())
	div = F(P_D, 100).denominator
	result = "Possible" if div <= N else "Broken"
	if P_G == 100 and P_D < 100 or P_G == 0 and P_D > 0: result = "Broken"
	print "Case #%d: %s" % (t + 1, result)
