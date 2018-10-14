import math

num_cases = input()

for line_index in xrange(0, num_cases):
	
	case_index = (line_index+1) #adjust since cases aren't zero-indexed
 
	line = raw_input()
	line = line.split(" ")

	n = int(line[0])
	m = int(line[1])
 
	recycled_pairs = list()
	count = 0
 
	for number in xrange(n, m+1):
		number_string = list(str(number))
		original_number = str(number)

	#print "*" + str(number)

		for shift_count in xrange(1,len(number_string)):
			number_string.append(number_string.pop(0))
  
			#out of bounds?
			current_number = int("".join(number_string))

			if (current_number >= n and current_number <= m and str(current_number) != original_number):
				#print str(current_number)

				if (not (number,current_number) in recycled_pairs):
					#print current_number
					recycled_pairs.append((number,current_number))
					count = count + 1
			
			
	print("Case #%d: %d" % (case_index, count / 2))