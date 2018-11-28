#!/usr/bin/env python
import math

def solve(read):
    [L, P, C] = read_int_line(read)
    count = 0
    #while True:
    #    if (P/L < C or (P/L == C and P%L == 0)):
    #        break
    #    count += 1
    #    cC = float(P)/L
    #    L = int(L * math.sqrt(cC))
    
    cC = float(P)/L
    while cC > C:
        cC = math.sqrt(cC)
        count += 1
        
    return count

def main():
    solve_n_cases(solve)

##### PROBLEM VARIABLES ######

INFILENAME = 'B-large.in'
OUTFILENAME = 'output.out'

##### PROBLEM TEMPLATE ######

def init_io():
    read = open(INFILENAME, 'rt')
    write = open(OUTFILENAME, 'wt')
    return (read, write)

def deinit_io(read, write):
    read.close()
    write.close()
    
def read_token_line(read, tokenparsefunction):
    return [tokenparsefunction(x)
                for x in read.readline().split()]
    
def read_int_line(read):
    return read_token_line(read, int)
    
def output_case_sharp(write, casenum, result):
    write.write( 'Case #{0}: {1}\n'.format(casenum, result) )

def solve_n_cases(case_function, output_function = output_case_sharp):
    read, write = init_io()
    
    cases_num = int(read.readline())
    current_case = 1
    
    while (cases_num>0):
        case_result = case_function(read)
        output_function(write, current_case, case_result)
        
        cases_num -= 1
        current_case += 1
        
    
    deinit_io(read, write)

main()