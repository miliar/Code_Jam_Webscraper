#!/usr/bin/python
# Input to stdin, output to stdout. 
# Python 2/3 compatible

import fileinput
input_data = list() 
for line in fileinput.input():
    input_data.append(line)

class SolTestCase: 
    first_ans = -1
    second_ans = -1
    first_possible_values = set()
    second_possible_values = set()
    def __init__(self, raw_input_lines, starting_index):
        self.first_ans = int(raw_input_lines[starting_index])
        self.first_possible_values = set(raw_input_lines[starting_index + 
                                                         self.first_ans].split())
        self.second_ans = int(raw_input_lines[starting_index + 5])
        self.second_possible_values = set(raw_input_lines[starting_index + 5 + 
                                                          self.second_ans].split())
    def output(self, case_num):
        possible_values = self.first_possible_values.intersection(self.second_possible_values)
        result_str = "Alpha Particles Hitting RAM"
        if (len(possible_values) == 0):
            result_str = "Volunteer cheated!"
        elif (len(possible_values) > 1):
            result_str = "Bad Magician!"
        elif (len(possible_values) == 1):
            result_str = str(list(possible_values)[0])
        print ("Case #{0}: {1}".format(case_num, result_str))
               
test_cases = int(input_data[0])
cur_row = 1
for i in range(0, test_cases):
    case = SolTestCase(input_data, cur_row)
    case.output(i + 1)
    cur_row += 10
    
