
import sys
import string
import math
import psyco
psyco.full()



def determine_number( message_string):
	
	base={
	'1':2,
	'2':3,
	'3':4,
	'4':5,
	'5':6,
	'6':7,
	'7':8,
	'8':9,
	'9':10,
	'a':11,
	'b':12,
	'c':13,
	'd':14,
	'e':15,
	'f':16,
	'g':17,
	'h':18,
	'i':19,
	'j':20,
	'k':21,
	'l':22,
	'm':23,
	'n':24,
	'o':25,
	'p':26,
	'q':27,
	'r':28,
	's':29,
	't':30,
	'u':31,
	'v':32,
	'w': 33,
	'x': 34,
	'y' : 35,
	'z' : 36};
	
	max_character = '0'
	
	for character in message_string:
		if character > max_character:
			max_character = character;
			
			
	return int(message_string, base[max_character])		
	
	
	
	
	
def decode( message_string):
	symbol_table = {};
	
	decoded_message = ''
	
	values =[
	'1',
	'0',
	'2',
	'3',
	'4',
	'5',
	'6',
	'7',
	'8',
	'9',
	'a',
	'b',
	'c',
	'd',
	'e',
	'f',
	'g',
	'h',
	'i',
	'j',
	'k',
	'l',
	'm',
	'n',
	'o',
	'p',
	'q',
	'r',
	's',
	't',
	'u',
	'v',
	'w',
	'x',
	'y',
	'z' ];
	
	current_value_index = 0;

	
	for character in message_string:
		if not symbol_table.has_key(character):
			symbol_table[character] = values[current_value_index];
			current_value_index+=1;		
			
		decoded_message+=symbol_table[character]
	
	return determine_number(decoded_message);




def solve_problem_A(input_file_path , output_file_path):
		
	input_file = open(input_file_path,"r");
	output_file = open(output_file_path,"w");
	
	test_case_count  = int(input_file.readline());

	for index in xrange(test_case_count):
		solution_string = "Case #%d: %d"%(index+1 , decode(input_file.readline().strip()));			
		print solution_string;
		output_file.write(solution_string+'\n');

	
	input_file.close()
	output_file.close()

	
	
	
	
	
def  start_me_up():
	if len(sys.argv) == 1:
		print "Usage:"
		print "%s input_file_path [output_file_path]" % ( sys.argv[0]);		
		print "Note: Solution is output to console too." ;		
		
	elif len(sys.argv) == 2:
		solve_problem_A(sys.argv[1], sys.argv[1]+'.out');
	
	elif len(sys.argv) >= 3:	
		solve_problem_A(sys.argv[1], sys.argv[2]);
		
		
		
		
		


if __name__ == "__main__":
	start_me_up();






