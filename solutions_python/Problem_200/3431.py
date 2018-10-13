def smart_decrease(letter, next_letter, index):
	decreased_digit = int(letter)

	if int(letter) < int(next_letter) and index > 0:
		return (str(int(next_letter)), False)
	elif index > 0:
		decreased_digit = int(letter) - 1
		if decreased_digit < 0:
			return ('9', False)
	else:
		decreased_digit = int(letter) - 1

	return (str(decreased_digit), True)


def tidy_decrease(number_str):
	stop, new_digit = False, list(number_str)
	next_letter = '-1'
	for itr in range(len(number_str)):
		if stop: break
		new_digit[-(itr+1)], stop = smart_decrease(number_str[-(itr+1)], next_letter, len(number_str)-(itr + 1))
		next_letter = new_digit[-(itr+1)]
	return str(int(''.join(new_digit)))



def is_descending(number_str):

	if len(number_str) == 1:
		return True

	old_number = -1
	for letter in number_str:
		digit = int(letter)
		if digit < old_number:
			return False

		old_number = digit

	return True


def handle_zero(number_str):
	if '0' in number_str:
		idx = number_str.index('0')
		num = str(int(number_str[:idx]) - 1)
		return str(int(num + ''.join(['9' for i in range(len(number_str[idx:]))])))
	return number_str

def get_last_tidy(number_str):
	#print ("Starting: %s" % number_str)
	while(not is_descending(number_str)):
		if '0' in number_str:
			number_str = handle_zero(number_str)
		else:
			number_str = tidy_decrease(number_str)

	return number_str


input_file_name = 'B-small-attempt0.in'
output_file_name = 'B-small-attempt0.out'

output_line_template = "Case #%d: %s"
outputs = []

with open(input_file_name, 'r') as input_file:
	num_tests = int(input_file.readline().strip())
	for test_id in range(1, num_tests+1):
		number = input_file.readline().strip()
		tidy_number = get_last_tidy(number)
		outputs.append(output_line_template % (test_id, tidy_number))

with open(output_file_name, 'w') as output_file:
	output_file.write('\n'.join(outputs))




