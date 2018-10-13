#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import copy

def cmp1(x, y):
    return x[0]-y[0]

def cmp2(x, y):
    return x[1]-y[1]

def main():
    n = int(raw_input())
    for i in range(n):
        t = int(raw_input())
        nab = raw_input().split(' ')
        na = int(nab[0])
        nb = int(nab[1])
        atbl = []
        for j in range(na):
            line = raw_input().split(' ')
            dt = line[0].split(':')
            at = line[1].split(':')
            atbl.append([int(dt[0])*60 + int(dt[1]), int(at[0])*60+int(at[1])+t])
            
        btbl = []
        for j in range(nb):
            line = raw_input().split(' ')
            dt = line[0].split(':')
            at = line[1].split(':')
            btbl.append([int(dt[0])*60 + int(dt[1]), int(at[0])*60+int(at[1])+t])
            

        atbl = sorted(atbl, cmp1)
        btbl = sorted(btbl, cmp1)
        
        atbl2 = sorted(atbl, cmp2)
        btbl2 = sorted(btbl, cmp2)
        
        atbl_clone = copy(atbl)
        btbl_clone = copy(btbl)
        for b in btbl2:
            for a in atbl_clone:
                if b[1] <= a[0]:
                    atbl_clone.remove(a)
                    break
        
        for a in atbl2:
            for b in btbl_clone:
                if a[1] <= b[0]:
                    btbl_clone.remove(b)
                    break
        
        print "Case #%d: %d %d" % (i+1, len(atbl_clone), len(btbl_clone))

if __name__ == '__main__':
    main()