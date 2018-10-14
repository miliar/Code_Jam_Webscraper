import math

t_no = int(input())

for t in range(1, t_no + 1):
	n, q = [int(x) for x in input().split()]
	
	e = [0] * n
	s = [0] * n
	for i in range(n):
		e[i], s[i] = [int(x) for x in input().split()]
	
	d = [None] * n
	for i in range(n):
		d[i] = [int(x) for x in input().split()]
	
	u = [0] * q
	v = [0] * q
	for i in range(q):
		u[i], v[i] = [int(x) for x in input().split()]
		u[i] -= 1
		v[i] -= 1

	d_sum = [0] * n
	for i in range(1, n):
		d_sum[i] = d_sum[i-1] + d[i-1][i]
	
	memo = {}
	def f(i, horse):
		if i == n - 1:
			return 0
		if (i, horse) in memo:
			return memo[(i, horse)]
		if d_sum[i+1] - d_sum[horse] > e[horse]:
			memo[(i, horse)] = math.inf
		else:
			memo[(i, horse)] = d[i][i+1] / s[horse] + min(f(i+1, i+1), f(i+1, horse))
		return memo[(i, horse)]

	print("Case #{}: {}".format(t, f(0, 0)))
