import math

pancakes = []

def height(i):
	return 2*pancakes[i][0]*pancakes[i][1]

def area(i):
	return pancakes[i][0]**2 + height(i)

T = int(raw_input())
for t in range(T):
	N, K = map(int, raw_input().split())
	pancakes = sorted([
		map(int, raw_input().split())
		for _ in range(N)
	], reverse=True)

	dp = [[-1 for _ in range(N)] for _ in range(K)]

	for j in range(N):
		dp[0][j] = area(j)

	for i in range(1, K):
		val = max([dp[i-1][x] for x in range(i)])
		for j in range(i, N):
			dp[i][j] = max(val+height(j), dp[i][j-1])
			val = max(val, dp[i-1][j])

	print 'Case #%d: %.9f' % (t+1, math.pi * max(dp[K-1]))


#   1 2
# 1 x -
# 2 x x
# 3 x x

