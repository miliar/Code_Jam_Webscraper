import sys

def one_test():
	c, f, x = map(lambda s: float(s) / 2, input().split())
	def ans(k):
		return c * sum(1 / (1 + f * i) for i in range(k)) + x / (1 + f * k)

	if x <= c:
		return x
	# ans(k + 1) - ans(k) = a * k + b
	a = c * f
	b = c * f + c - f * x
	opt_k = -b / a
	if opt_k < 0:
		return ans(0)

	int_k = int(opt_k)
	# return int_k
	return min(ans(i) if i >= 0 else x for i in range(int_k - 5, int_k + 6))

t = int(input())

for i in range(1, t + 1):
	print("Test {}".format(i), file = sys.stderr)
	print("Case #{}: {}".format(i, one_test()))
