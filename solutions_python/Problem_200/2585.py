import numpy as np
import os

def parse_input(file_path):
    with open(file_path) as f:
        lines = [l.strip() for l in f.readlines()]
    n_test_cases = int(lines[0])
    test_cases = [tuple(number_str) for number_str in lines[1:]]
    return test_cases

def solve_test_case(test_case):
    out_list = just_solve(list(test_case))
    return int("".join(out_list))

def just_solve(digit_list):
    right_idx = len(digit_list) - 1
    left_idx = right_idx - 1
    
    while True:
        digit_left = int(digit_list[left_idx])
        digit_right = int(digit_list[right_idx])
        if digit_left > digit_right:
            digit_list[left_idx] = str(digit_left -1)
            digit_list[right_idx:] = ['9'] * (len(digit_list) - right_idx)
        left_idx -= 1
        right_idx -= 1

        if left_idx < 0:
            break
    return digit_list

file_name = "B-large.in"


input_path = os.path.join("input", file_name)
output_path = os.path.join("output", file_name)
test_cases =  parse_input(input_path)

output_str_list = []
for i, test_case in enumerate(test_cases):
     print "Test case %i/%i: %s" % (i+1, len(test_cases), str(test_case))
     min_flips = solve_test_case(test_case)
     output_str = "Case #%i: %s" % (i+1, str(min_flips))
     output_str_list.append(output_str)
     print(output_str + "\n")
 
with open(output_path, 'w') as f: 
    f.write("\n".join(output_str_list))
