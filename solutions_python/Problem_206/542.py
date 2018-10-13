t = int(raw_input())
for x in range(t):
	D,n = map(int,raw_input().split())
	min_time = 0.0
	for i in range(n):
		s,k = map(int,raw_input().split())
		time_taken = float(D - s)/k
		if time_taken > min_time:
			min_time = time_taken
			
	final_speed = float(D)/min_time
	#
	print "Case #{}:".format(str(x+1)),
	print "{0:0.6f}".format(final_speed)