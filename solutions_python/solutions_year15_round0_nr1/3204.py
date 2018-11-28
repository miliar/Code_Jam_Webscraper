# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:33:52 2015

@author: nicolas
"""

import numpy as np

def interpret_input_file(input_filename):
    input_file = open(input_filename, 'r')
    num_of_test_cases = int(input_file.readline())
    testCases = {}
    for i in range(num_of_test_cases):
        line = str.split(input_file.readline())
        sMax = int(line[0])
        currentLine = []
        for k in range(sMax+1):
            currentLine.append(int(line[1][k]))
        testCases[i] = currentLine
    input_file.close()    
    return testCases

def compute_number_of_additional_persons(case):
    return max(0,-1*min(np.cumsum(case)-range(len(case)))+1)


def write_output(solution, output_filename):
    output_file = open(output_filename, 'w')
    for num, test_case in solution.iteritems():
        output_file.write("Case #{}: {}\n".format(num+1, test_case))
    output_file.close()



testCases = interpret_input_file("A-large.in")
solution = {}
for num, case in testCases.iteritems():
    solution[num] = compute_number_of_additional_persons(case)
write_output(solution,"output_file_large")


