import itertools


def in_nums():
	return [int(p) for p in input().split()]


def in_float():
	return [float(p) for p in input().split()]


def comp(cores, k):
	ans = 1
	for c in cores:
		ans *= c
	return ans
	# print('comp')
	failure = [1 - c for c in cores]
	ids = [i for i in range(len(cores))]
	total_f = 0
	for n in range(len(cores) - k + 1, len(cores) + 1):
		for p in itertools.combinations(ids, n):
			print(p)
			# print('here')
			cur = 1
			for i in p:
				cur *= failure[i]
			for i in ids:
				if i not in p:
					cur *= cores[i]
			total_f += cur
	return max(1 - total_f, 0)


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
		# print('mid', mid)
	for i, c in enumerate(cores):
		if c < mid:
			cores[i] = mid
	return cores


def solve(n, k, u, cores):
	if (len(cores) - k) % 2:
		cores = sorted(cores, reverse=True)
		# apart
		for i, c in enumerate(cores):
			c = min(c + u, 1)
			u += cores[i] - c
			cores[i] = c
	else:
		cores = distribute_core(cores, u)
		# print(cores)
	# print(cores)
	return comp(cores, k)


if __name__ == '__main__':
	T = int(input())
	for t in range(1, T+1):
		N, K= in_nums()
		U = in_float()[0]
		Cores = in_float()
		ans = solve(N, K, U, Cores)
		print("Case #%s: %s" % (t, ans))
