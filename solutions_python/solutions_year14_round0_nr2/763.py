import sys

tc = int(sys.stdin.readline())

for t in range(1,tc+1):
	result_str = "Case #" + str(t) + ": "
	#logic here
	line = sys.stdin.readline().split()
	c = float(line[0])
	f = float(line[1])
	x = float(line[2])

	cookie = 0.0
	rate = 2.0
	time = 0.0
	ans = 0
	at_current_rate = time + x/rate
	after_time_to_buy = time + c/rate
	rate_after = rate + f
	time_if_buy = after_time_to_buy +  x/rate_after
	while(at_current_rate > time_if_buy):
		rate = rate_after
		time =after_time_to_buy
		at_current_rate = time + x/rate
		after_time_to_buy = time + c/rate
		rate_after = rate + f
		time_if_buy = after_time_to_buy +  x/rate_after

	result_str += '{0:.7f}'.format(at_current_rate)
	print result_str