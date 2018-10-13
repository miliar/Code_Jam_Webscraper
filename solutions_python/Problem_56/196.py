#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(N, foo):
        res = []
        for _ in xrange(N):
                res.append(foo())
        return res
def readlinearray(foo): return map(foo, raw_input().split())

def get_vboard(board):
    nboard = []
    for _ in xrange(len(board)):
        nboard.append([])
        
    for y in xrange(len(board)):
        line = board[y]
        for x in xrange(len(line)):
            nboard[x].append(line[x])
    
    for i in xrange(len(nboard)):
        nboard[i] = ''.join(nboard[i])
    
    return nboard

def get_dboard(board):
    nboard = []
    N = len(board)
#    for _ in xrange(N * 2 - 1):
#        nboard.append([])
    
    #Horizontal (L -> R)
#    print 'Horizontal (L -> R)'
    for p in xrange(N):
        x, y = p, 0
        l = []
        while True:
            try:
#                l.append(board[x][y])
                l.append(board[y][x])
            except IndexError:
                break
            x += 1
            y += 1
#        print l
        nboard.append(l)
    
    #Vertical (L -> R)
#    print 'Vertical (L -> R)'
    for p in xrange(1, N):
        x, y = 0, p
        l = []
        while True:
            try:
#                l.append(board[x][y])
                l.append(board[y][x])
            except IndexError:
                break
            x += 1
            y += 1
#        print l
        nboard.append(l)

    #Horizontal (R -> L)
#    print 'Horizontal (R -> L)'
    for p in xrange(N):
        x, y = p, 0
        l = []
        while True and x >= 0:
            try:
#                l.append(board[x][y])
                l.append(board[y][x])
            except IndexError:
                break
            x -= 1
            y += 1
#        print l
        nboard.append(l)
    
    
    #Vertical (R -> L)
#    print 'Vertical (R -> L)'
    for p in xrange(1, N):
#        x, y = 0, p
        x, y = N-1, p
        l = []
        while True and x >= 0:
            try:
#                l.append(board[x][y])
                l.append(board[y][x])
            except IndexError:
                break
            x -= 1
            y += 1
#        print l
        nboard.append(l)

    for i in xrange(len(nboard)):
        nboard[i] = ''.join(nboard[i])
    
    return nboard

#"Red", "Blue", "Neither", or "Both"
def have_k_pieces(board, k):
    
    vboard = get_vboard(board)
    dboard = get_dboard(board)
    
#    print 20 * '#b'
#    printboard(board)
#    print 20 * '#v'
#    printboard(vboard)
#    print 20 * '#d'
#    printboard(dboard)
#    print 20 * '#'
    
    letter = 'R'
    ol = 'B'
    R = find_hor(k, letter, ol, board) or find_ver(k, letter, ol, vboard) or find_diag(k, letter, ol, dboard)

    letter = 'B'
    ol = 'R'
    B = find_hor(k, letter, ol, board) or find_ver(k, letter, ol, vboard) or find_diag(k, letter, ol, dboard)
    
    if R and B:
        return 'Both'
    
    if R:
        return 'Red'
    
    if B:
        return 'Blue'
    
    return 'Neither'

def find_hor(k, l, ol, board):
    for line in board:
        for nl in [v.replace('.','') for v in line.split(ol)]:
            if len(nl) >= k:
                return True
    return False

find_ver = find_hor
#def find_ver(k, l, ol,board):
#    return find_hor(k, l, ol, board)

find_diag = find_hor

#def find_diag(k, l, ol,board):
#    pass

def printboard(board):
    for l in board:
        print ''.join(l)

if __name__ == '__main__':
    T = readint()
    for t in xrange(1, T+1):
        N, K = readlinearray(int)
        board = []
        for l in xrange(N):
            line = raw_input()
            line = line.replace('.', '')
            line = line.rjust(N, '.')
            board.append(line)
#        board = rotate(N, board)
#        board = push_left(board)
#        print len(board)
#        printboard(board)
        
        ans = have_k_pieces(board, K)
        print 'Case #%d: %s' % (t, ans)
