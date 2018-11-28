import sys

###########################################################

# Produce output in format suitable for submission
def generate_output(answers):

	# Iterate over all test cases
	for i in range(len(answers)):
		print "Case #" + str(i+1) + ":", answers[i]

###########################################################

# Find a number for which all numbers greater than the 
# output, but less than the input, are untidy
def tidy_up(untidy_number):
	
	# Cast to string for indexing
	temp = str(untidy_number)

	# Start at right-most digit
	L = len(temp)
	for i in range(L-2, -1, -1):

		# If digits are decreasing
		RHS = int(temp[i+1])
		LHS = int(temp[i])

		if RHS < LHS:

			# Generate a slightly smaller, tidier number
			temp = temp[:i] + str(LHS - 1) + '9' * (L - i - 1)
			break

	return int(temp)

###########################################################

# To get the largest tidy number, tidy up until clean
def get_largest_tidy(number):

	old = number
	new = tidy_up(number)

	while new != old:
		old = new
		new = tidy_up(old)

	return new

###########################################################


input_file = open(sys.argv[1], 'r')

header_line = input_file.readline()
T = int(header_line.rstrip())

input_data = input_file.readlines()
input_file.close()

answers = []
for entry in input_data:
	number = int(entry.rstrip())
	answers.append(get_largest_tidy(number))

generate_output(answers)


