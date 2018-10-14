import decimal

def solve():
	inp = raw_input().split()
	C = decimal.Decimal(inp[0])
	F = decimal.Decimal(inp[1])
	X = decimal.Decimal(inp[2])
	ans = decimal.Decimal("0")
	EPS = decimal.Decimal("0.0000001")
	r = decimal.Decimal("2.0")
	tt= decimal.Decimal()
	m = 1
	tt = X*F - C*F
	while (tt-r*C> EPS):
		ans += C/r
		r = 2 + m*F
		m += 1
	ans += X/r
	return ans

def main():
	T = int(raw_input())
	for i in xrange (1,T+1):
		ans = decimal.Decimal()
		ans = solve()
		print "Case #" + str(i) + ":", ans
main()
