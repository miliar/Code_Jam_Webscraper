from math import ceil

#FILE_PATH = "B-small-attempt0.in"
#OUTPUT_FILE_PATH = 'B-small-attempt0.out'

FILE_PATH = "B-large.in"
OUTPUT_FILE_PATH = 'B-large.out'

def read_file(path):
	with open(path, 'rb') as f:
		lines = f.readlines()
		test_cases = [line for line in lines[1:]]
		for (i, test_case) in enumerate(test_cases):
			if test_case.endswith('\n'):
				test_cases[i] = test_case[:-1]
	print test_cases
	return test_cases

def output_solution(solution, path):
	lines = []
	with open(path, 'wb') as f:
		for (i, sol) in enumerate(solution):
			lines += ['Case #{index}: {solution}\n'.format(index=i+1, solution=sol)]
		f.writelines(lines)
	
# The only interesting function in this file
def solve_test_case(test_case):
    all_equal_index = 0
    cur_number = int(test_case[0])
    for i in xrange(1, len(test_case)):
        if int(test_case[i]) > cur_number:
            all_equal_index = i
            cur_number = int(test_case[i])
        elif int(test_case[i]) < cur_number:
            return int(test_case) - int(test_case[all_equal_index + 1:]) - 1
    return int(test_case)
    
if __name__ == "__main__":
	test_cases = read_file(FILE_PATH)
	solution = [solve_test_case(test_case) for test_case in test_cases]
	print solution
	output_solution(solution, OUTPUT_FILE_PATH)