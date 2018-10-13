#!/usr/bin/python

import sys

def slide_right(row,N,gravity=True):
    pieces = [p for p in row if p != "."]
    return "." * (N - len(pieces)) +  ''.join(pieces)


def check(seqs,K,colour):
    for s in seqs:
        if colour * K in s:
###            print seqs
###            print s
            return True

def make_diagonals(seqs,N,d):
    diagonals = []
    for i in xrange(N):
        if d == "left":
            diagonals.append("." * i + seqs[i] + "." * (N - i))
        else:
            diagonals.append("." * (N - i) + seqs[i] + "." * i)
    return diagonals


T = int(raw_input())

for test_case in xrange(T):
    N, K = [int(x) for x in raw_input().split()]
    board = []
    for i in xrange(N):
        row = slide_right(sys.stdin.readline().strip(), N)
        board.append(row)
###    print "\n".join(board )
    columns = ["".join([ board[i][j] for i in xrange(N)]) for j in xrange(N)]
    longer = make_diagonals(board,N, "left")
    left_diagonals = ["".join([ longer[i][j] for i in xrange(N)]) for j in xrange(2*N)]
    
    longer = make_diagonals(board,N, "right")
    right_diagonals = ["".join([ longer[i][j] for i in xrange(N)]) for j in xrange(2*N)]

            
    # stupid, but still O(n). given that n < 50, should be okay
    blue = check(board,K, "B") or check(columns,K,"B") or check(right_diagonals,K,"B") or check(left_diagonals, K,"B") 
    red = check(board,K, "R") or check(columns,K,"R") or check(right_diagonals,K,"R") or check(left_diagonals,K,"R")

    if blue and red:
        result = "Both"
    elif blue:
        result = "Blue"
    elif red:
        result = "Red"
    else:
        result = "Neither"
    print "Case #%d: %s" % (test_case + 1, result)

