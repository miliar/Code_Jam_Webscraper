import argparse
def parse_arguments():
	parser = argparse.ArgumentParser(description='Test the Magic trick on the input file and display result in the output file')
	parser.add_argument('input_file')
	parser.add_argument('output_file')
	return parser.parse_args()
	
class input_format:
	goal = 0.0
	farm_cost = 0.0
	rate_increase = 0.0
class output_format:
	result = 0
	
def process_input(input_file):
	number_of_tests = int(input_file.readline())
	result = []
	for i in range(number_of_tests):
		line = input_file.readline().split()
		input_result = input_format
		input_result.farm_cost = float(line[0])
		input_result.rate_increase = float(line[1])
		input_result.goal = float(line[2])
		
		result += ["Case #"+str(i+1)+": "+str(process(input_result))]
	return result
def process(input_result):
	total_time = 0.0
	rate = 2.0
	time_remaining = 1.0 #dummy
	time_remaining_with_new_farm = 0.0 #dummy
	
	while time_remaining > time_remaining_with_new_farm:
		total_time += input_result.farm_cost / rate
		time_remaining = (input_result.goal - input_result.farm_cost) / rate
		rate += input_result.rate_increase
		time_remaining_with_new_farm = input_result.goal / rate	
	return total_time + time_remaining # last iteration's time_remaining

args = parse_arguments()
input_file = open(args.input_file, 'r')
output_file = open( args.output_file, 'w')
output_file.write("\n".join(process_input(input_file)))
