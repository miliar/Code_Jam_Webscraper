# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import math

def f(n, k):
	i = int(math.floor(math.log(k,2)))
	k0 = 2 ** i
	delta_k = k - k0 + 1
	s = 2**i
	m = n - s + 1
	j, delta_m = divmod(m, s)
	if delta_k <= delta_m:
		return j + 1
	else:
		return j



t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	n, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
	l = f(n, k) - 1
	x = l // 2
	y = l - x
	print("Case #{}: {} {}".format(i, y, x))
	# check out .format's specification for more formatting options
