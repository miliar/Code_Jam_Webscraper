
import sys
import string
import re


def make_pattern( input_string):
	pattern_string = input_string.translate(string.maketrans("()","[]") , " \t");
	return re.compile(pattern_string);
	


def solve_alien_language_problem(input_file_path , output_file_path):
		
	input_file = open(input_file_path,"r");
	output_file = open(output_file_path,"w");
	
	word_len, word_count, pattern_count  = input_file.readline().split();
	word_len, word_count, pattern_count = int(word_len) , int(word_count) , int(pattern_count)  
	
	word_list = [];
	
	for index in xrange(word_count):
		word_list.append(input_file.readline());
	
	for index in xrange(pattern_count):
		pattern = make_pattern( input_file.readline());
		
		match_count = 0;
		
		for word in word_list:
			if pattern.match(word) is not None:
				match_count+=1;
		
		solution_string = "Case #%d: %d"%(index+1,match_count);			
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
		solve_alien_language_problem(sys.argv[1], sys.argv[1]+'.out');
	
	elif len(sys.argv) >= 3:	
		solve_alien_language_problem(sys.argv[1], sys.argv[2]);
		


if __name__ == "__main__":
	start_me_up();














