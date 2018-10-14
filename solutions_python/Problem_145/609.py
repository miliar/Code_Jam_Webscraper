import fractions, math

def trial():
	P, Q = [int(i) for i in raw_input().split('/')]
	gcd = fractions.gcd(P, Q)
	P = P/gcd
	Q = Q/gcd
	if (Q & (Q - 1)) != 0:
		return "impossible"
	return int(-math.floor(math.log(float(P)/Q, 2)))
	
	
T = int(raw_input())
for t in range(1, T+1):
	print "Case #%d:" % t,
	print trial()


