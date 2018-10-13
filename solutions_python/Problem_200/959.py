
ONES = [(10**(p+1) - 1)/9 for p in xrange(19)]

def solve(n):
	p, a = 0, n
	while a:
		a /= 10
		p += 1

	d = 1
	t = ONES[p-1]
	if n < t:
		p -= 1
		t = ONES[p-1]
	for p in xrange(p-1, -1, -1):
		ones = ONES[p]
		while d < 9 and t + ones <= n:
			d += 1
			t += ones
	return t


for t in range(int(raw_input())):
	n = int(raw_input().strip())
	print "Case #{}: {}".format(t+1, solve(n))
