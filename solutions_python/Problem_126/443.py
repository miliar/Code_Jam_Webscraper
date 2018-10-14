#!/usr/bin/python
#
# S. Singh
# May 12, 2013

import numpy as np
import re
import sys


def computeSubsets(s, n):
    subs = []
    
    for m in xrange(len(s) - n+1):
        sub = s[m : m + n]
        if 'a' in sub or 'e' in sub or 'i' in sub or 'o' in sub or 'u' in sub:
            continue
        
        if len(sub) >= n:
            for j in xrange(0, m + 1):
                #words.append(s[j : i + len(sub)])
                #subs.append((j, i + len(sub)))
                
                for k in xrange(m + n, len(s) + 1):
                    subs.append((j, k))
    
    return len(set(subs))


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    
    for i in xrange(1, T + 1):
        s, n = sys.stdin.readline().lower().split()
        n = int(n)
        
        print 'Case #%d:' % i, computeSubsets(s, n)
    
    

