import math


def top(r):
	return math.pi * r * r


def side(r, h):
	return 2 * math.pi * r * h


def solve(n, k, cakes):
	covered = 0
	selected = [False] * len(cakes)
	total = 0
	for i in range(k):
		max_c = 0
		max_i = -1
		for c_i, c in enumerate(cakes):
			if selected[c_i]:
				continue
			r, h = c
			atop = top(r)
			aside = side(r, h)
			atop = max(0, atop - covered)
			ac = atop + aside
			if ac > max_c:
				max_c = ac
				max_i = c_i
		selected[max_i] = True
		total += max_c
		covered = max(top(cakes[max_i][0]), covered)
	return total


if __name__ == '__main__':
	T = int(input())
	for t in range(1, T+1):
		N, K = input().split()
		N = int(N)
		K = int(K)
		Cakes = []
		for i in range(N):
			Cakes.append([int(p) for p in input().split()])
		ans = solve(N, K, Cakes)
		print("Case #%s: %s" % (t, ans))
