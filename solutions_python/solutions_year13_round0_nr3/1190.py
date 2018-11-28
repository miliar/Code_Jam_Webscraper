#!/usr/bin/env python
#author: Chen Zhao

import os.path
from math import sqrt, ceil, floor

finput = '/Users/chin/dev/codejam/2013/B-large.in'
finput = '/Users/chin/dev/codejam/2013/test.input'
finput = '/Users/chin/dev/codejam/2013/C-small-attempt0.in'


def is_palin(i):
    s = str(i)
    l = len(s)
    for i in range(0, l/2+1):
        if s[i]!=s[l-1-i]:
            return False
    return True

def solve(A, B):
    count = 0
    a = long(ceil(sqrt(A)))
    b = long(floor(sqrt(B)))
    for i in range (a, b+1):
        if is_palin(i):
            if is_palin(i**2):
                count+=1
    return str(count)


def main():
    f = file(finput)
    T = int(f.readline())
    for i in range(1, T+1):
        A, B = map(long, f.readline().split())
        print 'Case #%d: %s'%(i, solve(A, B))
    pass

if __name__=='__main__':
    main()

