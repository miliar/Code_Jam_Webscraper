#!/usr/bin/python
# Input to stdin, output to stdout. 
# Python 2/3 compatible

import fileinput
input_data = list() 
for line in fileinput.input():
    input_data.append(line)

class SolTestCase: 
    C = -1
    F = -1
    X = -1
    def __init__(self, raw_input_lines, starting_index):
        vals = (raw_input_lines[starting_index].split())
        self.C = float(vals[0])
        self.F = float(vals[1])
        self.X = float(vals[2])


    def get_result_for(self, start_val):
        if (start_val == 0):
            return self.X/2.0
        
        val = 0.0
        i = start_val
        while (i > 0):
            cookies_per_second = (2.0 + (self.F * (start_val - i)))
            val += self.C/cookies_per_second
            i -= 1
        cookies_per_second = (2.0 + (self.F * (start_val)))
        return val + self.X/cookies_per_second
        
    def calc_res(self):
        last_res = self.X/2.0
        counter = 1
        while True:
            new_res = self.get_result_for(counter)
            if (new_res >= last_res):
                return last_res
            last_res = new_res
            counter += 1
            
        
    def output(self, case_num):
        print ("Case #{0}: {1}".format(case_num, self.calc_res()))
    
test_cases = int(input_data[0])
for i in range(0, test_cases):
    case = SolTestCase(input_data, i+1)
    case.output(i+1)
