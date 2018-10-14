import sys
import math

case_nums=0
num_of_lines=1;

def print_ans(case_num,solution):
	print("Case #"+str(case_num)+":"),
	print_solution(solution)


def print_solution(solution):
	"""TO DO"""
	print solution

def input_processor(filename):
	f=open(filename)
	data=f.read().split("\n")
	case_nums=int(data[0])

	"""Insert number of lines per test case here"""
	num_of_lines=10
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
	"""Process raw input into apropriate type"""


	problem_variable=[]
	for i in xrange(len(problem)):
		problem_variable.append(problem[i].split(" "))

	for i in xrange(len(problem_variable)):
		for j in xrange (len(problem_variable[i])):
			problem_variable[i][j]=int(problem_variable[i][j])


	solve(case_num,problem_variable)

def solve(case_num,problem_variable):
	"Solve each problem"
	ans1=problem_variable[0][0]
	ans2=problem_variable[5][0]
	arrangement1=problem_variable[1:5]
	arrangement2=problem_variable[6:]

	possible1=arrangement1[ans1-1]
	possible2=arrangement2[ans2-1]
	ans=[]

	for item in possible1:
		if item in possible2:
			ans.append(item)

	if len(ans)==0:
		solution="Volunteer cheated!"
	if len(ans)==1:
		solution=ans[0]
	if len(ans)>1:
		solution="Bad magician!"
	print_ans(case_num,	 solution)


def main():
	input_file=sys.argv[1]
	input_processor(input_file)


if __name__=="__main__":
	main()




	


