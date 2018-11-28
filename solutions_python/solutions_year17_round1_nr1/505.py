#!/usr/bin/python
#-*- coding: utf-8 -*-

''' Template for Google Code Jam '''

import sys

def main():
    ''' main '''
    case_num = int(sys.stdin.readline())
    for i in range(1, case_num+1):
        line = sys.stdin.readline().rstrip()
        args = line.split(' ')
        row = int(args[0])
        col = int(args[1])
        lines = []
        for j in range(0, row):
            line = sys.stdin.readline().rstrip()
            lines.append(list(line))
        answer = solve(lines, row, col)
        print('Case #{0:d}:'.format(i))
        for r in range(row):
            print(''.join(map(str, lines[r])))

def solve(lines, row, col):
    ''' solve problem '''
    # ->
    for r in range(row):
        key = '?'
        for c in range(col):
            if lines[r][c] == '?':
                lines[r][c] = key
            else:
                key = lines[r][c]

    # <-
    for r in range(row):
        key = '?'
        for c in reversed(range(col)):
            if lines[r][c] == '?':
                lines[r][c] = key
            else:
                key = lines[r][c]
        
    # v
    for c in range(col):
        key = '?'
        for r in range(row):
            if lines[r][c] == '?':
                lines[r][c] = key
            else:
                key = lines[r][c]

    # ^
    for c in range(col):
        key = '?'
        for r in reversed(range(row)):
            if lines[r][c] == '?':
                lines[r][c] = key
            else:
                key = lines[r][c]

    return 'Solved'

if __name__ == '__main__':
    main()
