#!/usr/bin/python
# Input to stdin, output to stdout. 
# Python 2/3 compatible

import fileinput
input_data = list() 
for line in fileinput.input():
    input_data.append(line)

class SolTestCase: 
    def __init__(self, A, B, K):
        self.A = A
        self.B = B
        self.K = K
    def output(self, case_num):
        brutef_winners = 0;
        for i in reversed(range(0, A)):
            for j in reversed(range(0, B)):
                 if (i & j) < K:
                     brutef_winners += 1
        print ("Case #{0}: {1}".format(case_num, brutef_winners))
                
               
test_cases = int(input_data[0])
cur_row = 1
for i in range(0, test_cases):
    A = int(input_data[cur_row].split()[0])
    B = int(input_data[cur_row].split()[1])
    K = int(input_data[cur_row].split()[2])
    case = SolTestCase(A, B, K)
    case.output(i + 1)
    cur_row += 1
    
