#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import os
import time
import itertools
import collections

xs = range(4)
ys = range(4)

def solv(s, c):
    if any([all([s[i][j]==c or s[i][j]=='T' for j in ys]) for i in xs]):
        return True

    if any([all([s[i][j]==c or s[i][j]=='T' for i in xs]) for j in ys]):
        return True

    if all([s[i][i] == c or s[i][i] == 'T' for i in xs]):
        return True

    if all([s[i][3-i] == c or s[i][3-i] == 'T' for i in xs]):
        return True

def main():
    tt = int(raw_input())
    #print "t=",tt
    s = ['' for i in range(4)]
    for t in xrange(tt):
        s[0] = raw_input()
        s[1] = raw_input()
        s[2] = raw_input()
        s[3] = raw_input()
        ss = ''.join(s)
        if t!=tt-1:
            raw_input()
        #print s
        #print ss

        if solv(s, 'X'):
            print "Case #%d: X won" % (t+1)

        elif solv(s, 'O'):
            print "Case #%d: O won" % (t+1)

        elif '.' in ss:
            print "Case #%d: Game has not completed" % (t+1)
        else:
            print "Case #%d: Draw" % (t+1)

if __name__ == '__main__':
    main()
