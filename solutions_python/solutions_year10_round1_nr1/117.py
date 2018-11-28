#!/usr/bin/env python

import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return map(int, sys.stdin.readline().split())

def read_line():
    return sys.stdin.readline().strip()

# this is extremely slow
def match(board, N, L, K):
    target = L * K
    for l in range(N):
        #print 'line:', "".join(board[l])
        if target in "".join(board[l]):
            #print 'linha'
            return True
        for c in range(N):
            column = "".join([board[i][c] for i in range(N)])
            #print 'column:', column
            if target in column:
                #print 'coluna'
                return True

            d1 = ""
            x = l
            y = c
            while  x < N and y < N:
                d1 += board[x][y]
                x += 1
                y += 1
            if target in d1:
                #print 'd1'
                return True
           
            d2 = ""
            x = l
            y = c
            while  x < N and y >= 0:
                d2 += board[x][y]
                x += 1
                y -= 1
            if target in d2:
                #print 'd2'
                return True
    return False

def solve():
    N, K = read_ints()
    board = []
    for i in range(N):
        board.append(list(read_line()))

    # rotate
    new_board = [[''] * N for i in range(N)]
    for l in range(N):
        for c in range(N):
            new_board[c][N - l - 1] = board[l][c]

    board = new_board
    for c in range(N):
       r = []
       for l in range(N):
           if board[l][c] != '.':
               r.append(board[l][c])
       
       r.reverse()
       while len(r) < N:
           r.append('.')
       r.reverse()
       for l in range(N):
           board[l][c] = r[l]

    #for x in board:
    #    print "".join(x)
    #print
    blue = match(board, N, 'B', K)
    red = match(board, N, 'R', K)

    if blue and red:
        print 'Both'
    elif blue:
        print 'Blue'
    elif red:
        print 'Red'
    else:
        print 'Neither'


def main():
    T = read_int()
    
    for case in xrange(1, T + 1):
        print 'Case #%d:' % case,
        solve()

if __name__ == '__main__':
    main()

