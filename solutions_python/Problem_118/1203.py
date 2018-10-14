#!/usr/bin/env python
# encoding: utf-8
"""
square_and_fair.py

Created by Gilles de Hollander on 2013-04-13.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import numpy as np

INPUT_FILE = 'C-small-attempt0.in'

def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    
    return False

def parse_data(input_data):
    lines = [e.replace('\n', '') for e in input_data.readlines()]
    n_cases = int(lines[0])
    
    cases = []
    

    for case in range(n_cases):
        cases.append(tuple([int(e) for e in lines[case+1].split()]))
        
        
    return cases
    
def solve_interval(n1, n2):

    min_sqrt = np.ceil(np.sqrt(n1))
    max_sqrt = np.floor(np.sqrt(n2))


    sqrt_palindromes = filter(is_palindrome, np.arange(min_sqrt, max_sqrt+1, dtype=int))

    square_lambda_palindrome = lambda x: is_palindrome(np.square(x))

    return len(filter(square_lambda_palindrome, sqrt_palindromes))

cases = parse_data(open(INPUT_FILE))

result = open('result.txt', 'w')

for i, case in enumerate(cases):
    result.write('Case #%d: %s\n' % (i+1, solve_interval(*case)))

result.close()