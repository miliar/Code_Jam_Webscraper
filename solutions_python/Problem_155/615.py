# ___ ______________________________________________ ___ #
#|_/*|                                              |*\_|#
#|_/*|    Google Code Jam - "Hello World"           |*\_|#
#|_/*|    10.04.2015 - the end                      |*\_|#
#|_/*|    Qualification                             |*\_|#
#|_/*|______________________________________________|*\_|#
#|                                                      |#
#|        Denis Werner - denis@nobbd.de                 |#
#|______________________________________________________|#
#                                                        #


filename = "A-large.in"
#filename = "A-small-attempt0.in"

lines = ()
with open(filename) as file:
	lines = file.read().splitlines()

number_of_sets = int(lines[0])

with open(filename+".solved","w") as outputfile:
	for i in range(0,number_of_sets):


		#credits = int(lines[i*3+1])
		current_line = lines[i+1]
		max_level = current_line[0:current_line.index(" ")]
		#print max_level
		people = current_line[current_line.index(" "):]
		#print people
		curr_sum = 0
		additional_people = 0
		for j in range(1,len(people)):
			curr_sum += int(people[j])
			if curr_sum < j:
				additional_people += 1
				curr_sum += 1
		#print additional_people

		
		line = "Case #"+str(i+1)+": "+str(additional_people)
		print line
		outputfile.write(line+"\n")				
					