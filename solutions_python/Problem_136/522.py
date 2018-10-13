import sys
import math

case_nums=0
num_of_lines=1;

def print_ans(case_num,solution):
	print("Case #"+str(case_num)+":"),
	print_solution(solution)


def print_solution(solution):
	"""TO DO"""
	print ("%.7f" % solution)

def input_processor(filename):
	f=open(filename)
	data=f.read().split("\n")
	case_nums=int(data[0])

	"""Insert number of lines per test case here"""
	num_of_lines=1
	data_length=len(data)

	"""Edit start_index here"""
	start_index=1
	case_num=1
	for i in xrange(0,case_nums):
		start=(i*num_of_lines)+start_index
		problem=data[start:start+num_of_lines]
		process_input_case(case_num,problem)
		case_num+=1


def process_input_case(case_num,problem):
	problem_variable=problem[0].split(" ")
	for i in xrange(len(problem_variable)):
		problem_variable[i]=float(problem_variable[i])

	solve(case_num,problem_variable)

def solve(case_num,problem_variable):
	"Solve each problem"
	current_rate=2.0
	farm_num=0
	farm_cost=problem_variable[0]
	farm_rate=problem_variable[1]
	goal=problem_variable[2]
	cookies=0.0
	state=True
	timer=0.0

	solution=0.0
	if goal<farm_cost:
		timer=goal/current_rate
	else:
		while state:
			timer+=farm_cost/current_rate
			if ((goal-farm_cost)/current_rate)<(goal/(current_rate+farm_rate)):
				timer+=(goal-farm_cost)/current_rate
				break
			else:
				current_rate+=farm_rate

	solution=timer
	print_ans(case_num,	 solution)


def main():
	input_file=sys.argv[1]
	input_processor(input_file)


if __name__=="__main__":
	main()




	


