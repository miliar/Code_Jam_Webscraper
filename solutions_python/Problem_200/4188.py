import sys
import pdb

infput_file = sys.argv[1]
output_file = "output_tidy.txt"

def create_result_line(position, number):
	return "Case #{0}: {1}\n".format(position, number)

def is_tidy(number):
	number_string = str(number)
	return "".join(sorted(number_string)) == number_string


def solve(number):
	while not(is_tidy(number)) & (number > 0):
		number = number -1
	return number


with open(infput_file) as in_file:
	with open(output_file, 'w') as out_file:

	    file_lines = in_file.readlines()
	    T = (int)(file_lines[0])
	    for i in range(1,len(file_lines)):
	    	number = int(file_lines[i])
	    	highest_tidy = solve(number)
	    	line = create_result_line(i, highest_tidy)
	    	out_file.write(line)
