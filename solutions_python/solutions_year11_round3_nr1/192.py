#!/usr/bin/python

import operator, math, re, os, sys
from optparse import OptionParser

def parseOptions():
    parser = OptionParser()
    parser.add_option('-i', '--input', dest = 'input', help = 'Input file', default = 'A-large.in')
    # parser.add_option('-o', '--output', dest = 'output', help = 'Output file', default = 'output.txt')
    (options, args) = parser.parse_args()
    return options

def readParameters(options):
    input = open(options.input)
    n = int(input.readline().strip())
    rows, columns, boards = [], [], []
    for i in xrange(n):
        vals = input.readline().strip().split()
        rows.append(int(vals[0]))
        columns.append(int(vals[1]))
        board = []
        for j in xrange(rows[i]):
            board.append(list(input.readline().strip()))
        boards.append(board)
    return n, rows, columns, boards

def changeColor(rows, columns, board):
    for y in xrange(rows):
        for x in xrange(columns):
            if board[y][x] == '#':
                if x+1 >= columns or y+1 >= rows:
                    return '\nImpossible'
                if board[y][x+1] == board[y+1][x] == board[y+1][x+1] == '#':
                    board[y][x] = '/'
                    board[y+1][x+1] = '/'
                    board[y][x+1] = '\\'
                    board[y+1][x] = '\\'
                else:
                    return '\nImpossible'
    result = '\n'
    for y in xrange(rows):
        result += ''.join(board[y])
        if y < rows - 1:
            result += '\n'
    return result

def main(options):
    n, rows, columns, boards = readParameters(options)
    results = []
    for i in xrange(n):
        result = changeColor(rows[i], columns[i], boards[i])
        results.append('Case #%d: %s' % (i+1, result))
    open(options.input.replace('.in', '.out'), 'w').write('\n'.join(results))
    for r in results:
        print r

if __name__ == "__main__":
    options = parseOptions()
    main(options)
