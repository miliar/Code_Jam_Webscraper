#!/usr/bin/python

import re
import sys
from string import maketrans

input_file = open('A-large.in')
output_file = open('A-large.out', 'w')

T = int(input_file.readline())

def complete(board):
    for i in xrange(4):
        for u in xrange(4):
            if board[i][u] == '.':
                return False
    return True

def ch(board, row):
    first = board[row][0]
    if first == '.': return ''
    if first == 'T':
        first = board[row][1]
        if first == '.': return ''
    for i in xrange(1, 4):
        if not board[row][i] in ('T', first):
            return ''
    return first + ' won'

def cv(board, col):
    first = board[0][col]
    if first == '.': return ''
    if first == 'T':
        first = board[1][col]
        if first == '.': return ''
    for i in xrange(1, 4):
        if not board[i][col] in ('T', first):
            return ''
    return first + ' won'

def cd1(board):
    first = board[0][0]
    if first == '.': return ''
    if first == 'T':
        first = board[1][1]
        if first == '.': return ''
    for i in xrange(1, 4):
        if not board[i][i] in ('T', first):
            return ''
    return first + ' won'

def cd2(board):
    first = board[3][0]
    if first == '.': return ''
    if first == 'T':
        first = board[2][1]
        if first == '.': return ''
    for i in xrange(1, 4):
        if not board[3-i][i] in ('T', first):
            return ''
    return first + ' won'

for t in range(T):
    board = [[] for i in xrange(4)]
    board[0] = list(input_file.readline().replace('\n',''))
    board[1] = list(input_file.readline().replace('\n',''))
    board[2] = list(input_file.readline().replace('\n',''))
    board[3] = list(input_file.readline().replace('\n',''))
    
    for i in xrange(4):
        result = ch(board, i)
        if result != '': break
        result = cv(board, i)
        if result != '': break
    else:
        result = cd1(board)
        if result == '':
            result = cd2(board) 
    if result == '':
        if not complete(board):
            result = "Game has not completed"
        else:
            result = 'Draw'   
    output_file.write("Case #" + str(t + 1) + ": " + result + "\n")
    
    input_file.readline()

input_file.close()
output_file.close()
