filename = 'B-small-attempt0.in'
input = open(filename,'r')

output = open('output.txt','w')
cases = int(input.readline())

base_rate = 2.0

for testcaseno in range(1,cases+1):
	values = input.readline()[:-1].split(' ')
	#split(values)
	c = float(values.pop(0))
	f = float(values.pop(0))
	x = float(values.pop(0))

	rate = base_rate
	cookies = 0.0
	farms_to_buy = 0
	best_time = 1000000.0
	current_time = 0.0
	while(True):
		current_time = 0.0
		rate = base_rate
		farms_bought = 0
		while(farms_bought < farms_to_buy):
			time_to_next_farm = c / rate
			current_time += time_to_next_farm
			farms_bought += 1
			rate += f
			#print("Bought farm after " + str(time_to_next_farm))
			#print("Rate is " + str(rate))
		if farms_bought == farms_to_buy:
			time_to_x = x / rate
			#print("Stopped buying farms; " + str(current_time) +" has passed, " + str(time_to_x) + " to go to end.")
			current_time += time_to_x
		#print("Current time for " + str(farms_bought) + " farms is " + str(current_time))
		if best_time > current_time:
			best_time = current_time
		else:
			#Last farm count was best
			best_time = round(best_time, 7)
			output.write("Case #" + str(testcaseno) + ": " + str(best_time) +'\n')
			break

		farms_to_buy+=1
