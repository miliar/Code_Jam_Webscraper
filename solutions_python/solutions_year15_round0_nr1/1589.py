def get_cases(filename):
	file = open(filename, "r")
	num_tests = int(file.readline())
	test_cases = file.readlines()
	file.close()
	return num_tests, test_cases
	
def Q1(filename):
#	num_tests unused - and in fact I don't know why it's included
#	what language fails to detect an EOF??
	num_tests, test_cases = get_cases(filename)
	output = open(filename + ".solution", "w")
	for case in range(len(test_cases)):
		required_friends = 0
		current_clappers = 0
		audience_string = test_cases[case].split()[1]
		for shyness_level in range(len(audience_string)):
			if (current_clappers >= shyness_level):
				current_clappers += int(audience_string[shyness_level])
			else:
				required_friends += shyness_level - current_clappers
				current_clappers = shyness_level + int(audience_string[shyness_level])
		output.write("Case #%d: %d\n" % (case + 1,required_friends))
	output.close()
