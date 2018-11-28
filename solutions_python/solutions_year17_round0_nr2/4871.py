input_file = "input2.in"
output_file = open('OUTPUT_' + input_file, 'w')
output_data = []

def load_input():
	with open(input_file) as f:
		input_data = f.readlines()
	return input_data

def write_output(output_data):
	i = 1
	for output in output_data:
		out = "Case #" + str(i) + ": " + str(output) + "\n"
		output_file.write(out)
		i += 1

def loop_over_test_cases(test_cases):
	T = int(test_cases[0]) 
	for i in range(1,T+1):
		get_last_tidy_num(test_cases[i].strip())

def get_last_tidy_num(test_case):
	#base_10 = "{0:d}".format(int(test_case))
	last_number = int(test_case)

	for i in range(last_number, 0, -1):
		num_array = [int(d) for d in str(i)]
		#check if sorted in ascending
		if sorted(num_array) == num_array:
			output_data.append(i)
			break

#START

input_data = load_input()
loop_over_test_cases(input_data)
write_output(output_data)

print ("DONE!")



