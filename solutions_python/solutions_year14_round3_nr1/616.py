def power_two(b):
	a = 1
	while a < b:
		a *= 2
	return a == b

def solve(a,b):
	if not power_two(b):
		return "impossible"
	if 2 * a >= b:
		return 1
	if b % 2 == 0:
		return solve(a, b/2) + 1
	

number_cases = int(raw_input())
for i in xrange(number_cases):
	a, b = [int(x) for x in raw_input().split("/")]
	print "Case #{}: {}".format(i+1, solve(a, b))