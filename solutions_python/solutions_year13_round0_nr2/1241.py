# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 08:47:41 2013

@author: Ivan Koblik
"""

import sys

if len(sys.argv) <= 1:
    print "Expected input file name"
    exit(0)

def read_cases(from_file):
    with open(from_file) as f:
        lines = f.readlines()
    num_samples = int(lines[0])
    result = []
    current_row = 1
    for i in range(num_samples):
        N, M = map(int, lines[current_row].split(" "))
        case = map(lambda s: map(int, s.split(" ")), lines[current_row+1:current_row+1+N])
        result.append(case)
        current_row += 1+N
    return result

def max_in_rows(field):
    return [max(row) for row in field]
        
def max_in_columns(field):
    rotated = map(lambda *x: x, *field)
    return max_in_rows(rotated)

def check_field(field):
    N = len(field)
    M = len(field[0])
    max_row = max_in_rows(field)
    max_col = max_in_columns(field)
    for i in range(N):
        for j in range(M):
            val = field[i][j]
            if val < max_row[i] and val < max_col[j]:
                return False
    return True

fields = read_cases(sys.argv[1])
for i in range(len(fields)):
    field = fields[i]
    message = "Case #" + str(i+1) + ": "
    if check_field(field):
        message += "YES"
    else:
        message += "NO"
    print message
