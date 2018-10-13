input = open ("B-large.in", "r")
out = open  ("output.txt", 'w')

cases = int(input.readline())
for case in range (0, cases):
	params = map(float, input.readline().split())
	c = params[0] #cookies to buy the farm
	f = params[1] #farm cookie production per second
	x = params[2] #cookies to win
	
	time = 0 
	rate = 2 #starting rate of 2 cps
	cookies = 0
	
	"""
	algorithm: every c cookies, check how long will it take to goal if we buy the 
	farm, and how long if we dont. Pick the better. """
	while cookies < x:
		noFarm = time + (x)/rate
		#current time + time to get c cookies + time to get to goal with new rate
		withFarm = time + c/rate + (x )/(rate + f) 
		if noFarm < withFarm:
			cookies  = x
			time = time + (x)/rate
		else:
			cookies = 0
			time += c/rate #time to produce next c cookies
			rate += f
		#print noFarm
		#print withFarm
	print "Case #%d: %f" %(case+1, time)
	out.write("Case #%d: %f\n" %(case+1, time))
out.close()
input.close()
		
		
		
		