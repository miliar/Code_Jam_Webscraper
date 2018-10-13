#!/usr/bin/python

import sys
import math

def test(val):
    s = str(val)
    l = len(s)
    for i in xrange(0,l/2):
        if s[i] != s[l-i-1]:
            return False
    return True

def calc(a,b):
    ca,cb = 0,0
    v = 0
    while True:
        v = v + 1
        strv = str(v)
        rstrv = str(v)
        new_1 = int(strv + rstrv)
        new_2 = int(strv + rstrv[1:])
        new_1 = new_1 * new_1
        new_2 = new_2 * new_2
        r1 = test(new_1)
        r2 = test(new_2)
        if r1:
            #print new_1
            if new_1 <= a: ca+=1
            if new_1 <= b: cb+=1
        if r2:
            #print new_2
            if new_2 <= a: ca+=1
            if new_2 <= b: cb+=1
        if new_2 > b:
            break
    return cb-ca

if __name__=="__main__":
    fp = sys.stdin
    data = fp.readlines()
    N = int(data[0])
    data = data[1:]
    for i,line in enumerate(data):
        A,B = [int(x) for x in line.strip().split(' ')]
        
        res = calc(A-1,B)

        print "Case #%d:" %(i+1),
        print res

