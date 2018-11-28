def get_test_cases(input_path):
	f = open(input_path)
	num_cases = int(f.readline().strip())
	test_cases = []
	lines = f.readlines()
	i = 0
	while i < len(lines):
		num_intervals = int(lines[i].strip())
		intervals = [int(interval) for interval in lines[i+1].strip().split(' ')]
		i += 2
		assert num_intervals == len(intervals)
		test_cases.append(intervals)
	assert num_cases == len(test_cases)
	return test_cases

def solve(test_case):
	# first method
	num_mushrooms_on_plate = test_case[0]
	num_eaten = 0
	for interval in test_case[1:]:
		num_eaten += max(num_mushrooms_on_plate-interval, 0)
		num_mushrooms_on_plate = interval
	a = num_eaten

	# second method
	max_delta = 0
	num_mushrooms_on_plate = test_case[0]
	for interval in test_case[1:]:
		max_delta = max(max_delta, num_mushrooms_on_plate-interval)
		num_mushrooms_on_plate = interval

	num_mushrooms_on_plate = test_case[0]
	num_eaten = 0
	for interval in test_case[1:]:
		num_eaten += min(max_delta, num_mushrooms_on_plate)
		num_mushrooms_on_plate = interval
	b = num_eaten

	return a, b

if __name__ == '__main__':
	input_path = 'input.txt'
	output_path = 'output.txt'
	f = open(output_path, 'w')
	test_cases = get_test_cases(input_path)
	for index, test_case in enumerate(test_cases):
		a, b = solve(test_case)
		print >> f, 'Case #%d: %d %d' % (index+1, a, b)
	f.close()