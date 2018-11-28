
# open files
input_file = open("A-large.in", "r")
output_file = open("output.txt", "w")

# line counter
i = 0
# read through input file
for line in input_file:
	# strip the end new line
	line = line.rstrip("\n")
	# check empty line = eof or fulfilled number of test cases
	if (line):
		# first line tells number of test cases
		if (i == 0):
			n_test_cases = int(line)	# scope is magical in Python
		# fulfilled number of test cases
		elif (i <= n_test_cases):
			# max_shy = maximum shyness Smax
			# shy_distribution = number of persons for each shyness level, 
			# starting from 0 up to max_shy
			max_shy, shy_distribution = line.split(" ")
			# number of friends required
			friends_required = 0
			# initial standing persons = 0
			standing_persons = 0
			for j in range(0, len(shy_distribution)):
				# audience is too shy
				if j > standing_persons+friends_required:
					friends_required += j-standing_persons-friends_required
				# more people standing ~ WOO!!!
				standing_persons += int(shy_distribution[j])
			output_file.write("Case #"+str(i)+": "+str(friends_required)+"\n")
		else:
			print("Google be trolling you!")
			break
	i += 1

# close files
input_file.close()
output_file.close()

# remember to remove the last \n at eof