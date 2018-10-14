import os
import sys
from math import *

f = open('input.txt', 'r')

def read():
    k = f.readline()
    while k == '\n':
        k = f.readline()
    return k.replace("\n", "")

t = read()

def win(s, l):
    return s.replace("T", l) == l * 4

for zt in range(int(t)):
    r = [read(), read(), read(), read()]
    c = []
    for i in range(4):
        s = ''
        for j in range(4):
            s += r[j][i]
        c.append(s)
    
    fin = False

    for a in ["X", "O"]:
        for i in range(4):
            if not fin and (win(r[i], a) or win(c[i], a)):
                fin = True
                print 'Case #%d: %s won' % (zt+1, a)

    d1 = r[0][0] + r[1][1] + r[2][2] + r[3][3]
    d2 = r[3][0] + r[2][1] + r[1][2] + r[0][3]

    if not fin and (win(d1, "X") or win(d2, "X")):
        fin = True
        print 'Case #%d: %s won' % (zt+1, "X")

    if not fin and (win(d1, "O") or win(d2, "O")):
        fin = True
        print 'Case #%d: %s won' % (zt+1, "O")

    if not fin and '.' not in ''.join(r):
        fin = True
        print 'Case #%d: Draw' % (zt+1)

    if not fin:
        print 'Case #%d: Game has not completed' % (zt+1)
