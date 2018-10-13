#!/usr/bin/env python
import sys


RESULT = ('Game has not completed', 'X won', 'O won', 'Draw')


def main():
    T = int(sys.stdin.readline())

    for i in range(T):
        # result index
        ri = 3

        # X, O, .
        mr = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        mc = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        # diagonal left-to-right, right-to-left
        md = [[0, 0], [0, 0]]

        # read rows
        for j in range(4):
            s = sys.stdin.readline().strip()

            # iterate char in a row
            for k, c in enumerate(s):
                if c == 'X' or c == 'T':
                    mr[j][0] += 1
                    mc[k][0] += 1

                    if j == k:
                        md[0][0] += 1

                    if (j + k) == 3:
                        md[1][0] += 1

                if c == 'O' or c == 'T':
                    mr[j][1] += 1
                    mc[k][1] += 1

                    if j == k:
                        md[0][1] += 1

                    if (j + k) == 3:
                        md[1][1] += 1

                if c == '.':
                    mr[j][2] += 1
                    mc[k][2] += 1

                # Check if 'X' wins
                if mr[j][0] == 4 or mc[k][0] == 4 or \
                   md[0][0] == 4 or md[1][0] == 4:
                    ri = 1

                # Check if 'O' wins
                if mr[j][1] == 4 or mc[k][1] == 4 or \
                   md[0][1] == 4 or md[1][1] == 4:
                    ri = 2

        # If no winner, check for draw or not completed
        if ri != 1 and ri != 2:
            # Check for not completed
            if mr[j][2] > 0 or mc[k][2] > 0:
                ri = 0

        # space after test case
        sys.stdin.readline()

        print 'Case #%d: %s' % (i+1, RESULT[ri])

if __name__ == '__main__':
    main()
