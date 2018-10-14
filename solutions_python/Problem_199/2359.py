from math import ceil

FILE_PATH = "A-large.in"
OUTPUT_FILE_PATH = 'A-large.out'

ORD_PLUS = ord('+')
ORD_MINUS = ord('-')
ORD_PLUS_PLUS_MINUS = ORD_PLUS + ORD_MINUS

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
	
def solve_test_case(test_case):
    test_case = test_case.replace('+', '0')
    test_case = test_case.replace('-', '1')
    splitted_stack = test_case.split(' ', 1)
    stack, k = int(splitted_stack[0], 2), int(splitted_stack[1])
    xored_k = 2**k - 1
    count, cur_idx = 0, 0
    max_length = len(bin(stack)) - 2
    while stack > 0 and cur_idx < max_length:
        # If the current pancake is facing down (1):
        if stack & 2**cur_idx:
            stack ^= (xored_k << cur_idx)
            count += 1
        cur_idx += 1
    if stack != 0:
        count = 'IMPOSSIBLE'
    return count      
    
if __name__ == "__main__":
	test_cases = read_file(FILE_PATH)
	solution = [solve_test_case(test_case) for test_case in test_cases]
	print solution
	output_solution(solution, OUTPUT_FILE_PATH)