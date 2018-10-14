#!/usr/bin/python

"""Usage:
    X.py < X.in > X.out
"""

import re

################################################################################
# util functions

logging = False

globalCase = 0
def log(string="", case=0):
    global globalCase
    if logging:
        if case > 0:
            globalCase = case
            string = "started case - %s" % string
        print("Case #%d: %s" % (globalCase, string))

################################################################################
# problem functions

def solve(name, n):
    log('trying to solve {} of {}'.format(name,n))
    s = re.sub('[^0]','1',re.sub('[aeiou]','0',name))
    log('s= "{}"'.format(s))

    N = '1'*n
    i = s.find(N)
    count = 0
    x = 0
    while i > -1:
        log('found {} in {}'.format(N,s))
        log('({}+1) * ({}-{}-{}-{}+1)'.format(i,len(name),i,n,x))
        count += (i+1) * (len(name)-i-n-x+1)
        s = s[i+1:]
        x += i+1
        i = s.find(N)
    
    return count
    
################################################################################
# main

if __name__ == '__main__':
    import sys
    r = sys.stdin.readline
    cases = int(r())
    for c in xrange(cases):
        log(case=c+1)
        #string = r().strip()
        #single = int(r())
        #multi = map(int, r().split())
        (name, n) = r().split()
        n = int(n)
        print 'Case #{}: {}'.format(c + 1, solve(name,n))
