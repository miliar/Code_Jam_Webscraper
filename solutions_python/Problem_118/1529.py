#!/usr/bin/python
'''
Google code jam 2013
Qualification Round
Fair and Square

By Tyrus Tenneson
2013-04-12
'''

import sys
import collections
import math
import re

'''
Solution
'''
def is_palindrome(num):
    #print num, str(num) == str(num)[::-1]
    return str(num) == str(num)[::-1]

def get_fairs(min_, max_):
    return_me = []
    for n in range(int(math.ceil(min_**.5)), int(math.floor(max_**.5))+1):
        if is_palindrome(n) and is_palindrome(n**2):
            return_me.append(n**2)
    return tuple(return_me)

def eval_case(case, fairs):
    '''
    Returns solution to case
    '''
    a, b = case
    count = 0
    for n in fairs:
        if a <= n and n <= b:
            count += 1
    return count
            
'''
I/O
'''
def process_input():
    '''
    Returns list of strings, each string is a case.
    '''
    #with open(file_path, 'r') as input:
    with sys.stdin as input:
        # first line is number of cases
        num_cases = int(input.readline().rstrip())
        cases = tuple(tuple(map(int,case.rstrip().split(' '))) for case in input.readlines())
    return cases

def solve():
    fairs = get_fairs(1, 10**14)
    cases = map(lambda case: eval_case(case, fairs), process_input())
    for idx, val in enumerate(cases):
        write_string = "Case #%i: %s\n" % (idx+1, val)
        print write_string,

if __name__ == "__main__":
    solve()