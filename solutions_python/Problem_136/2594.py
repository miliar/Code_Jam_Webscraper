num_testcases = raw_input()
for i in range(0,int(num_testcases)):
	inp_str = raw_input()
	inp_split = inp_str.split(" ")
	c = float(inp_split[0])
	f = float(inp_split[1])
	x = float(inp_split[2])
	cur = 0
	time = 0
	rate = 2
	while cur<x:
		#Do we buy a farm in this round?
		time_taken_with_cur_rate = x / rate

		time_taken_with_next_rate = (c/rate)+(x/(rate+f))

		if time_taken_with_cur_rate<time_taken_with_next_rate:
			#We've hit the optimal rate.
			time += time_taken_with_cur_rate
			break
		else:
			#buy
			time += c/rate
			rate += f
	print "Case #"+str(i+1)+": "+str(time)