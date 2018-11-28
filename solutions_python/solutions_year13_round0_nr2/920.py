#!/usr/bin/env python
# encoding: utf-8
"""
lawn.py

Created by Gilles de Hollander on 2013-04-13.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import numpy as np

INPUT_FILE = 'B-large.in'

def parse_data(input_data):
    lines = [e.replace('\n', '') for e in input_data.readlines()]
    n_cases = int(lines[0])
    
    cases = []
    
    new=  True    
    
    for line in lines[1:]:
        
        if new:
            dimensions = [int(e) for e in line.split()]
            current_row = 0
            current_case = np.zeros(dimensions)
            new = False
            
        else:
            current_case[current_row, :] = [int(e) for e in line.split()]
            current_row += 1
            if current_row == dimensions[0]:
                cases.append(current_case)
                new = True
        
        
    return cases

def check_possible2(case):
    for row in np.arange(case.shape[0]):

        for col in np.where(case[row, :] < np.max(case[row, :]))[0]:
            if (case[:, col] > case[row, col]).any():
                return 'NO'



    return 'YES'

cases = parse_data(open(INPUT_FILE))

result = open('result.txt', 'w')

for i, case in enumerate(cases):
    result.write('Case #%d: %s\n' % (i+1, check_possible2(case)))

result.close()
