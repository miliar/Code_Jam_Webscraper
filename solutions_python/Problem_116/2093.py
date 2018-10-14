#!/usr/bin/python

in_file_name = raw_input('in file: ')
in_file = open(in_file_name)
out_file = open(in_file_name.split('.')[0]+'.out', 'w')

T = int(in_file.readline())

def test_one_line(line):
    if '.' in line:
        return None
    if 'O' in line and 'X' in line:
        return None
    if 'X' in line:
        return 'X'
    if 'O' in line:
        return 'O'

for i in range(T):

    board = [in_file.readline() for _ in range(4)]
    _ = in_file.readline()

    lines = board[:] 
    for j in range(4): 
            lines.append([board[_][j] for _ in range(4)])
    lines.append([board[_][_] for _ in range(4)]) 
    lines.append([board[_][3-_] for _ in range(4)])

    result = None
    for line in lines:
        result = test_one_line(line)
        if result:
            break 

    out_file.write('Case #%i: ' % (i+1))
    if result in ['X', 'O']:
        out_file.write('%s won' % result)
    elif not '.' in ''.join(board):
        out_file.write('Draw')
    else:
        out_file.write('Game has not completed')
    if i < T-1: out_file.write('\n')
          
out_file.close()
        
