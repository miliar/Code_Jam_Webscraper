
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



class Prison:
	def __init__(self):
		self.is_empty = False;



def count_coins_for_release(prison_list, release_index):
	prison_count = len(prison_list);
	
	coin_count = 0;
	
	for index in range(release_index +1 , prison_count):
		if prison_list[index].is_empty:
			break;
		else:
			coin_count+=1;
			
	for index in range(1 , release_index +1 ):
		if prison_list[release_index - index].is_empty:
			break;
		else:
			coin_count+=1;
	return coin_count;




def count_total_coins( prison_list, release_order_list):
	coins = 0;
	
	for release_index in release_order_list:
		prison_list[release_index -1].is_empty = True;
		coins+= count_coins_for_release(prison_list,release_index -1)	

	return coins;


def find_minimum_count( prison_count , release_list):
	minimum_count = 99999999999999999999;
	best_order = None;
	
	for p in all_perms(release_list):
		prison_list = [ Prison() for x in xrange(prison_count) ]
		count =  count_total_coins(prison_list , p)
		if count < 	minimum_count:
			minimum_count = count;
			best_order = p

	#print best_order
	
	return minimum_count



def find_solution(input_file):
	prison_count , release_count = input_file.readline().split();	
	release_list = input_file.readline().split()
	for index in xrange(len(release_list)):
		release_list[index] = int(release_list[index])
	return find_minimum_count(int(prison_count),release_list )







def solve_problem_C(input_file_path , output_file_path):
		
	input_file = open(input_file_path,"r");
	output_file = open(output_file_path,"w");
	
	test_case_count  = int(input_file.readline());

	for index in xrange(test_case_count):
		solution_string = "Case #%d: %d"%(index+1 , find_solution(input_file));			
		print solution_string;
		output_file.write(solution_string+'\n');

	
	input_file.close()
	output_file.close()

	
	
	
	
	
def  start_me_up():
	if len(sys.argv) == 1:
		print "Usage:"
		print "%s input_file_path [output_file_path]" % ( sys.argv[0]);		
		print "Note: Solution is output to console too." ;		
		#solve_problem_C("test.in", 'test.out');
		
	elif len(sys.argv) == 2:
		solve_problem_C(sys.argv[1], sys.argv[1]+'.out');
	
	elif len(sys.argv) >= 3:	
		solve_problem_C(sys.argv[1], sys.argv[2]);
		
		
		
		
		


if __name__ == "__main__":
	start_me_up();






