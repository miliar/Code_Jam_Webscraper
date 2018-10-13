def distance(cores, u):
	s = 0
	for c in cores:
		if c < u:
			s += u - c
	return s


def distribute_core(cores, u):
	cores = sorted(cores)
	lb = cores[0]
	ub = 1
	mid = (lb + ub) / 2
	diff = distance(cores, mid)
	while abs(diff - u) > 1e-7:
		if diff > u:
			ub = mid
		else:
			lb = mid
		mid = (lb + ub) / 2
		diff = distance(cores, mid)
	for i, c in enumerate(cores):
		if c < mid:
			cores[i] = mid
	return cores


def solve(n, k, u, cores):
	if (len(cores) - k) % 2:
		cores = sorted(cores, reverse=True)
		for i, c in enumerate(cores):
			c = min(c + u, 1)
			u += cores[i] - c
			cores[i] = c
	else:
		cores = distribute_core(cores, u)
	result = 1
	for i in cores:
		result *= i
	return result


t = int(raw_input())

for i in range(1, t + 1):
	N, K = map(int, raw_input().split())
	P = float(raw_input())
	arr = map(float, raw_input().split())
	print("Case #%d: %f" % (i, solve(N, K, P, arr)))
