#!/usr/bin/python
'''
Google code jam 2013
Round 1B
Osmos

By Tyrus Tenneson
2013-05-04
'''

import sys
import collections
import math
import re

'''
Solution
'''
def brute_force(lst):
    '''
    0th element is current mote

    we can either choose to add a guy or remove a guy
    '''
    # base case
    if len(lst) == 1:
        return 0
    current, next_ = lst[0], lst[1]
    if current > next_:
        return brute_force([current + next_] + lst[2:])
    if current == 1:
        return len(lst) - 1
    removed_next_lst = [current] + lst[2:]
    new_next_lst = [2*current - 1] + lst[1:]
    removed = brute_force(removed_next_lst)
    new_ = brute_force(new_next_lst)
    return_me = min(removed, new_)
    return 1 + return_me

def eval_case(case):
    '''
    Returns solution to case
    '''
    start, num_motes = case[0]
    motes = sorted(case[1])
    return brute_force([start] + list(motes))
    
'''
I/O
'''
def chunks(l, n):
    '''
    Yield successive n-sized chunks from l.
    http://stackoverflow.com/a/312464
    '''
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def process_case_lines(case_lines):
    if type(case_lines) == tuple:
        return_me = []
        for line in case_lines:
            return_me.append(tuple(map(int, line.rstrip().split(' '))))
        return tuple(return_me)
    else:
        return tuple(map(int, case_lines.rstrip().split(' ')))

def process_input():
    '''
    Returns list of strings, each string is a case.
    '''
    with sys.stdin as input:
        # first line is number of cases
        num_cases = int(input.readline().rstrip())
        lines = tuple(input.readlines())
        if len(lines)/num_cases != 1:
            lines = chunks(lines, len(lines)/num_cases)
        cases = tuple(map(process_case_lines, lines))
    return cases

def solve():
    cases = map(eval_case, process_input())
    for idx, val in enumerate(cases):
        write_string = "Case #%i: %s\n" % (idx+1, val)
        print write_string,

if __name__ == "__main__":
    solve()