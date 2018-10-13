ntc = int(input())

for tc in range(ntc):
	s = input()
	arr = list(s)

	n = len(arr)
	# ..., 3, 2, 1
	for idx in range(n-1, 0, -1):
		if arr[idx-1] > arr[idx]:
			for j in range(idx, n):
				arr[j] = '9';
			arr[idx-1] = chr(ord(arr[idx-1])-1)

	ans = int(''.join(arr))

	print('Case #{}: '.format(tc+1), end='')
	print(ans)
