def process(f):
	cost, extraRate, goal = [float(x) for x in f.readline().split(' ')]
	rate = 2
	projectedTime = goal / rate
	overhead = 0
	# We want to compare time at current rate vs. time when we buy
	while True:
		timeIfBought = overhead + cost / rate + goal / (extraRate + rate)
		if timeIfBought >= projectedTime:
			return projectedTime
		projectedTime = timeIfBought
		overhead = overhead + cost / rate
		rate = rate + extraRate


with open("testcase") as f:
	numCases = int(f.readline())
	for case in range(1, numCases + 1):
		val = process(f)
		print "Case #{case}: {time}".format(case=case, time=val)
