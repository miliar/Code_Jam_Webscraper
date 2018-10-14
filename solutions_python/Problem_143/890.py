import math
##### Functions Below ##########################################################

##### Program Logic Below ######################################################

#The filenames of the input and output files
input_path = r"C:\Users\Jake\Documents\~Programming Stuff\Google Code Jam\Competition\Round 1b\Problem 2\input.txt"
output_path = r"C:\Users\Jake\Documents\~Programming Stuff\Google Code Jam\Competition\Round 1b\Problem 2\output.txt"

#Read in the text from the input file
input_text = open(input_path, 'r')

#Determine the number of test cases by converting the first line to an int
test_cases = int(input_text.readline())

# Solve each case and output answer to a text file
output_text = open(output_path, 'w')

for case in range(test_cases):
	print case
	nums = [int(i) for i in input_text.readline().split()]

	A = nums[0]
	B = nums[1]
	C = nums[2]

	multiplier = 1

	'''
	places = 1
	num = 1
	while num < C:
		num *= 2
		places += 1


	A_check = 0
	B_check = 0

	A_b_loc = bin(A).index('b')
	B_b_loc = bin(B).index('b')

	if places >= len(bin(A)[A_b_loc + 1:]):
		A_check = A
	else:
		A_check = (2**places)
	if places >= len(bin(B)[B_b_loc + 1:]):
		B_check = B	
	else:
		print 'a'
		B_check = (2**places)

	
	bin_string = bin(min(A,B))[2:]
	bin_string = bin_string[:-places]
	multiplier = math.factorial(len(bin_string))
	'''
	

	winners = 0
	for i in range(A):
		for j in range(B):
			if (i & j) < C:
				winners += 1
	winners = winners * multiplier

	output_text.write("Case #%s: %s\n" %(case + 1, winners))

output_text.close()
