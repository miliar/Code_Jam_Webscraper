#!/usr/bin/python
'''
Google code jam 2015
Qualification Round
Standing Ovation

By Tyrus Tenneson
2015-04-11
'''

import sys

'''
Solution
'''
def eval_case(case):
    '''
    Returns solution to case
    '''
    s_max, digits = case
    up = extra = 0
    for i, s in enumerate(digits):
        # Add more for this level...
        more = max(0, i - up)
        extra += more
        up += more + s
    return extra

'''
I/O
'''
def process_input():
    '''
    Reads stdin, returns tuple of tuples (s_max, (s_1, ...)).
    '''
    with sys.stdin as input:
        num_cases = int(input.readline().rstrip())
        cases = []
        for line in input.readlines():
            s_max, digits = line.strip().split(' ')
            digits = tuple([int(x) for x in digits])
            cases.append((s_max, digits))
        assert num_cases == len(cases)
    return cases

def solve():
    cases = map(eval_case, process_input())
    for idx, val in enumerate(cases):
        write_string = "Case #%i: %s\n" % (idx+1, val)
        print write_string,

if __name__ == "__main__":
    solve()
