#!/usr/bin/python

# Tic-Tac-Toe-Tomec

import sys
import os
from itertools import chain


def _get_cases(raw):
    """Takes a raw list of strings/lines and turn into cases.
    """
    raw[0] = int(raw[0])
    step = len(raw[1:])/raw[0]
    cases = []
    for i in range(1,len(raw),step):
        c = raw[i:i+step]
        cases.append(c)
    return cases

def parse_input(filename):
    print filename
    raw = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n')
            if line:
                raw.append(line.strip('\n'))
    return _get_cases(raw)

def get_boards(filename):
    """Turn into a tic tac toe case matrix.
    """
    cases = parse_input(filename)
    matrix = []
    for lcase in cases:
        case = []
        for s in lcase:
            case.append(list(s))
        matrix.append(case)
    return matrix

def _check_rows(board):
    for row in board:
        j = ''.join(sorted(row))
        if j == 'XXXX' or j == 'TXXX':
            return 'X'
        elif j == 'OOOO' or j == 'OOOT':
            return 'O'

def get_winner(board):    

    w = _check_rows(board) #check horizontal
    if w: return w 
    w = _check_rows(zip(*board)) #check vertical
    if w: return w
    
    b = board
    diags = [
        [b[0][0],b[1][1],b[2][2],b[3][3]],
        [b[0][3],b[1][2],b[2][1],b[3][0]]]
    
    w = _check_rows(diags) #check diagonal
    if w: return w

    if not '.' in [i for i in chain(*board)]:
        return 'D' #draw
    else:
        return 'N' #not finished
        
def write_out(results):
    with open(os.path.join(os.path.dirname(__file__), 'output.txt'), 'w') as f:
        for i, b in enumerate(results):
            winner = b
            if i>0: f.write('\n')
            cp = 'Case #{}: '.format(i+1)
            if winner in 'XO':
                s = cp+winner+' won'
            elif winner == 'D':
                s = cp+'Draw'
            elif winner == 'N':
                s = cp+'Game has not completed'
            f.write(s)
        

def run(filename):
    boards = get_boards(filename)
    write_out([get_winner(b) for b in boards])

def main(inputf):
    inputf = os.path.join(os.path.dirname(__file__), inputf)
    run(inputf)

if __name__ == '__main__':
    main(sys.argv[1])
    
