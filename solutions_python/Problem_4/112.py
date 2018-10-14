#!/usr/bin/env python2.5

"""
Google Code Jam 2008
Solution for the "Minimum Scalar Product" problem.
rbp@isnomore.net

Usage: scalar.py input_file output_file
"""

import sys

def read_input():
    in_file = file(sys.argv[1])

    in_text = in_file.readlines()
    n_cases = int(in_text.pop(0))
    cases = []
    for i in range(n_cases):
        vector_size = int(in_text.pop(0))
        cases.append({'v1': [int(i) for i in in_text.pop(0).split()]})
        cases[-1].update({'v2': [int(i) for i in in_text.pop(0).split()]})
        cases[-1].update({'size': vector_size})
        #print scalar(cases[-1]['v1'], cases[-1]['v2'])
    in_file.close()
    return cases

def scalar(v1, v2):
    return sum([i*j for i, j in zip(v1, v2)])

def solve_case(c):
    v1 = c['v1'][:]
    v2 = c['v2'][:]
    v1.sort()
    v2.sort(reverse=True)
    return scalar(v1, v2)

if __name__ == '__main__':
    cases = read_input()
    #print cases
    output = "\n".join(['Case #%d: %d' % (i+1, solve_case(c))
                        for i, c in enumerate(cases)])
    if len(sys.argv) < 3:
        print output
    else:
        out_file = file(sys.argv[2], "w")
        out_file.write(output)
        out_file.close()
