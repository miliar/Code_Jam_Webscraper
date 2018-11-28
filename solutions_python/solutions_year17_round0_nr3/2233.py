import math

INPUT_FILE_PATH = r"C:\Users\Alon\Downloads\bathroom_stalls_input.txt"
OUTPUT_FILE_PATH = r"C:\Users\Alon\Downloads\bathroom_stalls_output.txt"

def find_wanted_level_and_index(number_of_people):
	wanted_level = int(math.floor(math.log(number_of_people, 2)))
	wanted_index = number_of_people - pow(2, int(math.floor(math.log(number_of_people, 2))))
	return wanted_level, wanted_index

def generate_new_stall(space):
	return (int(math.floor((space - 1) / 2.0)), int(math.ceil((space - 1) / 2.0)))

def get_next_level(level):
	new_level = []
	for stall in level:
		new_level.append(generate_new_stall(stall[0]))
		new_level.append(generate_new_stall(stall[1]))
	return new_level

def compare_two_stalls(stall_one, stall_two):
	stall_one_total = stall_one[0] + stall_one[1]
	stall_two_total = stall_two[0] + stall_two[1]
	if stall_one_total < stall_two_total:
		return -1
	if stall_one_total > stall_two_total:
		return 1
	return 0

def generate_bathroom_stall_output(number_of_stalls, number_of_people):
	wanted_level, wanted_index = find_wanted_level_and_index(number_of_people)
	all_levels = [[generate_new_stall(number_of_stalls)]]
	for i in xrange(wanted_level):
		all_levels.append(get_next_level(all_levels[-1]))
	last_level = all_levels[-1]
	last_level.sort(cmp=compare_two_stalls, reverse=True)
	return last_level[wanted_index]

def main():
	with open(INPUT_FILE_PATH, "rb") as f:
		data = f.read()

	lines = data.split('\n')
	amount_of_input_lines = int(lines[0])
	input_lines = lines[1:]
	output = []
	for i in xrange(amount_of_input_lines):
		number_of_stalls, number_of_people = input_lines[i].split(' ')
		number_of_people = int(number_of_people)
		number_of_stalls = int(number_of_stalls)
		bathroom_stall_output = generate_bathroom_stall_output(number_of_stalls, number_of_people)
		output.append('Case #{0}: {1} {2}'.format(i+1, max(bathroom_stall_output), min(bathroom_stall_output)))
	output = '\n'.join(output)
	with open(OUTPUT_FILE_PATH, 'wb') as f:
		f.write(output)

if __name__ == '__main__':
	main()