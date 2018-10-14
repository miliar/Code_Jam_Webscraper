tests = int(raw_input())

for i in range(tests):
	numbers = raw_input().split(" ")
	cost = float(numbers[0])
	bonus = float(numbers[1])
	goal = float(numbers[2])

	seconds = 0.0
	curr_rate = 2.0

	while goal / curr_rate > (((goal) / (curr_rate + bonus)) + (cost / curr_rate)):
		seconds += (cost / curr_rate)	
		curr_rate += bonus
		
	#print goal / curr_rate
	seconds += goal / curr_rate
	
	print "Case #" + str(i+1) + ": ",
	print("%.7f" % seconds)




# 1. 1.0000
# 2. 39.1666667
# 3. 63.9680013
# 4. 526.1904762
