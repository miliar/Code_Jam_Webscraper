T = int(raw_input())

DEBUG = False

for case in xrange(T):

	# The initial cookie winning rate is 2 cookies.
	cookie_rate = 2.0
	no_cookies  = 0.0
	time        = 0.0

	input_line = raw_input().split()

	C = float(input_line[0])  # The coast of a farm.
	F = float(input_line[1])  # The additional rate given by a farm.
	X = float(input_line[2])  # The cookies target.

	while(no_cookies < X):

		# Calculates the time left to reach the target
		# with the current cookie rate.
		time_left = (X - no_cookies) / cookie_rate

		if DEBUG:
			print "[T: {1} NC: {2} R: {3}] Time left is {0}".format(time_left, time, no_cookies, cookie_rate)

		time_with_farm = no_cookies / F + (C - no_cookies) / cookie_rate

		if DEBUG:
			print "With", time_with_farm,"..."
		# Then, we have to decide if it is worth buying the farm.
		if time_with_farm < time_left:
			if DEBUG:
				print "Timespan of {0} at {1} cookies".format(time_with_farm, no_cookies)

			# We can actually buy the farm.
			if no_cookies >= C:
				if DEBUG:	
					print "Bought"
				cookie_rate += F
				no_cookies  -= C				
			else:
				if DEBUG:
					print "Not bought"
				# Advances time till we can buy the new farm.
				time_really_needed = (C - no_cookies) / cookie_rate
				time += time_really_needed
				no_cookies += time_really_needed * cookie_rate
		else:
			time += time_left
			break

		#raw_input()

		# Update the number of cookies.
		# Decide whether or not buy a new farm.
		# update cookie rate.

	if DEBUG:
		print "Case #{0}: {1:.7f}\n----------------------------".format(case + 1, time)
	else:
		print "Case #{0}: {1:.7f}".format(case + 1, time)
