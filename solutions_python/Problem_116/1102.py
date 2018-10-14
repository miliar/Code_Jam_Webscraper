#!env python2

import sys


def get_line_winner(line):
    if line[0] == '.':
        return None

    for c in line:
        if c != 'T' and c != line[0]:
            return None
    return line[0] + " won"


def get_verticals(lines):
    vertical_lines = []

    for x in range(4):
        vertical_lines.append([line[x] for line in lines])

    return vertical_lines


def get_diagonals(lines):
    return [
        [lines[0][0], lines[1][1], lines[2][2], lines[3][3]],
        [lines[0][3], lines[1][2], lines[2][1], lines[3][0]]
    ]


def check_board_state(lines):
    possible_lines = lines + get_verticals(lines) + get_diagonals(lines)

    for line in possible_lines:
        winner = get_line_winner(line)
        if winner is not None:
            return winner

    if '.' in ''.join(lines):
        return 'Game has not completed'
    else:
        return 'Draw'


def read_input():
    lines = []

    for line in sys.stdin.readlines()[1:]:
        line = line.strip()
        if line == '':
            yield lines
            lines = []
        else:
            lines.append(line)

    yield lines


case = 1
for lines in read_input():
    if len(lines) == 0: continue
    result = check_board_state(lines)
    print "Case #%d: %s" % (case, result)
    case += 1
