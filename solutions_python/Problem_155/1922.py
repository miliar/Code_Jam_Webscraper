##### Functions Below ##########################################################

##### Program Logic Below ######################################################

#The filenames of the input and output files
input_path = r"C:\Users\Jake\Documents\~Programming Stuff\Google Code Jam\Competition\2015\Qualification Round\Problem 1\input.txt"
output_path = r"C:\Users\Jake\Documents\~Programming Stuff\Google Code Jam\Competition\2015\Qualification Round\Problem 1\output.txt"

#Read in the text from the input file
input_text = open(input_path, 'r')

#Determine the number of test cases by converting the first line to an int
test_cases = int(input_text.readline())

# Solve each case and output answer to a text file
output_text = open(output_path, 'w')
for c in range(test_cases):	
	data = input_text.readline().split(" ")
	s_max = data[0]
	s_others = data[1]
	if "\n" in s_others:
		s_others = s_others[0:-1]

	up = 0
	needed = 0
	for i in range(len(s_others)):
		s_i = int(s_others[i])
		while up < i:
			needed += 1
			up += 1
		up += s_i

	output_text.write("Case #%s: " %(c + 1) + str(needed) + "\n")

output_text.close()