#! /usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

input_filename = 'A-large.in'
output_filename = 'A-large.out'

# Size of the tic-tac-toe
size = 4
# The possible states and outputs
XWON, OWON, DRAW, NOTCOMPLETED, UNKNOWN = range(5)
outputs = dict({XWON: 'X won', OWON: 'O won', DRAW: 'Draw', NOTCOMPLETED: 'Game has not completed'})

def get_state(line):
    if '.' not in line:
        if 'O' not in line:
            return XWON
        if 'X' not in line:
            return OWON
    return UNKNOWN
    
def describe_state(case):
    # Check rows and columns
    for i in range(size):
        row = case[i:(i+1),:]
        state = get_state(row)
        if state != UNKNOWN:
            return outputs[state]
        
        column = case[:,i:(i+1)]
        state = get_state(column)
        if state != UNKNOWN:
            return outputs[state]
    
    # Check diagonals
    diagonal1 = case.diagonal()
    state = get_state(diagonal1)
    if state != UNKNOWN:
        return outputs[state]
    
    diagonal2 = case[:,::-1].diagonal()
    state = get_state(diagonal2)
    if state != UNKNOWN:
        return outputs[state]
    
    if '.' in case:
        return outputs[NOTCOMPLETED]
    else:
        return outputs[DRAW]


# Reading test cases
f = open(input_filename)
lines = f.readlines()
f.close()
no_test_cases = int(lines[0])
test_cases = []

# Populating the test_cases from the input
for i in range(no_test_cases):
    test_case = zeros((size,size), str)
    for n in range(size):
        for m in range(size):
            test_case[n,m] = lines[5*i+n+1][m]
    test_cases.append(test_case)

f = open(output_filename, 'a')
for i, test_case in enumerate(test_cases):
    f.write('Case #'+str(i+1)+': '+describe_state(test_case)+'\n')
f.close()
