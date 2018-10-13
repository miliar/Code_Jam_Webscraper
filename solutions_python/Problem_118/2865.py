#!/usr/bin/env python
# -*- utf-8 -*-

from math import *

def palindrome(num):
    return str(num) == str(num)[::-1]

def solver(nStart, nEnd):
    myStart = int(ceil(sqrt(nStart)))
    myEnd = int(floor(sqrt(nEnd)))
    
    cnt = 0
    # print myStart, myEnd

    for i in range(myStart, myEnd+1):
        if palindrome(i) and palindrome(i*i):
            cnt += 1

    return cnt

def main():
    f = open("C-small-attempt0.in", "r")
    num = int(f.readline())
    for i in range(0,num):
        [s,e] = f.readline().split()
        print "Case #%d: %d" % (i+1, solver(int(s), int(e)))
    
if __name__ == "__main__":
    main()
