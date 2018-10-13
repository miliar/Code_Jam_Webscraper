# -*- coding: utf-8 -*-

def solve():
	N, K = map(int, input().split())
	lo = 0
	hi = int(K ** 0.5 + 10)
	while hi - lo > 1:
		mid = (hi + lo) // 2
		sum = (1 << mid) - 1
		if K <= sum:
			hi = mid
		else:
			lo = mid
	used = (1 << lo) - 1
	rest = K - used
	vacant = N - used
	r, q = divmod(vacant, 2 ** lo)
	c = r + 1 if rest <= q else r
	return (c // 2, (c - 1) // 2)


T = int(input())
for i in range(0, T):
	max, min = solve()
	print(f'Case #{i+1}: {max} {min}')

