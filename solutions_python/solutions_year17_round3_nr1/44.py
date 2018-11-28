from math import pi

import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

cnt_tests = int(input())
for test in range(cnt_tests):
	n, k = list(map(int, input().split()))
	cakes = []
	for i in range(n):
		cakes.append(list(map(int, input().split())))


	cakes.sort(key=lambda cake: -cake[0])

	def plus_height(cake):
		return pi * cake[0] * 2 * cake[1]

	def plus_circle(cake):
		return pi * cake[0] * cake[0]

	dp = []
	for i in range(k + 1):
		dp.append((0, 0))
	dp[1] = (plus_circle(cakes[0]), plus_height(cakes[0]))

	for i in range(1, n):
		prev = []
		for obj in dp:
			prev.append((obj[0], obj[1]))
		for j in range(1, k + 1):
			if j == 1:
				if prev[j][0] + prev[j][1] < plus_circle(cakes[i]) + plus_height(cakes[i]):
					dp[j] = plus_circle(cakes[i]), plus_height(cakes[i])
			else:
				if prev[j][0] + prev[j][1] < prev[j - 1][0] + prev[j - 1][1] + plus_height(cakes[i]):
					dp[j] = prev[j - 1][0], prev[j - 1][1] + plus_height(cakes[i])

				
	print('Case #%d: %.10f' % (test + 1, sum(dp[k])))
