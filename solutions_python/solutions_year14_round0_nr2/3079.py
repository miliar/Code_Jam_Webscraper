test_cases = int(raw_input())
for test in xrange(test_cases):
	c, f, x = map(float,raw_input().split())
	rate = 2.0
	current_time = 1
	next_time = 0
	total_time = 0
	while next_time < current_time:
		current_time = x / rate
		next_time = c / rate + x / (rate+f)
		if next_time < current_time:
			total_time += c / rate
		else:
			total_time += current_time
		#for debugging
		#print rate,current_time,next_time,total_time
		rate += f
	print 'Case #%d: %.7f' %((test+1),total_time)
