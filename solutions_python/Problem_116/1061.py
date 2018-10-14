import sys
import os

import numpy as np

#bits to modify // check
win_X = 1
win_O = 2
full_board = 4

def check_board(board):
    lines = np.sum(board, axis=0)
    cols = np.sum(board, axis=1)
    diag = np.trace(board)
    antidiag = np.sum(board.flat[[3,6,9,12]])
    sums = np.hstack((lines, cols, diag, antidiag))

    result = 0
    if 3 in sums or 4 in sums:
        result |= win_X

    if 30 in sums or 40 in sums:
        result |= win_O

    if np.all(sums < 1000):
        result |= full_board

    return result

filename = sys.argv[1]

input_file = open(filename, 'r')
output_file = open(os.path.splitext(filename)[0] + '.out', 'w')

input_lines = input_file.readlines()
num_lines = int(input_lines[0])

input_lines = input_lines[1:]
for i in range(len(input_lines)):
    new_line = input_lines[i].replace('X','1,')
    new_line = new_line.replace('O','10,')
    new_line = new_line.replace('.','1000,') #If there is a dot, we are 100% sure this not a filled line/board.
    new_line = new_line.replace('T','0,')
    new_line = new_line.strip(',\n')
    if len(new_line) > 0:
        input_lines[i] = [int(val) for val in new_line.split(',')]

for i in range(num_lines):
    #5 lines per board, drop the trailing empty line.
    board = input_lines[i * 5:(i+1) * 5 - 1]
    board = np.array(board)
    result = check_board(board)

    output_file.write('Case #%i: ' % (i + 1))
    if result & win_X:
         output_file.write('X won\n')
    elif result & win_O:
        output_file.write('O won\n')
    elif result & full_board:
        output_file.write('Draw\n')
    else:
        output_file.write('Game has not completed\n')

output_file.close()