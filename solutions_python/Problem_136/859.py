# Helper Functions


### MAIN PROGRAM ###

input_filename  = "B-large.in"
output_filename = "B-large-ans.txt"


f = open(input_filename, "r")
g = open(output_filename, "w")

number_of_cases = int(f.readline())

case_cnt = 0
while case_cnt < number_of_cases:
	# get C, F, X
	C, F, X = [float(x) for x in f.readline().strip().split(' ')]
	
	cookie_cnt   = 0
	cookie_rate  = 2
	time_elapsed = 0
	
	# deal with special case where we reach X before getting option to buy new farm
	if X <= C:
		cookie_cnt    = X
		time_elapsed += X / cookie_rate
	
	# normal case where X > C
	while cookie_cnt < X:
		# move forward in time until you have C cookies.
		cookie_cnt    = C
		time_elapsed += C / cookie_rate
		# check if it makes sense to buy a new farm. if yes, buy it.
		# if it doesn't, then generate cookies until X is reached.
		if X / (cookie_rate + F) < (X-C) / cookie_rate:
			cookie_cnt   = 0
			cookie_rate += F
		else:
			cookie_cnt    = X
			time_elapsed += (X-C) / cookie_rate

	# output to screen & file
	print   "Case #" + str(case_cnt+1) + ": " + ("%.7f" % time_elapsed)
	g.write("Case #" + str(case_cnt+1) + ": " + ("%.7f" % time_elapsed) + "\n")
	
	# move on to the next case
	case_cnt += 1

f.close()
g.close()

