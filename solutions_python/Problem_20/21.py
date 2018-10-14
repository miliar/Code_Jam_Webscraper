#!/usr/bin/python

import sys

stdin = sys.stdin
buf = stdin.read().split()
buf_pos = -1

def next():
    global buf_pos
    buf_pos += 1
    return buf[ buf_pos ]

def next_int():
    return int( next() )

def next_time():
    hr, mn = next().split(':')
    return int(hr)*60 + int(mn)

def licz():
    H, W, R = next_int(), next_int(), next_int()
    kam = [ (next_int()-1, next_int()-1) for x in range(R) ]

    tab = [ [0 for x in range(H)] for x in range(W)]

    if (0,0) in tab:
        return "00"

    tab[0][0] = 1;
    for x in range(W):
        for y in range(H):
            if tab[x][y]:
                for nx, ny in ((x+1,y+2),(x+2,y+1)):

                    if nx >= W or ny >= H:
                        continue

                    if (ny,nx) in kam:
                        continue
                    tab[nx][ny] += tab[x][y]
                    tab[nx][ny] %= 10007

    return str(tab[W-1][H-1])

def run():
    tests = next_int()

    for i in range(tests):

        res = licz()
        print 'Case #%d: %s' % ( i+1, res)
                    

run()
