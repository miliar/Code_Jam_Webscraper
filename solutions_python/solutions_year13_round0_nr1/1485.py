TTTSIZE = 4

def who_win_line(line):
    elements = set(line)
    if '.' in elements:
        return '.'
    elements.discard('T')
    if len(elements) >= 2:
        return 'D'
    else:
        return elements.pop()

def who_win_tic_tac_toe(original_rows):
    #print('%s' % repr(original_rows))
    board_full = True
    rows = [row[0:TTTSIZE] for row in original_rows]
    #print('%s' % repr(rows))
    columns = [ [rows[0][0], rows[1][0], rows[2][0], rows[3][0]],
            [rows[0][1], rows[1][1], rows[2][1], rows[3][1]],
            [rows[0][2], rows[1][2], rows[2][2], rows[3][2]],
            [rows[0][3], rows[1][3], rows[2][3], rows[3][3]] ]
    diagonal1 = [rows[0][0], rows[1][1], rows[2][2], rows[3][3]]
    diagonal2 = [rows[0][3], rows[1][2], rows[2][1], rows[3][0]]

    lines = rows
    lines.extend(columns)
    lines.append(diagonal1)
    lines.append(diagonal2)

    for line in lines:
        winner = who_win_line(line)
        if winner == 'X':
            return 'X won'
        elif winner == 'O':
            return 'O won'
        elif winner == '.':
            board_full = False
    if board_full:
        return 'Draw'
    else:
        return 'Game has not completed'


import sys
#import pdb

if __name__ == '__main__':
    filename_prefix = sys.argv[1]
    filename_in = filename_prefix + ".in"
    filename_out = filename_prefix + ".out"

    file_in = open(filename_in, 'r')
    lines = file_in.readlines()

    testcnt = int(lines[0])
    idx = 1

    file_out = open(filename_out, 'w')

    #pdb.set_trace()
    for test in range(testcnt):
        res = who_win_tic_tac_toe(lines[idx : idx + TTTSIZE])
        file_out.write("Case #{0}: {1}\n".format(test + 1, res))
        idx += TTTSIZE + 1
