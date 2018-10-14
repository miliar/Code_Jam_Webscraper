from collections import defaultdict

def solve():
	n = int(input())
	l = [set(input().split()) for _ in range(n)]
	prod = [[0] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			prod[i][j] = l[i] & l[j]
	ans = 1000000000
	for i in range(1 << (n - 2)):
		res = set(prod[0][1])
		for j in range(n - 2):
			if i & (1 << j):
				res |= prod[1][j + 2]
			else:
				res |= prod[0][j + 2]
		for j in range(n - 2):
			for k in range(n - 2):
				if ((i & (1 << j) and not i & (1 << k)) or
				    (not i & (1 << j) and i & (1 << k))):
					res |= prod[j + 2][k + 2]
		ans = min(ans, len(res))
	return ans

t = int(input())
for i in range(t):
	print('Case #{}: {}'.format(i + 1, solve()))
