import sys
import math

case_nums=0
num_of_lines=1;

def print_ans(case_num,solution):
	print("Case #"+str(case_num)+":"),
	print_solution(solution)


def print_solution(solution):
	"""TO DO"""
	print solution[0],solution[1]

def input_processor(filename):
	f=open(filename)
	data=f.read().split("\n")
	case_nums=int(data[0])

	"""Insert number of lines per test case here"""
	num_of_lines=3
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
	for i in xrange(1,3):
		problem_variable.append(problem[i].split(" "))
	for i in xrange(2):
		for j in xrange(len(problem_variable[i])):
			problem_variable[i][j]=float(problem_variable[i][j])
	solve(case_num,problem_variable)

def solve(case_num,problem_variable):
	"Solve each problem"

	naomi=problem_variable[0]
	ken=problem_variable[1]
	naomi1=sorted(naomi)[::-1]
	naomi2=naomi1[:]
	ken1=sorted(ken)[::-1]
	ken2=ken1[:]
	solution=[]
	plus=0

	while True:
		if checkALL(naomi1, ken1):
			break
		item1=naomi1.pop()
		item2=ken1[-1]
		if item1>item2:
			ken1.pop()
			plus+=1
		else:
			ken1.pop(0)

	solution.append(len(naomi1)+plus)

	while True:
		if check2(naomi2, ken2):
			break
		item=naomi2.pop()
		flag=0
		for i in range(1,len(ken2)):
			if ken2[-i]>item:
				flag=-i
				break
		ken2.pop(flag)

	solution.append(len(naomi2))

	print_ans(case_num,	 solution)

def checkALL(naomi,ken):
	for i in xrange(1,len(naomi)+1):
		if naomi[-i]<ken[-i]:
			return False
	return True

def check2(naomi2,ken2):
	if len(naomi2)<=0:
		return True
	if naomi2[-1]>ken2[0]:
		return True
	return False

def main():
	input_file=sys.argv[1]
	input_processor(input_file)


if __name__=="__main__":
	main()




	


