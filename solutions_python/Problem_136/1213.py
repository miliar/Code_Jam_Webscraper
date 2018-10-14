f=file("B-large.in")
op=file("Blarge.op","w")
total_line=f.readline()
total_line=int(total_line)

for i in range(total_line):
	
	line=f.readline()
	nums=line.split(' ')
	nums[-1]=nums[-1].split('\n')[0]
	nums=[ float(data) for data in nums]
	
	speed=2
	ms=0
	total_time=0
	cookies=0
	farm_cost=nums[0]
	speed_increase=nums[1]
	goal_cookies=nums[2]
	flag=0
	#print farm_cost,",",speed_increase,",",goal_cookies
	while cookies<goal_cookies:
		ms=ms+farm_cost/speed
		cookies=farm_cost
		
		if cookies>=farm_cost:
			if (goal_cookies-cookies)/speed > (goal_cookies)/(speed+speed_increase): 
				cookies=cookies-farm_cost
				speed=speed+speed_increase
			else:
				total_time=ms + float((goal_cookies-cookies)/speed)
				cookies=goal_cookies
				flag=1
		#print "s:",ms," cookies : ",cookies," speed:",speed 
		
	if flag!=1:
		total_time=ms
	
	print total_time
	
		
	string = "case #"+str(i+1)+": "
	string =string + str(total_time)
	op.write(string+"\n")
	
	
