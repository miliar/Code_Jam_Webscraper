TEST = "A-large"

with open(TEST + ".in", 'r') as in_data:
	input_data = in_data.readlines()

num_tests = int(input_data[0])
outputs = []

# iterate through tests
for test_num in range(num_tests):

	# extract test data
	test_line = input_data[test_num + 1]
	max_shy, shy_levels = test_line.strip().split()

	# cast to integers
	max_shy = int(max_shy)
	shy_levels = [int(i) for i in shy_levels]

	# determine friends to invite
	before = 0
	friends = 0
	for (level, count) in enumerate(shy_levels):
		while before + friends < level:
			friends += 1
		before += count
			
	outputs.append(friends)

with open(TEST + ".out", 'w') as out_data:
	for (num, result) in enumerate(outputs):
		line = "Case #" + str(num + 1) + ": " + str(result) + "\n"
		out_data.write(line)
