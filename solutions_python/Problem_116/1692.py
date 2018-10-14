import os
import sys

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'A-large.in'))
sys.stdout = open('out1.txt', 'wb')

cases = int(raw_input())
for i in range(cases):
    grid = [raw_input() for l in range(4)]
    if i < cases - 1:
        raw_input()

    s1 = grid[0]
    s2 = grid[1]
    s3 = grid[2]
    s4 = grid[3]

    hasEmptySpace = s1.find('.') != -1 or s2.find('.') != -1 or s3.find('.') != -1 or s4.find('.') != -1

    s5 = grid[0][0] + grid[1][0] + grid[2][0] + grid[3][0]
    s6 = grid[0][1] + grid[1][1] + grid[2][1] + grid[3][1]
    s7 = grid[0][2] + grid[1][2] + grid[2][2] + grid[3][2]
    s8 = grid[0][3] + grid[1][3] + grid[2][3] + grid[3][3]

    s9 = grid[0][0] + grid[1][1] + grid[2][2] + grid[3][3]
    s10 = grid[3][0] + grid[2][1] + grid[1][2] + grid[0][3]

    lst = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
    for l in lst:
        line = l.replace('T', 'K')
        O = line.strip('O')
        if not O or O == 'K':
            print 'Case #%d: O won' % (i + 1)
            break
        X = line.strip('X')
        if not X or X == 'K':
            print 'Case #%d: X won' % (i + 1)
            break
    else:
        if hasEmptySpace:
            print 'Case #%d: Game has not completed' % (i + 1)
        else:
            print 'Case #%d: Draw' % (i + 1)

sys.stdout.close()