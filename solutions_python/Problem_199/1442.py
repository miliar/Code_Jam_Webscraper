from functools import reduce

ntc = int(input())

for tc in range(ntc):
	s, k = input().split()
	k = int(k)

	arr = list(s)
	n = len(arr)

	ans = 0
	for idx in range(n-k+1):
		if arr[idx] == '-':
			for j in range(idx, idx+k):
				arr[j] = '+' if arr[j] == '-' else '-'
			ans += 1

	possible = reduce(lambda acc, c: acc and c == '+', arr)

	print('Case #{}: '.format(tc+1), end='')
	if possible:
		print(ans)
	else:
		print('IMPOSSIBLE')