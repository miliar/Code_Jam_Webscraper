'''
Google code jam 2013
Qualification Round
Tic-Tac-Toe-Tomek

By Tyrus Tenneson
2013-04-12
'''

import sys
import collections
import re

'''
Solution
'''
def check_line(line):
    winner = None
    draw = True
    counter = collections.Counter(line)
    if '.' in counter:
        draw = False
    has_t = 'T' in counter
    if counter['X'] + has_t == 4:
        winner = 'X'
    elif counter['O'] + has_t == 4:
        winner = 'O'
    return (winner, draw)

def eval_case(case):
    '''
    Returns solution to case
    '''
    draw = True
    winner = None
    # check rows
    for row in case:
        (winner, row_draw) = check_line(row)
        if not row_draw:
            draw = False
        if winner:
            break
    # check cols
    for i in range(len(case)):
        if winner:
            break
        col = []
        for row in case:
            col.append(row[i])
        (winner, col_draw) = check_line(col)
        if not col_draw:
            draw = False
        if winner:
            break        
    # check down diag
    diag = []
    for i in range(len(case)):
        if winner:
            break
        diag.append(case[i][i])
        (winner, diag_draw) = check_line(diag)
        if not diag_draw:
            draw = False
        if winner:
            break
    # check up diag
    diag = []
    for i in range(len(case))[::-1]:
        if winner:
            break
        diag.append(case[i][len(case)-i-1])
        (winner, diag_draw) = check_line(diag)
        if not diag_draw:
            draw = False
        if winner:
            break                
    if winner:
        return_me = "%s won" % (winner)
    elif draw:
        return_me = "Draw"
    else:
        return_me = "Game has not completed"
    return return_me
            
'''
I/O
'''
def process_input(file_path):
    '''
    Returns list of strings, each string is a case.
    '''
    with open(file_path, 'r') as input:
        # first line is number of cases
        num_cases = int(input.readline().rstrip())
        lines = list(case.rstrip() for case in input.readlines())
    cases = []
    case = []
    for line in lines:
        if not line:
            cases.append(tuple(case))
            case = []
        else:
            case.append(tuple([char for char in line]))
    cases.append(tuple(case))
    cases.remove(tuple())
    cases = tuple(cases)
    return cases

def solve(file_path):
    cases = map(lambda case: eval_case(case), process_input(file_path))
    with open('output.txt', 'w') as out:
        for idx, val in enumerate(cases):
            write_string = "Case #%i: %s\n" % (idx+1, val)
            out.write(write_string)

if __name__ == "__main__":
    #solve('./test.in')
    #solve('./A-small-attempt0.in')
    solve('./A-large.in')

    
