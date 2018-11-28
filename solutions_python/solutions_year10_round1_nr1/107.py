#!/usr/bin/env python

import re, sys

def rotate_row(row):
    pieces = row.replace('.', '')
    return '.'*(len(row) - len(pieces)) + pieces

def get_diagnols_incr(b, n, r, c):
    m = min(n-r, n-c)
    return ''.join(b[r+i][c+i] for i in xrange(m))

def get_diagnols_decr(b, n, r, c):        
    m = min(n-r, c+1)
    return ''.join(b[r+i][c-i] for i in xrange(m))

def solve(n, k, board):
    new_board = [rotate_row(row) for row in board]
    rows = [row for row in new_board]

    cols = []
    for c in xrange(n):
        col = ''.join(new_board[r][c] for r in xrange(n))
        cols.append(col)

    # max diag len is n
    sz = n - k + 1
    diagnols = [None]*(sz*4)
    for i in xrange(sz):
        o = i * 4
        diagnols[o+0] = get_diagnols_incr(new_board, n, 0, i)
        diagnols[o+1] = get_diagnols_incr(new_board, n, i, 0)
        diagnols[o+2] = get_diagnols_decr(new_board, n, 0, n-i-1)
        diagnols[o+3] = get_diagnols_decr(new_board, n, i, n-1)

    lines = rows + cols + diagnols
    red  = re.compile(r'.*R{%d}.*' % k)
    blue = re.compile(r'.*B{%d}.*' % k)
    has_red, has_blue = False, False
    for line in lines:
        if not has_red:
            has_red = red.match(line) is not None
        if not has_blue:
            has_blue = blue.match(line) is not None
        if has_red and has_blue:
            return 'Both'
    if has_red:
        return 'Red'
    elif has_blue:
        return 'Blue'
    return 'Neither'               

def main():
    lines = sys.stdin.readlines()
    T = int(lines[0])
    
    case = 1
    i = 1
    while True:
        N, K = lines[i].split(' ')
        N = int(N)
        K = int(K)
        i += 1
        board = [lines[i+j].strip() for j in xrange(N)]
        i += N
        output = solve(N, K, board)
        print 'Case #%d: %s' % (case, output)
        if case == T:
            return
        case += 1

if __name__ == '__main__': main()
