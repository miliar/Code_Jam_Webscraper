import argparse
def parse_arguments():
	parser = argparse.ArgumentParser(description='Test the Magic trick on the input file and display result in the output file')
	parser.add_argument('input_file')
	parser.add_argument('output_file')
	return parser.parse_args()
	
class input_format:
	first_row = []
	second_row = []
class output_format:
	result = 0
	
def retrieve_row(input_file):
	row_id = int(input_file.readline())
	for _ in range(row_id - 1):
		next(input_file)
	result =  input_file.readline()
	for _ in range(4 - row_id):
		next(input_file)
	return result
def process_input(input_file):
	number_of_tests = int(input_file.readline())
	result = []
	for i in range(number_of_tests):
		input_result = input_format
		input_result.first_row = retrieve_row(input_file)
		input_result.second_row = retrieve_row(input_file)
		result += ["Case #"+str(i+1)+": "+process(input_result)]
	return result
def process(input_result):
	result = list(set(input_result.first_row.split()) & set(input_result.second_row.split()))
	if len(result) > 1:
		return "Bad magician!"
	if len(result) < 1:
		return "Volunteer cheated!"
	return result[0]

args = parse_arguments()
input_file = open(args.input_file, 'r')
output_file = open( args.output_file, 'w')
output_file.write("\n".join(process_input(input_file)))
