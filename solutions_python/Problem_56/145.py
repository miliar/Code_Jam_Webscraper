#!/usr/bin/env python
# -*- coding: utf-8 -*-
def p(str):
    #print str
    pass


def readline():
    import sys
    f = open(sys.argv[1])
    T = int(f.readline()[:-1])
    p(T)
    for t in range(T):
        N, K = f.readline()[:-1].split()
        N = int(N)
        K = int(K)
        p(N)
        p(K)
        piece = []
        for n in range(N):
            pc = f.readline()[:-1]
            piece.append(pc)
            p(pc)
        p2 = rotate(piece)
        p3 = gravity(p2)
        str = judge(p3,K)
        print "Case #%d: %s" % (t+1, str)
    

def rotate(piece):
    len_of_p2 = len(piece)
    p(piece)
    p2 = []
    for y in range(len_of_p2):
        p2y = ['.'] * len_of_p2
        for x in range(len_of_p2):

            pa = piece[len_of_p2-x-1]
            #p(pa)
            p2y[x] = pa[y]

        p2.append(p2y)
        #p(p2[y])
    #p(p2)
    return p2

def gravity(piece):
    l = len(piece)

    p2 = piece#[['.'] * l ] * l
    for x in range(l):
        yl = range(l)
        yl.reverse()
        for y in yl:
            #p("%d,%d" %(x,y)),
            if p2[y][x] == '.':
                loop(p2, x, y)

    for p2y in range(l):
        p(p2[p2y])

    return p2

def loop(p2, x, y):

    yl2 = range(y)
    yl2.reverse()
    for y2 in yl2:
        #p(" %d,%d,%s" %(x,y2, p2[y2][x])),
        if p2[y2][x] != '.':
            p2[y][x] = p2[y2][x]
            p2[y2][x] = '.'
            #p('swap x:%d y1:%d y2:%d' %(x,y,y2))
            return

def judge(p2,K):
    L = len(p2)
    pts_r = pts_b = 0
    for y in range(L):
        for x in range(L):
            pts_r += judgeLine(p2, x, y, K, L,'R')
            pts_r += judgeRaw(p2, x, y, K, L, 'R')
            pts_r += judgeRightDown(p2, x, y, K, L, 'R')
            pts_r += judgeLeftDown(p2, x, y, K, L, 'R')
            
            pts_b += judgeLine(p2, x, y, K, L,'B')
            pts_b += judgeRaw(p2, x, y, K, L, 'B')
            pts_b += judgeRightDown(p2, x, y, K, L, 'B')
            pts_b += judgeLeftDown(p2, x, y, K, L, 'B')
    p("score")
    p(pts_r)
    p(pts_b)

    if pts_r == 0 and pts_b == 0: return "Neither"
    elif pts_r > 0 and pts_b == 0: return "Red"
    elif pts_r ==0 and pts_b >0: return "Blue"
    else: return "Both"

def judgeLine(p2, x, y, K, L, color):

    if p2[y][x] == color and x+K < L+1:
        for x2 in range(x+1,x+K):
            if p2[y][x2] != color: break
        else:
            return 1#p("%s +1 line" % color)
    return 0

def judgeRaw(p2, x, y, K, L, color):
    if p2[y][x] == color and y+K < L+1:
        for k in range(1,K):
            if p2[y+k][x] != color: break
        else:
            return 1#p("%s +1 raw" % color)
    return 0

def judgeRightDown(p2, x, y, K, L, color):

    if p2[y][x] == color and y+K < L+1 and x+K < L+1:
        for k in range(1,K):
            if p2[y+k][x+k] != color: break
        else:
            return 1#p("%s +1 rightdown" % color)
    return 0

def judgeLeftDown(p2, x, y, K, L, color):

    if p2[y][x] == color:
        if y+K < L+1 and x >= K -1:
            for k in range(1,K):
                if p2[y+k][x-k] != color: break
            else:
                return 1#p("%s +1 leftdown" % color)
    return 0

readline()
