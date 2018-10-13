#!/usr/bin/env python
"""
5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW

Case #1: [E, A]
Case #2: [R, I, R]
Case #3: [F, D, T]
Case #4: [Z, E, R, A]
Case #5: []
"""
import sys
import re

class TestCase:
    n_C_pattern = re.compile(r'^\s*(\d+)(.*)$')
    C_pattern = re.compile(r'^\s*(\w)(\w)(\w)(.*)$')
    n_D_pattern = n_C_pattern
    D_pattern = re.compile('^\s*(\w)(\w)(.*)$')
    n_N_pattern = n_C_pattern
    N_pattern = re.compile('^\s*(\w)(.*)$')

    def __init__(self, case_number, input_line):
        match = TestCase.n_C_pattern.match(input_line)
        n_C = int(match.group(1))
        input_line = match.group(2)
        C_dict = {}
        for i in range(n_C):
            match = TestCase.C_pattern.match(input_line)
            C_dict[match.group(1) + match.group(2)] = match.group(3)
            C_dict[match.group(2) + match.group(1)] = match.group(3)
            input_line = match.group(4)

        match = TestCase.n_D_pattern.match(input_line)
        n_D = int(match.group(1))
        input_line = match.group(2)
        D_dict = {} 
        for i in range(n_D):
            match = TestCase.D_pattern.match(input_line)
            D_dict[match.group(1)] = match.group(2)
            D_dict[match.group(2)] = match.group(1)
            input_line = match.group(3)

        match = TestCase.n_N_pattern.match(input_line)
        n_N = int(match.group(1))
        input_line = match.group(2)
        N_list = []
        for i in range(n_N):
            match = TestCase.N_pattern.match(input_line)
            N_list.append(match.group(1))
            input_line = match.group(2)

        result_list = []
        for N in N_list:
            add_to_result = True
            check_deletion = True
            if (len(result_list) > 0) and ((result_list[-1] + N) in C_dict):
                N = C_dict[result_list[-1] + N]
                result_list.pop()
                check_deletion = False

            if check_deletion and (N in D_dict) and (D_dict[N] in result_list):
                result_list = []
                #while (result_list[-1] != D_dict[N]):
                #    result_list.pop()
                #result_list.pop()
                add_to_result = False

            if add_to_result:
                result_list.append(N)

        print('Case #' + str(case_number) + ': [' + ', '.join(result_list) + ']')

if len(sys.argv) < 2:
    print('Please specify input file')
    exit()

try:
    f = open(sys.argv[1])
except:
    print('Failed to open input file')
    exit()

n_test_cases = int(f.readline())
for i in range(n_test_cases):
    TestCase(i+1, f.readline())

f.close()
