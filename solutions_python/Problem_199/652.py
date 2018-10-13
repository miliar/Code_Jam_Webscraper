T = int(input())
for t in range(1,T+1):
	arr, K = input().split()
	arr = list(arr)
	K = int(K)
	def swap(X):
		for x in range(len(X)):
			X[x] = '-' if X[x] == '+' else '+'
		return X	
	count = 0		
	for i in range(len(arr) - K + 1):
		if arr[i] == '-':
			arr[i:i+K] = swap(arr[i:i+K])
			count += 1
	
	answer = count if arr.count('+') == len(arr) else 'IMPOSSIBLE'				
	print('Case #{}: {}'.format(t,answer))