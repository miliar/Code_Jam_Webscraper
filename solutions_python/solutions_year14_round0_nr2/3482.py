
file = open('problem2_small.in')
w = open("problem2_out.txt",'w')

file.readline()

count = 0
for line in file:
	count += 1
	l = line.strip().split(" ")

	c = float(l[0])
	f = float(l[1])
	x = float(l[2])

	rate = 2.0

	total = 0

	previous = 100000.0
	farms = 0
	result = 50000.0
	total_farm = 0

	while result < previous:
		previous = result
		more_farm = c/rate
		result = (x/rate) + total_farm
		rate += f
	
		total_farm += more_farm
	
		#print "f: " + str(more_farm)
		#print "w: " + str(result)
	

	w.write("Case #" + str(count) + ": " + str(previous)+'\n')
	
w.close()
file.close()

	
	


	
	
	
	
	
	

