import sys

lines = [line.strip() for line in sys.stdin.readlines()]

t = lines.pop(0)

i = 1
for line in lines:
	
	max_shy, shyness_string = line.split()
	
	total_clapping = 0
	friends_needed = 0

	for threshold, value in enumerate(shyness_string):
		#print threshold, value
		if value != '0':
			if (total_clapping >= threshold):
				total_clapping += int(value)
			else:
				#print "Friends needed", threshold, total_clapping
				diff = threshold - total_clapping
				friends_needed += diff 
				total_clapping += int(value) + diff
	
	print "Case #" + str(i) + ": " + str(friends_needed)
	i += 1		
