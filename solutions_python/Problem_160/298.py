def get_test_cases(input_path):
	f = open(input_path)
	num_cases = int(f.readline().strip())
	test_cases = []
	lines = f.readlines()
	i = 0
	while i < len(lines):
		num_barbers, place_in_line = [int(interval) for interval in lines[i].strip().split(' ')]
		barber_times = [int(interval) for interval in lines[i+1].strip().split(' ')]
		i += 2
		assert num_barbers == len(barber_times)
		test_cases.append([place_in_line, barber_times])
	assert num_cases == len(test_cases)
	return test_cases

def greatest_common_denominator(x, y):
    while y:      
        x, y = y, x % y
    return x

def atomic_lcm(x, y):
    return x * y // greatest_common_denominator(x, y)

def least_common_multiple(*args):
    return reduce(atomic_lcm, args)

def simulate(barber_times, LCM):
	time_step = 0
	barber_states = [0]*len(barber_times)
	chosen_barbers = []
	while time_step < LCM:
		for index, barber_state in enumerate(barber_states):
			if barber_state == 0:
				chosen_barbers.append(index+1)
				barber_states[index] = barber_times[index] # reset the clock
			barber_states[index] = barber_states[index] - 1
		time_step += 1
	return chosen_barbers

def solve(test_case):
	place_in_line, barber_times = test_case
	LCM = least_common_multiple(*barber_times)
	chosen_barbers = simulate(barber_times, LCM)
	remainder = place_in_line % len(chosen_barbers)
	my_barber = chosen_barbers[remainder-1]
	return my_barber

if __name__ == '__main__':
	input_path = 'input.txt'
	output_path = 'output.txt'
	f = open(output_path, 'w')
	test_cases = get_test_cases(input_path)
	for index, test_case in enumerate(test_cases):
		my_barber = solve(test_case)
		print >> f, 'Case #%d: %d' % (index+1, my_barber)
	f.close()