LINES_FOR_EACH_INPUT = 1
INPUT_FILE_NAME = 'input.txt'
OUTPUT_FILE_NAME = 'output.txt'

def do_case(parsed_input):
	max_shyness = parsed_input[0]
	shyness_list = parsed_input[1]
	
	to_add_counter = 0
	standing = shyness_list[0]
	
	for cur_shyness in range(1, max_shyness + 1):
		
		if shyness_list[cur_shyness] == 0:
			continue
		
		if standing < cur_shyness:
			to_add_counter += cur_shyness - standing
			standing += cur_shyness - standing
		
		standing += shyness_list[cur_shyness] 
		
	
	return str(to_add_counter)
	

def do_parse(input):
	splitted = input[0].split(' ')
	return [int(splitted[0], 10), map(int, list(splitted[1].strip()))]

def main():
	input_f = open(INPUT_FILE_NAME, 'r')
	output = []
	
	num_of_test_cases = int(input_f.readline(), 10)
	
	input_lines = input_f.readlines()
	
	for test_case in range(num_of_test_cases):
		parsed_input = do_parse(input_lines[test_case*LINES_FOR_EACH_INPUT : (test_case + 1) * LINES_FOR_EACH_INPUT])
		output.append('Case #' + str(test_case + 1) + ': ' + do_case(parsed_input))

	output_f = open(OUTPUT_FILE_NAME, 'w')
	output_str = '\n'.join(output)
	output_f.write(output_str)
	print output_str
	
	input_f.close()
	output_f.close()
	
if __name__ == '__main__':
	main()