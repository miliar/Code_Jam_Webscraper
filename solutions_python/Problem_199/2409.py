import numpy as np
import os

def parse_input(file_path):
    with open(file_path) as f:
        lines = [l.strip() for l in f.readlines()]
    n_test_cases = int(lines[0])
    test_cases = [{'pancakes': np.array([int(pk) for pk in lines[i].split()[0].replace("+","1").replace("-","0")]),
                  'flipper_size': int(lines[i].split()[1])} for i in range(1,n_test_cases+1)]
    return test_cases

def solve_test_case(test_case, minimum_flips):
    flipper = test_case['flipper_size']
    pancakes = test_case['pancakes']
    try:
        flips = iterative_solve(pancakes, flipper)
        return flips
    except:
        return "IMPOSSIBLE"

def recursive_solve(pancakes, flipper_size):
    if all_pancakes_are_happy(pancakes):
        return 0

    first_unhappy = np.where(pancakes==0)[0][0]
    if flip(pancakes, flipper_size, first_unhappy):
        flips = recursive_solve(pancakes, flipper_size)
        return flips+1
    else:
        raise ValueError

def iterative_solve(pancakes, flipper_size):
    flips = 0
    while True:
        if all_pancakes_are_happy(pancakes):
            return flips

        first_unhappy = np.where(pancakes==0)[0][0]
        if flip(pancakes, flipper_size, first_unhappy):
            flips += 1
        else:
            raise ValueError
    
def flip(pancakes, flipper, start_position):
    if start_position+flipper > len(pancakes):
        return False
    print "startposition: %i" % start_position
    print "flipper: %i" % flipper
    pancakes[start_position:start_position+flipper] = 1 - pancakes[start_position:start_position+flipper]
    print pancakes 
    return True
    

def all_pancakes_are_happy(pancakes):
    return pancakes.sum() == len(pancakes)


file_name = "A-large.in"
input_path = os.path.join("input", file_name)
print parse_input(input_path)
test_cases =  parse_input(input_path)

output_path = os.path.join("output", file_name)
output_str_list = []
for i, test_case in enumerate(test_cases):
    print "Test case %i/%i" % (i, len(test_cases))
    min_flips = solve_test_case(test_case, 0)
    output_str = "Case #%i: %s" % (i+1, str(min_flips))
    output_str_list.append(output_str)
    print(output_str + "\n")

with open(output_path, 'w') as f: 
    f.write("\n".join(output_str_list))
    