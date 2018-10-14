import functools
import sys
from bisect import bisect_left

def f1(a, b):
	# return 0
	n = len(a)
	j = 0
	ret = -1
	for i in range(n):
		while (j < n) and (a[i] > b[j]):
			j += 1
		ret = max(ret, i - j)

	return n - 1 - ret

def f2(a, b):
	n = len(a)
	l, r = 0, n
	ret = 0
	for x in a[::-1]:
		if x > b[r - 1]:
			ret += 1
			l += 1
		else:
			r -= 1
	return ret

def one_test():
	n = int(input())
	a = sorted(map(float, input().split()))
	b = sorted(map(float, input().split()))

	return str(f1(a, b)) + " " + str(f2(a, b))

t = int(input())
for i in range(1, t + 1):
	print("Test {}".format(i), file = sys.stderr)
	print("Case #{}: {}".format(i, one_test()))