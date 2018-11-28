n = int(raw_input())

for iterator in range(n):
	C, F, X = map(float, raw_input().strip().split(' '))
	rate = 2.0
	wait_time_offset = 0.0
	count = 0
	while True:
		wait_time_to_finish = wait_time_offset + X/rate
		wait_time_to_buy = wait_time_offset + C/rate
		rate_new = rate + F
		wait_time_to_finish_new = wait_time_to_buy + X/rate_new
		#print wait_time_to_finish, wait_time_to_finish_new
		if wait_time_to_finish < wait_time_to_finish_new :
			break
		rate = rate_new
		wait_time_offset = wait_time_to_buy
		count += 1
	#print count
	#print wait_time_to_finish, wait_time_to_finish_new
	print "Case #%d: %.7f" % (iterator+1, wait_time_to_finish)
