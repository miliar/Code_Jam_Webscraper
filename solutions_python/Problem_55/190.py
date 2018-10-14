import sys
from fractions import gcd

data = [x.strip() for x in sys.stdin.readlines()]

T = int(data.pop(0))
testcases = []
for i in xrange(len(data) / 2):
	R, k, N = tuple([int(x) for x in data[i * 2].split(' ')])
	g = [int(x) for x in data[i * 2 + 1].split(' ')]
	testcases.append((R, k, g))

for case, e in enumerate(testcases):
	R, k, g = e
	profit = 0

	# Building cache
	cache = []
	for i in xrange(len(g)):
		passengers = 0
		next_group = i
		for j in xrange(i, len(g)):
			if passengers + g[j] > k:
				break
			passengers += g[j]
			next_group += 1

		if passengers < k and next_group == len(g):
			next_group = 0
			for j in xrange(0, i):
				if passengers + g[j] > k:
					break
				passengers += g[j]
				next_group += 1
		else:
			if next_group == len(g):
				next_group = 0

		cache.append((passengers, next_group))

	# Looking for loop
	positions = {0: (0, 0)}
	pos = 0
	profit = 0

	starting_ride = R
	loop_length = R + 1
	loop_profit = 0

	for i in xrange(len(g) * 2 + 1):
		passengers, pos = cache[pos]

		if pos in positions:
			prev_i, prev_profit = positions[pos]
			loop_length = i + 1 - prev_i
			loop_profit = profit + passengers - prev_profit
			starting_ride = i + 1
			break
		else:
			profit += passengers
			positions[pos] = (i + 1, profit)

	# Subtract loops
	if R > starting_ride:
		loops = (R - starting_ride) / loop_length
		profit = loop_profit * ((R - starting_ride) / loop_length)
		R -= loops * loop_length
	else:
		profit = 0

	pos = 0
	for r in xrange(R):
		passengers, pos = cache[pos]
		profit += passengers

	print "Case #" + str(case + 1) + ": " + str(profit)
