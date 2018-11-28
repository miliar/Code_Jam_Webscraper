import sys, itertools
import numpy as np

lines_per_case = 4
winningX = set(('XXXX', 'XXXT', 'XXTX', 'XTXX', 'TXXX'))
winningO = set(('OOOO', 'OOOT', 'OOTO', 'OTOO', 'TOOO'))
r = range(4)
xwon = 'X won'
owon = 'O won'
tstr = lambda x: ''.join(x)

def solve_case(case):
    lines = [line.strip() for line in case[:4]]
    transp_lines = map(tstr, zip(*lines))

    diagonals = (''.join((lines[i][i] for i in r)), 
            ''.join(lines[i][3-i] for i in r))

    winner = get_winner(lines)
    if not winner:
        winner = get_winner(transp_lines)
    if not winner:
        winner = get_winner(diagonals)
    if not winner:
        # draw?
        if '.' in ''.join(case):
            return 'Game has not completed'
        else:
            return 'Draw'

    return winner


def get_winner(lines):
    for line in lines:
        if line in winningX:
            return xwon
        if line in winningO:
            return owon
    return None


def produce_output(index, solution):
    print 'Case #%s: %s' % (index, solution)


def get_test_cases(lines, n_of_lines_per_case=1):
    x = 0
    while x < len(lines):
        y = x + n_of_lines_per_case
        yield lines[x:y+1]
        x = y+1

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        fn = sys.argv[1]
        with open(fn) as f:
            lines = f.readlines()
            nt = int(lines[0])
            for index, case in enumerate(get_test_cases(lines[1:], lines_per_case), 1):
                solution = solve_case(case)
                produce_output(index, solution)
