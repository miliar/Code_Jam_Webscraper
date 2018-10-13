#!/usr/bin/python

import sys

def readints(f):
    a = [int(s) for s in f.readline().split()]
    return a

def readint(f):
    return int(f.readline())

def readmatrix(f, rows):
    matrix = []
    for i in xrange(rows):
        matrix += [readints(f)]
    return matrix

def check(v, x):
    return all([c == x for c in v])

def getContents(board, n, m):
    contents = set([board[i][j] for i in xrange(n) for j in xrange(m)])
    contents = [x for x in contents]
    contents.sort()
    return contents

def possible(board, n, m):
    while len(board) > 0 and len(board[0]) > 0:
        contents = getContents(board, n, m)
        test = contents[0]
        deleted = False
        rem = -1
        for r in xrange(n):
            if check(board[r], test):
                rem = r
        if rem > -1 and (len(board) > 0 and len(board[0]) > 0):
            board.pop(rem)
            n -= 1
            deleted = True
        else:
            for c in xrange(m):
                if check([board[i][c] for i in xrange(n)], test):
                    rem = c
            if rem > -1 and (len(board) > 0 and len(board[0]) > 0):
                for r in xrange(n):
                    board[r].pop(rem)
                m -= 1
                deleted = True
        if (not deleted) and (len(board) > 0 and len(board[0]) > 0):
            return 'NO'
    return 'YES'

if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    numCases = readint(f)
    for i in xrange(numCases):
        print "Case #%d:" % (i + 1),
        n, m = readints(f)
        board = readmatrix(f, n)
        print possible(board, n, m)
