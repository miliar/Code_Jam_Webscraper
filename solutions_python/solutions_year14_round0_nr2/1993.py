T = input()

for t in range(1, T+1):

	farm_cost, rate_gain, goal = map(float, raw_input().split())

	res = 0.0
	rate = 2

	while True:
		t1 = goal / rate
		t2 = (farm_cost / rate) + (goal / (rate + rate_gain))

		if t1 <= t2:
			res += t1
			break
		else:
			res += (farm_cost / rate)
			rate += rate_gain 

	print 'Case #%d: %.07f' % (t, res)
