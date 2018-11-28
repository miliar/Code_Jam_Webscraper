# -*- coding: utf-8 -*-

import os,sys
import math

def jamout(linestring):
    if istest:
        print linestring
    else:
        fo.write(linestring + '\n')
        print linestring

def chk(ch):
    tx = ['X' if 'T'==c else c for c in ch]
    if tx[0]==tx[1]==tx[2]==tx[3]=='X': return 'X won'
    ty = ['O' if 'T'==c else c for c in ch]
    if ty[0]==ty[1]==ty[2]==ty[3]=='O': return 'O won'
    
    return None
    
def solve(bd):
    for y in range(0,4):
        res = chk(bd[y])
        if res: return res
    for x in range(0,4):
        b = [bd[0][x],bd[1][x],bd[2][x],bd[3][x]]
        res = chk(b)
        if res: return res
    b = [bd[0][0],bd[1][1],bd[2][2],bd[3][3]]
    res = chk(b)
    if res: return res
    b = [bd[0][3],bd[1][2],bd[2][1],bd[3][0]]
    res = chk(b)
    if res: return res
    
    for x in range(0,4):
        for y in range(0,4):
            if bd[y][x]=='.':
                return 'Game has not completed'
    return 'Draw'
        
ex = """6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O
"""

if len(sys.argv)==3:
    infile  = sys.argv[1]
    outfile = sys.argv[2]
    fo = open(outfile,'w')
    s = open(infile, 'r').read()
    lines = s.split('\n')
    istest = False
else:
    lines = ex.split('\n')
    istest = True

T = int(lines[0])
cursor = 1
board = []
for i in range(T):
    b0 = lines[cursor]
    b1 = lines[cursor+1]
    b2 = lines[cursor+2]
    b3 = lines[cursor+3]
    cursor += 5
    board = [b0,b1,b2,b3]
    result = solve(board)
    jamout("Case #%d: %s" % (i+1, result))

if istest==False:
    fo.close()