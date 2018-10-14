#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinput as f
import math

def is_palindrome(n):
    s = str(n)
    if len(s) == 1:
        return True
    i = 0;
    j = len(s) - 1
    while(j>i):
        if(s[i]==s[j]):
            i+=1
            j-=1
        else:
            return False
    else:
        return True

def fair_squares(limit=10**3):
    count = 0
    p = {p for p in palindromes(limit)}
    for i,s in enumerate(squares(limit)):
        if (i+1) in p and s in p :
            yield s

def squares(limit=10**3):
    SQ = {}
    i = 1
    while i < math.sqrt(limit):
        yield i*i
        i+=1

def palindromes(limit=10**3):
    f = 1 
    while f < limit:
        if is_palindrome(f):
           yield f
        f += 1       

def rank(key,lo,hi,fs):
    if hi < lo:
       return lo
    mid = lo + (hi - lo) / 2
    if key < fs[mid]:
       return rank(key, lo, mid-1,fs)
    elif key > fs[mid]:
        return rank(key, mid+1, hi,fs)
    else:
       return mid

def main():
    """docstring for main"""
    cases = []
    for line in f.input():
        if f.lineno() == 1:
            T = line.rstrip('\n')
            continue
        cases.append(line.split())
    fs = [p for p in fair_squares()]
    for i, case in enumerate(cases):
        l,h = case[0],case[1]
        lo,hi = int(l), int(h)
        x = rank(int(lo), 0, len(fs)-1,fs)
        y = rank(int(hi) , 0, len(fs)-1,fs)
        if hi < lo:
           num = 0
        elif hi in fs:
            num = y - x + 1
        else:
            num = y-x
#        print "Greater than %d: %d" % (int(lo), x)
#        print "Less than %d: %d" % (int(hi), y)
        print "Case #%d: %d" % (i + 1, num )

if __name__ == '__main__':
    main()
