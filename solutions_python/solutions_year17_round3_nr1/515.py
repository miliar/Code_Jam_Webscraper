import sys
import math

# sys.stdin = open("D:\\Computer\\TestingArea\\test.in", "r")
# sys.stdout = open("D:\\Computer\\TestingArea\\test.out", "w")

# sys.stdin = open("A-large.in", "r")
# sys.stdout = open("A-large.out", "w")

t = int(input())
for z in range(1, t + 1):
	data = []
	mx = 0
	n, k = [int(i) for i in input().strip().split()]
	for i in range(n):
		data.append([int(i) for i in input().split()])
	data.sort(key = lambda x: - x[0])
	for i in range(n - k + 1):
		v = sum([2 * each[0] * each[1] for each in sorted(data[i + 1:], \
			key = lambda x: -x[0]*x[1])[:k-1]])
		v += data[i][0]**2 + 2 * data[i][0] * data[i][1]
		if mx < v:
			mx = v
	print("Case #", z, ": ", "{0:.12f}".format(math.pi * mx), sep = '')