def get_ans(n, k):
	if k == 1:
		if n % 2:
			return (n / 2, n / 2)
		else:
			return (n / 2, n / 2 - 1)
	if n == k:
		return (0, 0)
	if n % 2:
		return get_ans(n / 2, k / 2)
	else:
		if k % 2:
			return get_ans(n / 2 - 1, k / 2)
		else:
			return get_ans(n / 2, k / 2)

def solve(case_number):
	n, k = [int(s) for s in raw_input().split(" ")]
	x, y = get_ans(n, k)
	print "Case #{}: {} {}".format(case_number, x, y)

t = int(raw_input())  # read a line with a single integer
for case in xrange(1, t + 1):
	solve(case)

'''
python solution.py <small.in> small.out
python solution.py <large.in> large.out
'''