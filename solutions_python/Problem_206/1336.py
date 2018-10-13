import os
import numpy as np

def parse_input(file_path):
    with open(file_path) as f:
        lines = [l.strip() for l in f.readlines()]
    n_test_cases = int(lines[0])
    test_cases = []
    current_line_idx = 1
    for i in range(1,n_test_cases+1):
        dest_kilometers, n_horses = [int(number) for number in lines[current_line_idx].split()]
        horses = []
        for m in range(1, n_horses+1):
            horse_lst = lines[current_line_idx+m].split()
            horses.append({"initial_km": float(horse_lst[0]),
                           "max_speed": float(horse_lst[1])})
        current_line_idx += n_horses+1
        test_cases.append({"case_no": i, 
                           "destination_km": float(dest_kilometers),
                           "horses": horses})
    return test_cases

def solve_test_case(test_case):
    destination_km = test_case["destination_km"]
    
    time_to_dest = -float("inf")
    for horse in test_case['horses']:
        horse_time_to_dest = (destination_km - horse['initial_km'])/horse['max_speed']
        time_to_dest = max(time_to_dest, horse_time_to_dest)
    max_travel_speed = destination_km/time_to_dest
    
    return max_travel_speed


file_name = "A-large.in"

# Parse test cases
input_path = os.path.join("input", file_name)
output_path = os.path.join("output", file_name)
test_cases =  parse_input(input_path)
 
# Solve test cases
output_str_list = []
for i, test_case in enumerate(test_cases):
     print "Test case %i/%i: %s" % (i+1, len(test_cases), str(test_case))
     answer = solve_test_case(test_case)
     output_str = "Case #%i: %s" % (i+1, str(answer))
     output_str_list.append(output_str)
     print(output_str + "\n")
  
with open(output_path, 'w') as f: 
    f.write("\n".join(output_str_list))
