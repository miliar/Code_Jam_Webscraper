#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import sys

# Internal imports (if any)

def getline():
    return sys.stdin.next().rstrip()

def get_ans_and_board():
    ans = int(getline().strip())
    board = list()
    for _ in xrange(4):
        board.append(getline().strip().split())
    return board[ans - 1]

def challenge():
    first_row = get_ans_and_board()
    second_row = get_ans_and_board()
    candidates = list(set(first_row) & set(second_row))
    if len(candidates) == 1:
        print candidates[0]
    elif len(candidates) == 0:
        print 'Volunteer cheated!'
    else:
        print 'Bad magician!'

# Main entry point
if __name__ == '__main__':
    testcases = int(getline())

    for testcase in xrange(1, testcases + 1):
        print 'Case #%d:' % (testcase, ),
        challenge()

