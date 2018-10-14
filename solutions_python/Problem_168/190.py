#!/bin/env python

input_file = None

import os
import sys


def main():
    cases = readone(int)
    output = []
    for case_num in range(1, cases + 1):
        result = None
        ### Begin solution code
        rows, cols = readmany(int)
        row_arrows = [0] * rows
        col_arrows = [0] * cols
        grid = []
        changed = 0
        for r in range(rows):
            line = []
            chars = readone(str)
            for c in chars:
                line.append(c)
            grid.append(line)
        pivots = []
        for r in range(rows):
            line = grid[r]
            for c in range(cols):
                character = line[c]
                if character == '.':
                    continue
                else:
                    row_arrows[r] += 1
                    col_arrows[c] += 1
                    pivots.append((r, c))
        for pivot in pivots:
            found = 0
            r, c = pivot
            if grid[r][c] == '<':
                for i in range(c):
                    if grid[r][i] != '.':
                        found = 1
                        break
            elif grid[r][c] == '>':
                for i in range(c + 1, cols):
                    if grid[r][i] != '.':
                        found = 1
                        break
            elif grid[r][c] == '^':
                for i in range(r):
                    if grid[i][c] != '.':
                        found = 1
                        break
            elif grid[r][c] == 'v':
                for i in range(r + 1, rows):
                    if grid[i][c] != '.':
                        found = 1
                        break
            if found:
                continue
            elif row_arrows[r] * col_arrows[c] == 1: # if both are 1
                result = 'IMPOSSIBLE'
                break
            else:
                changed += 1
        if result != 'IMPOSSIBLE':
            result = str(changed)

        ### End solution code
        output.append('Case #%d: ' % (case_num,) + str(result))
    output_file = open(output_filename, 'w')
    output_file.write('\n'.join(output))
    output_file.close()
    if output_filename.endswith('sample.out'):
        their_output = open('A-their-sample.out')
        for line_num, line in enumerate(output):
            their_line = their_output.readline().strip()
            if line == their_line:
                print line
            else:
                print line_num, ' yours :', line
                print line_num, ' theirs:', their_line
        their_output.close()
    else:
        print '\n'.join(output)

def readone(t):
    line = input_file.readline()
    assert(len(line.split()) == 1)
    return t(line.strip())

def readmany(t):
    return map(t, input_file.readline().split())

if __name__ == '__main__':
    input_file = sys.stdin
    output_filename = 'test.out'
    if os.path.exists('A-large.in'):
        input_file = open('A-large.in')
        output_filename = 'A-large.out'
    elif os.path.exists('A-small.in'):
        input_file = open('A-small.in')
        output_filename = 'A-small.out'
    elif os.path.exists('A-sample.in'):
        input_file = open('A-sample.in')
        output_filename = 'A-sample.out'
    main()
    input_file.close()