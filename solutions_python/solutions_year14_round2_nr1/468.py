import sys
import math

case_nums=0
num_of_lines=1


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
	num_of_lines=int(data[1])+1
	data_length=len(data)

	"""Edit start_index here"""
	start_index=1
	case_num=1
	start=1
	for i in xrange(0,case_nums):

		num_of_lines=int(data[start])+1
		#print num_of_lines
		problem=data[start:start+num_of_lines]
		process_input_case(case_num,problem)
		case_num+=1
		start+=num_of_lines



def process_input_case(case_num,problem):
	"""Process raw input into apropriate type"""
	problem_variable=problem[1:]
	solve(case_num,problem_variable)

def solve(case_num,problem_variable):
	"Solve each problem"
	n=len(problem_variable)
	compressed_word=[]
	word1=problem_variable[0]
	char1=''
	for c in word1:
		if c==char1:
			continue
		compressed_word.append(c)
		char1=c

	max_num=[]
	for i in xrange(len(compressed_word)):
		max_num.append(0)

	
	total_num=[]
	for i in xrange(n):
		total_num.append([])

	for i,word in enumerate(problem_variable):
		w_ind=0
		for index in range(len(compressed_word)):
			c=compressed_word[index]
			num=0
			while (w_ind<len(word)) and (c==word[w_ind]) :
				num+=1
				w_ind+=1
			if num==0:
				print_ans(case_num,	 "Fegla Won")
				return
				


			total_num[i].append(num)
			if num>max_num[index]:
				max_num[index]=num
		if word[-1]!=compressed_word[-1]:
			print_ans(case_num,	 "Fegla Won")
			return

	num_of_operation=[]
	for i in xrange(len(compressed_word)):
		num_of_operation.append(1000)

	for i in xrange(len(compressed_word)):
		operation_list=[]
		for j in xrange(1,max_num[i]+1):
			operations=0
			for word in total_num:
				operations+=abs(word[i]-j)
			operation_list.append(operations)
		num_of_operation[i]=min(operation_list)

	total_sum=0
	for i in xrange (len(compressed_word)):
		total_sum+=num_of_operation[i]

	print_ans(case_num,	 total_sum)










def main():

	input_file=sys.argv[1]
	input_processor(input_file)


if __name__=="__main__":
	main()




	


