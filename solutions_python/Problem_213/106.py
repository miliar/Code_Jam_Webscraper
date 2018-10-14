#! /usr/bin/python

T = int(raw_input())

for t in range(1, T+1):

	N, C, M = [int(inp) for inp in raw_input().split()]
	counts = [[0 for i in range(N)] for j in range(C)]
	for _ in range(M):
		p, b = [int(inp) for inp in raw_input().split()]
		counts[b - 1][p - 1] += 1

	sum0 = sum(counts[0])
	sum1 = sum(counts[1])
	minRides = counts[0][0] + counts[1][0]

	totalRides = max(sum0, sum1, minRides)

	counts[0] += [max(sum1 - sum0, 0)]
	counts[1] += [max(sum0 - sum1, 0)]

	maxMatch = max([counts[0][i] + counts[1][i] - totalRides for i in range(N + 1)])

	promotions = max(maxMatch, 0)

	print 'Case #' + str(t) + ': ' + str(totalRides) + ' ' + str(promotions)