from math import ceil

#FILE_PATH = "B-small-attempt0.in"
#OUTPUT_FILE_PATH = 'B-small-attempt0.out'

FILE_PATH = "B-large.in"
OUTPUT_FILE_PATH = 'B-large.out'

#FILE_PATH = "example.txt"
#OUTPUT_FILE_PATH = 'example.out'

def read_file(path):
	with open(path, 'rb') as f:
		lines = f.readlines()
		test_cases = [line for line in lines[1:]]
		for (i, test_case) in enumerate(test_cases):
			if test_case.endswith('\n'):
				test_cases[i] = test_case[:-1]
	#print test_cases
	return test_cases

def output_solution(solution, path):
	lines = []
	with open(path, 'wb') as f:
		for (i, sol) in enumerate(solution):
			lines += ['Case #{index}: {solution}\n'.format(index=i+1, solution=sol)]
		f.writelines(lines)
    
# The only interesting function in this file
def solve_test_case(test_case):
    #import ipdb; ipdb.set_trace()
    N, R, O, Y, G, B, V = map(int, test_case.split(' '))
    color_numbers = ['R', 'Y', 'B', 'G', 'V', 'O']
    if R > 0 and R == G:
        if Y == 0 and B == 0:
            return 'RG' * R
        else:
            return 'IMPOSSIBLE'
    if Y > 0 and Y == V:
        if R == 0 and B == 0:
            return 'YV' * Y
        else:
            return 'IMPOSSIBLE'
    if B > 0 and B == O:
        if Y == 0 and R == 0:
            return 'BO' * B
        else:
            return 'IMPOSSIBLE'
    R2 = R - G
    Y2 = Y - V
    B2 = B - O
    colors = [(0, R2), (1, Y2), (2, B2)]
    colors.sort(key=lambda x: x[1])
    final_stables = ''
    small, medium, large = colors[0][1], colors[1][1], colors[2][1]
    if small + medium < large:
        return 'IMPOSSIBLE'
    num1 = large - medium
    first_str = color_numbers[colors[2][0]] + color_numbers[colors[0][0]]
    final_stables = final_stables + first_str * num1
    num2 = small - num1
    second_str = first_str + color_numbers[colors[1][0]]
    final_stables = final_stables + second_str * num2
    num3 = large - small
    third_str = color_numbers[colors[2][0]] + color_numbers[colors[1][0]]
    final_stables = final_stables + third_str * num3
    
    # === splitting only by R G and B 
    rep_r = 'RG' * G + 'R'
    final_stables = final_stables.replace('R', rep_r, 1)
    rep_y = 'YV' * V + 'Y'
    final_stables = final_stables.replace('Y', rep_y, 1)
    rep_b = 'BO' * O + 'B'
    final_stables = final_stables.replace('B', rep_b, 1)
    
    assert len(final_stables) == N, "wrong length of string! test case: %s" % test_case
    
    return final_stables
    
if __name__ == "__main__":
	test_cases = read_file(FILE_PATH)
	solution = [solve_test_case(test_case) for test_case in test_cases]
	#print solution
	output_solution(solution, OUTPUT_FILE_PATH)