t=int(input())
for i in range(1, t+1):
	n, k = map(int, input().split())
	k += 1
	ans = bool(k and not (k % (1 << n)))
	print('Case #{0}: {1}'.format(i, 'ON' if ans else 'OFF'))