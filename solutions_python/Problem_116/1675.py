'''
Created on Apr 1, 2013

@author: pawel
'''
import sys
 
def read_case_info(file):
    data = {}
    data['board'] = {}
    data['amount_of_empty'] = 0
    for i in range(4):
        raw_line = file.readline().strip('\n')
        for j in range(4):
            data['board'][(i,j)] = raw_line[j]
            if raw_line[j] == '.':
                data['amount_of_empty'] += 1
    file.readline()
    return data

def check(symbol, board, fields):
    for field in fields:
        if board[field] not in [symbol, 'T']:
            return False
    return True

def check_rows(symbol, board):
    for i in range(4):
        if check(symbol, board, [(i, j) for j in range(4)]):
            return True
    return False
def check_cols(symbol, board):
    for i in range(4):
        if check(symbol, board, [(j, i) for j in range(4)]):
            return True
    return False
def check_diagonals(symbol, board):
    if check(symbol, board, [(i, i) for i in range(4)]):
        return True
    
    if check(symbol, board, [(3 - i, i) for i in (range(4))]):
        return True
    return False

def has_won(symbol, board):
    if check_rows(symbol, board):
        return True
    if check_cols(symbol, board):
        return True
    if check_diagonals(symbol, board):
        return True
    return False

def solve_case(data):
    if has_won('X', data['board']):
        return 'X won'
    elif has_won('O', data['board']):
        return 'O won'
    elif data['amount_of_empty'] > 0:
        return 'Game has not completed'
    else:
        return 'Draw'

file = open(sys.argv[1], 'r')
number_of_cases = int(file.readline().strip())
counter = 0
results = []
while number_of_cases > counter:
    case_info = read_case_info(file)
    results.append(solve_case(case_info))
    counter += 1
    
file_output = open(sys.argv[2], 'w')
for index, result in enumerate(results):
    file_output.write('Case #' + str(index + 1) +  ': ' + result + '\n') 
