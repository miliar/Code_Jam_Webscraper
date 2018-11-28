import sys


def solve(s_max, digits):

	num_needed = 0
	s = 0
	for k in range(s_max+1):
		n = int(digits[k])
		num_needed = max(num_needed, k - s)
		s += n

	return num_needed


# main

T = int(sys.stdin.readline())
i = 1
while i <= T:
	d = sys.stdin.readline().split()
	s_max = int(d[0])
	digits = d[1]

	print("Case #%d: %d" % (i, solve(s_max, digits)))
	i += 1