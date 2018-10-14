
import sys
import string
import math


import psyco
psyco.full()


def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]



def make_all_combinations(number_string):
	combinations = []
	for p in all_perms(number_string):
		try:
			combinations.index(int(p));
		except:	
			combinations.append(int(p))
	return combinations

def find_next_number(number_string):
	combinations = make_all_combinations(number_string + '0')
	combinations.sort();
	found_at = combinations.index(int(number_string))
	if found_at == len(combinations) -1:
		return combinations[  found_at ]
	return combinations[  found_at + 1]


def solve_problem_B(input_file_path , output_file_path):
		
	input_file = open(input_file_path,"r");
	output_file = open(output_file_path,"w");
	
	test_case_count  = int(input_file.readline());

	for index in xrange(test_case_count):
		number_string = input_file.readline().strip();
		solution_string = "Case #%d: %d"%(index+1 ,find_next_number(number_string ));			
		print solution_string;
		output_file.write(solution_string+'\n');

	
	input_file.close()
	output_file.close()

	
	
	
	
	
def  start_me_up():
	if len(sys.argv) == 1:
		print "Usage:"
		print "%s input_file_path [output_file_path]" % ( sys.argv[0]);		
		print "Note: Solution is output to console too." ;		
		solve_problem_B("test.in", 'test.out');
		
	elif len(sys.argv) == 2:
		solve_problem_B(sys.argv[1], sys.argv[1]+'.out');
	
	elif len(sys.argv) >= 3:	
		solve_problem_B(sys.argv[1], sys.argv[2]);
		
		
		
		
		


if __name__ == "__main__":
	start_me_up();






