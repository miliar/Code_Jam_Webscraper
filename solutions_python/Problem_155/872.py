T = int(input())

for case in range(1, T+1):
	s = input().split(' ')[1]
	s = [int(x) for x in s]
	pSum = [0 for x in s]
	ans = 0
	for i in range(1, len(pSum)):
		pSum[i] = pSum[i-1] + s[i-1]
		ans = max(ans, i-pSum[i])
	print('Case #', case, ': ', ans, sep='')