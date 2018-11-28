#!/usr/bin/python

import sys;
import os.path; 

def readi():
    return int(sys.stdin.readline().strip());

def readia():
    return [int(x) for x in sys.stdin.readline().strip().split()];

def readfa():
    return [float(x) for x in sys.stdin.readline().strip().split()];

def reads():
    return sys.stdin.readline().strip();

def checkSmall(A, B, K):
    res = 0;
    for a in xrange(A):
        for b in xrange(B):
            if a & b < K:
                res += 1;
    return res;

def main():
    nt = readi();
    for t in range(1, nt+1):
        (A, B, K) = readia();

        res = checkSmall(A, B, K);

        print "Case #%d: %d" % (t, res);
    

main();
