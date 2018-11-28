#!/usr/bin/env python


def rotate_and_grav(board):
    
    board.reverse()
    new_board = []
    size = len(board)
    for l in board:
        for x in xrange(size-1, 0, -1):
            while l[x] == '.' and ('B' in l[0:x] or 'R' in l[0:x]):
                l.pop(x)
                l.insert(0, '.')
    for i in xrange(0, size):
        new_board.append([x[i] for x in board])
    
    return new_board

def find_winners(board, k):
    
    res = set()
    
    size = len(board)
    
    for l in board:
        string = ''.join(l)
        
        if string.find('R'*k) != -1:
            res.add('R')
        if string.find('B'*k) != -1:
            res.add('B')
        if len(res) == 2:
            return res
    for i in xrange(size):
        string = ''.join([x[i] for x in board])
        if string.find('R'*k) != -1:
            res.add('R')
        if string.find('B'*k) != -1:
            res.add('B')
        if len(res) == 2:
            return res
    for i in xrange(0, size-k+1):
        i2 = i
        j2 = 0
        string = []
        while i2 < size and j2 < size:
            string.append(board[i2][j2])
            j2 += 1
            i2 += 1
        string = ''.join(string)
        if string.find('R'*k) != -1:
            
            res.add('R')
        if string.find('B'*k) != -1:
            
            res.add('B')
        if len(res) == 2:
            return res
    for i in xrange(1, size-k+1):
        i2 = 0
        j2 = i
        string = []
        while i2 < size and j2 < size:
            string.append(board[i2][j2])
            j2 += 1
            i2 += 1
        string = ''.join(string)
        if string.find('R'*k) != -1:
            
            res.add('R')
        if string.find('B'*k) != -1:
            
            res.add('B')
        if len(res) == 2:
            return res
    for i in xrange(k-1, size):
        i2 = i
        j2 = 0
        string = []
        while i2 >= 0 and j2 < size:
            string.append(board[i2][j2])
            j2 += 1
            i2 -= 1
        string = ''.join(string)
        if string.find('R'*k) != -1:
            
            res.add('R')
        if string.find('B'*k) != -1:
            
            res.add('B')
        if len(res) == 2:
            return res
    for j in xrange(1, size-k+1):
        i2 = size-1
        j2 = j
        string = []
        while i2 >= 0 and j2 < size:
            string.append(board[i2][j2])
            j2 += 1
            i2 -= 1
        string = ''.join(string)
        if string.find('R'*k) != -1:
            
            res.add('R')
        if string.find('B'*k) != -1:
            
            res.add('B')
        if len(res) == 2:
            return res
    return res
    

if __name__ == '__main__':
    
    test_case = int(raw_input())
    for i in range(1, test_case+1):
        n, k = map(int, raw_input().split(' '))
        board = []
        for j in range(n):
            board.append(list(raw_input()))
        board = rotate_and_grav(board)
        groups = find_winners(board, k)
        if len(groups) == 0:
            print "Case #%d: Neither" % (i,)
        elif len(groups) == 2:
            print "Case #%d: Both" % (i,)
        elif list(groups)[0] == 'R':
            print "Case #%d: Red" % (i,)
        else:
            print "Case #%d: Blue" % (i,)
