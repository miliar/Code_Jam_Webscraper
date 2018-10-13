#!/usr/bin/python

import collections

def solution(case, text):
    with open("output.txt", "a") as output_file:
        output_file.write("Case #{0}: {1}\n".format(case, text))

with(open("input.txt", "r")) as input_file:
    test_cases = input_file.readline()
    nested_dict = lambda: collections.defaultdict(nested_dict)
    chosen_lines = nested_dict()
    
    for i in range(1, int(test_cases) + 1):
        for j in range(2):
            line = int(input_file.readline())
            for k in range(1,5):
                possible_line = input_file.readline()
                if(k == line):
                   possible_line = possible_line[:-1]
                   chosen_lines[j] = possible_line.split(' ')
            final_set = set(chosen_lines[0]).intersection(chosen_lines[1])
            
        if len(final_set) == 0:
            solution(i, "Volunteer cheated!")
        elif len(final_set) == 1:
            solution(i, str(list(final_set)[0]))
        else:
            solution(i, "Bad magician!")
        chosen_lines = nested_dict()

