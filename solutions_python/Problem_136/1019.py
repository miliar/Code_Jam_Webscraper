cookie = 0


t = int(raw_input())


for i in xrange(t):
	time = 0
	rate = 2
	c,f,x = map(float,raw_input().split())
	
	last_rate = 0
	while(True):
		first = (x/rate) + last_rate
		second = ((c/rate) + (x/(rate+f))) + last_rate 
		if second < first:
			last_rate += (c/rate)
			time += last_rate
			rate += f
		else :
			break
	
	print "Case #" + str(i+1) + ":",
	print "%.7f" % (first)
