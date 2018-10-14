#!/usr/bin/env python

import sys
import numpy as np


def solve(N):
    digits = map(int, str(N))
    
    problem = False
    for i in xrange(len(digits)-1):
        if digits[i] > digits[i+1]:
            problem = True
            break
    
    if not problem:
        return N
    
    for j in xrange(i, 0, -1):
        if digits[j-1] < digits[j]:
            return int(''.join(map(str, digits[0:j] + [digits[j] - 1] + [9]*(len(digits) - j- 1))))
            
    return int(''.join(map(str, [digits[0] - 1] + [9]*(len(digits) - 1))))


def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
        n_testcases = int(fin.readline().strip())
        
        for i_testcase in xrange(1, n_testcases + 1):
            line = fin.readline().strip()
            
            # Parse input line
            #input = map(int, line.split())
            N = int(line)
            
            # Solve
            res = solve(N)
            
            # Write solution
            fout.write('Case #{}: {}\n'.format(i_testcase, res))


if __name__ == '__main__':
    main()