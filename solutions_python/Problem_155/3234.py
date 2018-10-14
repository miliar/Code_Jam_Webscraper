__author__ = 'El1t'


def calculate(audience):
	current_standers = 0
	required_standers = 0
	for shyness_level, members_of_shyness in enumerate(audience):
		if current_standers < shyness_level:
			required_standers += shyness_level - current_standers
			current_standers = shyness_level
		current_standers += int(members_of_shyness)
	return required_standers

file_name = input('Input file: ')
number_of_cases = None
with open(file_name, 'r') as input_file, open('standing_output.txt', 'w') as output_file:
	for i, line in enumerate(input_file):
		if not number_of_cases:
			number_of_cases = int(line)
		else:
			output_file.write('Case #' + str(i) + ': ' + str(calculate(line.split(' ')[1].strip())) + '\n')