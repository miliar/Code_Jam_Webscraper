
import sys
import string
import math
import psyco
psyco.full()



def is_solution(values):
	#print values
	for index in range(len(values)):
		a=  index + 1;
		b = int(values[index])
		#print a, b
		if   a < b: 
			return False;
		
	return True;


def Adj(u):
	result = [];
	for  index in xrange(len(u) - 1):
		temp = list(u);
		temp[index],temp[index+1] = temp[index+1],temp[index]
		if not tuple(temp) == tuple(u):
			result.append(temp);
	return result;


def BFS(s):
	if is_solution(s):
		return 0;
		
		
	cache = {}

	white = {}
	gray = {}
	black = {}


	distance = {}
	parent = {}

	tuple_s = tuple(s)
	
	gray[tuple_s] = True;
	
	distance[tuple_s] = 0;
	
	queue = []
	queue.append(s);
	while queue:
		u = queue.pop(0);
		tuple_u = tuple(u)
		for  v in  Adj(u):
			tuple_v = tuple(v);
			if not gray.has_key(tuple_v) and not black.has_key(tuple_v):
				gray[tuple_v] = True;
				distance[tuple_v] = distance[tuple_u] + 1
				if is_solution(v):
					return distance[tuple_v];
				parent[tuple_v]= tuple_u
				queue.append(v);
		black[tuple_u] = True;
	#error
	



def count_position_of_last_one(str):
	count = 0;
	for index in range(len(str)):
		if str[index] =='1':
			count = index + 1;
	return count;
	
	
	

def find_solution_for(input_file):
	number_of_rows = int(input_file.readline());
	source = [];
	for index in xrange(number_of_rows):
		source.append(count_position_of_last_one( input_file.readline()))
	return  BFS(source);	
	
	
def solve_problem_D(input_file_path , output_file_path):
		
	input_file = open(input_file_path,"r");
	output_file = open(output_file_path,"w");
	
	test_case_count  = int(input_file.readline());

	for index in xrange(test_case_count):
		solution_string = "Case #%d: %d"%(index+1 , find_solution_for(input_file));			
		print solution_string;
		output_file.write(solution_string+'\n');

	
	input_file.close()
	output_file.close()

	
	
	
	
	
def  start_me_up():
	if len(sys.argv) == 1:
		print "Usage:"
		print "%s input_file_path [output_file_path]" % ( sys.argv[0]);		
		print "Note: Solution is output to console too." ;		
		#solve_problem_D( "A-small-attempt0.in" , "A-small-attempt0.out");

	elif len(sys.argv) == 2:
		solve_problem_D(sys.argv[1], sys.argv[1]+'.out');
	
	elif len(sys.argv) >= 3:	
		solve_problem_D(sys.argv[1], sys.argv[2]);
		
		
		
		
		


if __name__ == "__main__":
	start_me_up();






