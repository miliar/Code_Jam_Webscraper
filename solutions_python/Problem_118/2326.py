#!/usr/bin/env python
# encoding: utf-8

from math import sqrt,ceil,floor

def is_palindromes(n):
    s = str(n)
    l = len(s)
    c = 0
    for j in range(l/2):
        if s[j] != s[l-j-1]:
            break
        else:
            c += 1
    if c != l/2:
        return False
    else:
        return True

def palindromes(a,b):
    if b < 10:
        return range(a,b+1)
    else:
        tmp = []
        if a < 10:
            tmp += range(a,10)
            a = 10
        for i in xrange(a,b+1):
            s = str(i)
            l = len(s)
            c = 0
            for j in xrange(l/2):
                if s[j] != s[l-j-1]:
                    break
                else:
                    c += 1
            if c != l/2:
                continue
            else:
                tmp.append(i)
        return tmp

def main():
    try:
        n = raw_input()
        n = int(n)
    except:
        return
    else:
        a = [raw_input() for i in range(n)]
        for idx,r in enumerate(a):
            count = 0
            a,b=r.split()
            a = int(ceil(sqrt( int(a))))
            b = int(floor(sqrt( int(b))))
            pa = palindromes(a,b)
            for p in pa:
                p2 = p*p
                if is_palindromes(p2):
                    count += 1
            print "Case #{0}:".format(idx+1),count

main()
