current = 0.0
rate = 2.0
C = 500.0
F = 4.0
X = 2000.0
def solve(C, F, X):
	current = 0.0
	rate = 2.0

	while True:
		time_to_farm = C/rate

		time_to_cookie = X/rate

		time_to_cookie_with_farm = time_to_farm + X/(rate + F)
		
		if time_to_cookie_with_farm < time_to_cookie:
			current += time_to_farm
			rate += F
		else:
			current += time_to_cookie
			break

	return current


with open('p2.in') as f:
	lines = [line.strip() for line in f.readlines()]

testcases = int(lines.pop(0))

for testcase in xrange(1, testcases + 1):

	C, F, X = (float(x) for x in lines.pop(0).split())

	print "Case #%d: %.7f" % (testcase, solve(C, F, X))
