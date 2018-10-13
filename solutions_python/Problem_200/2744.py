INPUT_FILE_PATH = r"C:\Users\Alon\Downloads\tidy_numbers_input.txt"
OUTPUT_FILE_PATH = r"C:\Users\Alon\Downloads\tidy_numbers_output.txt"

def find_decreasing_index(num):
	digits = list(str(num))
	curr_dig = digits[0]
	for index, digit in enumerate(digits):
		if digit < curr_dig:
			return index
		curr_dig = digit
	return -1

def find_largest_tidy_number(num):
	found_index = find_decreasing_index(num)
	if found_index == -1:
		return num
	
	return (find_largest_tidy_number(str(int(num[:found_index]) - 1)) + '9' * (len(num) - found_index)).lstrip('0')

def main(input_file):
	with open(input_file, 'rb') as f:
		data = f.read()
	lines = data.split('\n')
	amount_of_input_lines = lines[0]
	input_lines = lines[1:]
	output = '\n'.join(['Case #{0}: {1}'.format(index+1, find_largest_tidy_number(input_line)) for index, input_line in enumerate(input_lines)])
	with open(OUTPUT_FILE_PATH, "wb") as f:
		f.write(output)

if __name__ == '__main__':
	main(INPUT_FILE_PATH)