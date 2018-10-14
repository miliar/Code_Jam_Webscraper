#!/usr/python

def getResultOfWaiting(diner_plates):
        for i in range(0, len(diner_plates)):
		if diner_plates[i] > 0:
			diner_plates[i] = diner_plates[i] - 1
        return diner_plates

def splitLargestByFactor(plates, factor):
        max_index = plates.index(max(plates))
	if (plates[max_index] /factor) > 1:
		plates.append(plates[max_index]/factor)
		plates[max_index] = plates[max_index]-(plates[max_index]/factor)
#		print "PLATES AFTER SPLIT"
#		print plates
#		print "++++++++++++"
		return plates
	return []

def cost(time, plates):
	return time + max(plates)

num_tests = 0
num_diners = 0
diner_pancakes = []
tests = []

with open("B-small-attempt1.in") as f:
        num_tests = int(f.readline())
        for i in range(0, int(num_tests)):
		num_diners = int(f.readline())
                diner_pancakes = [int(n) for n in f.readline().strip().split()]
                total_pancakes = sum(diner_pancakes)
		#diner_pancakes.append(test)
		tests.append([num_diners, diner_pancakes])
#		print(diner_pancakes)
		
f = open('eatTimeOutput.txt', 'w+')

for i in range(0, num_tests):
	test = tests[i]
	num_diners = test[0]
	diner_plates = test[1]
	total_pancakes = sum(diner_plates)	
	 
	times = []	
	frontier = []
	current_node = []
	frontier.append([0, diner_plates])

	optimal_time = 100000 
	while frontier:
		minimum = 10000
		min_index = 0
		current_diner_plates = frontier.pop()

#		print "CURRENT TIME :: " + str(current_diner_plates[0])
		total_pancakes = sum(current_diner_plates[1])
#		print "total pancakes = " + str(total_pancakes)
		#print current_diner_plates[1]

		if( total_pancakes <= 0):
			time_cost = cost(current_diner_plates[0], current_diner_plates[1])
			times.append(time_cost)
#	 		print "TIME ADDED :: " + str(time_cost)
#			print "reached the end. breaking out"
			continue	
		
		#take next frontier object and add result of either
		# waiting, or cutting a stack by n pancakes\
		new_diner_plates_after_wait = getResultOfWaiting(current_diner_plates[1][:])
#		print "new diners ::"
#		print new_diner_plates_after_wait

#		print new_diner_plates_after_split

		frontier.append([current_diner_plates[0]+1,new_diner_plates_after_wait])		

		for factor in range(2, (max(current_diner_plates[1])/2)+1):
			new_diner_plates_after_split = splitLargestByFactor(current_diner_plates[1][:], factor)
			if new_diner_plates_after_split:
				frontier.append([current_diner_plates[0]+1,new_diner_plates_after_split])
#		print "-----------------------------------------------------"
		 	
		#print "NEW DINER PLATE ALLOCATION AFTER SPLIT :: "
		#print (new_diner_plates_after_split)
	#	print "FRONTIER SIZE :: " + str(len(frontier))
			


		## readjust size of stacks
		
		## get new total count
#	print times
#	print "------------------------------------------------------"
	f.write( "Case #" + str(i+1) + ": " + str(min(times)) + "\n"	)



