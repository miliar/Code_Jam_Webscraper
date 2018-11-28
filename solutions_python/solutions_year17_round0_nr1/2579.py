import sys
import math


    
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
    """Process raw input into apropriate type"""
    problem = problem[0].split(" ");
    k = int(problem[1])
    problem_variable = []
    for i in xrange(len(problem[0])):
        problem_variable.append(problem[0][i] == "+")
    
    solve(case_num,problem_variable, k)

def solve(case_num,problem_variable,k):
    result = 0
    for i in  xrange(len(problem_variable)- k + 1):
        if not problem_variable[i]:
            result +=1
            for j in xrange(k):
                problem_variable[i+j] = not problem_variable[i+j]

    if False in problem_variable[-k:]:
        print_ans(case_num, "IMPOSSIBLE")
    else:
        print_ans(case_num, result)

def main():
    input_file=sys.argv[1]
    input_processor(input_file)


if __name__=="__main__":
    main()