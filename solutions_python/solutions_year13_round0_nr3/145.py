#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys


ret = 0

l = [0, 1, 4, 9]

def ck(i):
    sqr = str(i * i)
    if sqr == sqr[::-1]:
        if int(sqr) not in l:
            l.append(int(sqr))
        #print sqr

for i in range(0, 25):
    ck(int("2" + ("0"*i) +       ("0"*i) + "2"))
    ck(int("2" + ("0"*i) + "0" + ("0"*i) + "2"))
    ck(int("2" + ("0"*i) + "1" + ("0"*i) + "2"))
    ck(int("2" + ("0"*i) + "2" + ("0"*i) + "2"))

i = 0
while i <= 2**25:
    p = bin(i)[2:]

    ck(int(p + p[::-1]))
    #ck(int("2" + p[1:] + "0"+p[:0:-1] + "2"))
    #ck(int("2" + p[1:] + "1"+p[:0:-1] + "2"))
    #ck(int("2" + p[1:] + "2"+p[:0:-1] + "2"))
    ck(int(p + "0" + p[::-1]))
    ck(int(p + "1" + p[::-1]))
    ck(int(p + "2" + p[::-1]))

    i += 1


l.sort()
sys.stderr.write('fertig\n')

sys.stdin.readline()
sys.stderr.write('weiter\n')

f = open('C-large-2.in', 'r')
from sys import stdin
C = int(f.readline())
for c in range(1,C+1):
    res = 0
    x, y = map(int, f.readline().split())
    for el in l:
        if el > y:
            break
        if el < x:
            continue
        res += 1
    print "Case #%d:" % c , res
f.close()
