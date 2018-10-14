def get_cases(input_path):
	f = open(input_path)
	num_cases = int(f.readline().strip())
	test_cases = []
	for line in f:
		max_shyness, shy_counts = line.strip().split(' ')

		max_shyness = int(max_shyness)
		shy_counts = [int(i) for i in list(shy_counts)]
		test_cases.append(shy_counts)
		assert max_shyness+1 == len(shy_counts)
	f.close()

	assert num_cases == len(test_cases)
	return test_cases

def solve(shy_counts):
	people_standing = 0
	friends_invited = 0
	for shyness_level, count in enumerate(shy_counts):
		if people_standing < shyness_level:
			friends_invited += shyness_level - people_standing
			people_standing += shyness_level - people_standing
		people_standing += count
	return friends_invited


if __name__ == '__main__':
	input_path = 'input.txt'
	output_path = 'output.txt'

	test_cases = get_cases(input_path)
	f = open(output_path, 'w')
	for (index, case) in enumerate(test_cases):
		print >> f, 'Case #%d: %d' % (index+1, solve(case))
	f.close()


