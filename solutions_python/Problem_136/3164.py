import sys

filename = sys.argv[1]

# We start with 0 cookies.
# C - Number of cookies for a farm
# F - Additional cookies per second from farm
# X - Number of cookies that we want to end up with.

cps = 2.0
start_cookies = 0.0

fp = open(filename, "r")
cases = int(fp.readline())

for i in range(0, cases):
	params = fp.readline().split(' ')
	c = float(params[0])
	f = float(params[1])
	x = float(params[2])
	
	total_cookies = start_cookies
	current_cps = cps
	total_time = 0
	done = False
	
	while not done:
		if (((x / (current_cps + f)) + (c / current_cps)) < (x / current_cps)):
			total_time = total_time + (c / current_cps)
			current_cps = current_cps + f
		else:
			total_time = total_time + (x / current_cps)
			done = True
		
	print "Case #" + str(i+1) + ":", total_time

