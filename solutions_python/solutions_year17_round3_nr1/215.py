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


t = int(raw_input())

for i in range(1, t + 1):
	N, K = map(int, raw_input().split())
	cake = [None] * N
	for j in range(N):
		cake[j] = map(int, raw_input().split())

	print("Case #%d: %f" % (i, solve(N, K, cake)))
