
test_input = """
6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O
"""

def solve(case):
    case = case
    row = ''
    cols = ['', '', '', '']
    diag1, diag2 = '', ''
    for idx, x in enumerate('|'.join(case)):
        if x == '|':
            if row.replace('T', 'X') == 'XXXX':
                return 'X won'
            if row.replace('T', 'O') == 'OOOO':
                return 'X won'
            row = ''
        row += x
        if idx % 5 != 4:
            cols[idx%5] += x
        if idx % 6 == 0:
            diag1 += x
        if idx % 4 == 3:
            diag2 += x

    for col in cols:
        if col.replace('T', 'X') == 'XXXX':
            return 'X won'
        if col.replace('T', 'O') == 'OOOO':
            return 'O won'


    if diag1.replace('T', 'X') == 'XXXX':
        return 'X won'
    if diag1.replace('T', 'O') == 'OOOO':
        return 'O won'
    if diag2.replace('T', 'X') == 'XXXX':
        return 'X won'
    if diag2.replace('T', 'O') == 'OOOO':
        return 'O won'
    if '.' in ''.join(case):
        return 'Game has not completed'
    return 'Draw'

    
def run(input):
    lines = input.split()
    no = int(lines[0])
    lines = lines[1:]
    for i in range(no):
        print 'Case #%d: %s'%((i+1), solve(lines[i*4:i*4+4]))

if __name__ == '__main__':
    import sys
    input = sys.argv[1]
    run(open(input).read())
