#!/usr/bin/python

import sys, re
from scipy import *



def main():
    NN = int(sys.stdin.next())
    for nn in xrange(1,NN+1):
        print 'Case #%d: %d' % (nn, calculate())


def calculate():
    n = int(sys.stdin.next())
    t = []
    for i in range(n):
        t.append(sys.stdin.next().rfind('1'))

    ret = 0
    for i in range(len(t)):
#        print ret, t
        for j in range(i,len(t)):
            if t[j]<=i and feasible(t[i:j]+t[j+1:], i+1):
                ret += j-i
                t = t[:i] + [t[j]] + t[i:j] + t[j+1:]
                break;
    return ret


def feasible(a,n):
    a = array(sorted(a))
    b = n+arange(len(a))
    return all(a<=b)
    
if __name__ == "__main__":
    main()
