import sys

""" Magic trick """

PRINT_STRING = "Case #{0}: {1}"
BAD_MAGIC = "Bad magician!"
CHEATER = "Volunteer cheated!"

if (len(sys.argv) < 2):
	print "Pass in a file please"
else:
	
	# Open file 
	f = open(sys.argv[1], "r")

	lines = f.readlines()

if len(lines) < 1:
	print "Uhhh... wrong file?"
else:
	test_cases = lines[0]
	i = 1 # 0 is the test_cases
	c = 0
	out_file = open("out.txt", "w")
	
	while c < int(test_cases) :
		first_answer = lines[i].replace("\n","")
		
		i = i + 1
	
		first_arrangement = []
		
		x = 0
		while x < 4:
			first_arrangement.append(lines[i].replace("\n", ""))
			x = x + 1
			i = i + 1
				
		second_answer = lines[i].replace("\n","")

		i = i + 1
		
		second_arrangment = []
		
		x = 0
		while x < 4:
			second_arrangment.append(lines[i].replace("\n", ""))
			x = x + 1
			i = i + 1

		print second_answer
		second_lines = second_arrangment[int(second_answer) - 1].split(" ")
		first_lines = first_arrangement[int(first_answer) - 1].split(" ")

		number_of_lines = 0
		for line in first_lines:
			if line in second_lines:
				answer = line
				number_of_lines = number_of_lines + 1
		
		c = c + 1

		if number_of_lines == 0:
			out_file.write(PRINT_STRING.format(c, CHEATER) + "\n")
		elif number_of_lines > 1:
			out_file.write( PRINT_STRING.format(c, BAD_MAGIC)+ "\n")
		else:
			out_file.write( PRINT_STRING.format(c, answer)+ "\n")


