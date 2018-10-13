#!/usr/bin/env python
# encoding: utf-8
"""
tictactoe.py

Created by Gilles de Hollander on 2013-04-13.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import numpy as np

INPUT_FILE = 'A-large.in'

def parse_data(input_data):
    lines = [e.replace('\n', '') for e in input_data.readlines()]
    n_cases = int(lines[0])
    
    cases = []
    for case_n in range(n_cases):
        case = np.zeros((4, 4), dtype='str')
        for i in range(4):
            case[i,:] = list(lines[((case_n) * 5) + i + 1])
        cases.append(case)
    return cases
    

def solve_case(case):
    X_board = case.copy()
    Y_board = case.copy()
    X_board[X_board == 'T'] = 'X'
    Y_board[Y_board == 'T'] = 'O'

    for board, winner in zip([X_board, Y_board], ['X', 'O']):    
        if (board.T == winner).all(axis=0).any() or (board.T == winner).all(axis=1).any() or (board.diagonal() == winner).all() or (np.fliplr(board).diagonal() == winner).all():
            return '%s won' % winner

    if np.sum(case == '.') == 0:
        return 'Draw'

    return 'Game has not completed'
    
cases = parse_data(open(INPUT_FILE))

result = open('result.txt', 'w')

for i, case in enumerate(cases):
    result.write('Case #%d: %s\n' % (i+1, solve_case(case)))

result.close()