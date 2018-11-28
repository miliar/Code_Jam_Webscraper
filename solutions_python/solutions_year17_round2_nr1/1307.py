#!/usr/bin/env python3

tc = int(input().strip())

for t in range(tc):
	d, n = map(int, input().strip().split())


	slower = 0
	for h in range(n):
		k, s = map(int, input().strip().split())
		slower = max(slower, (d-k)/s)

	print('Case #{}: {:.6f}'.format(t+1, d/slower))

