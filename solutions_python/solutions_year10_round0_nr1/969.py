#! /usr/bin/python

# usage :: ./snapper.py <file>

from sys import argv


def light_check(N,K):
    # with x or y snaps the light will turn on
    x= 2**N - 1
    if K == x: return 'ON'
    elif K > x:
        y= x
        r= 1
        while y <= K:
            y= x + (x+1)*r
            if K == y: return 'ON'
            r+= 1
        else: return 'OFF'
    else: return 'OFF'


with open(argv[1]) as f:
    no_cases= f.readline()
    for i in xrange(int(no_cases)):
        case= f.readline()
        N,K= case.split()
        result= 'Case #%d: ' % (i+1)
        result+= light_check(int(N),int(K))
        print result
