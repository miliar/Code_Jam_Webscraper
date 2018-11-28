#!/usr/bin/env python

import sys

def check(a, b, n):
    N = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000];
    for i in range(1, n):
        if (a % N[i] * N[n-i] + a / N[i] == b):
            return 1;
    return 0;

def getrecs(c, n):
    N = [0, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000];
    recs = set();
    for i in range(1, n):
        recs.add(c % N[i] * N[n-i] + c / N[i]);
    return recs;

with open(sys.argv[1]) as infile:
    cases = [[int(item) for item in line.split()] for line in infile][1:];
    cid = 0;
    for case in cases:
        cid += 1;
        A = case[0];
        B = case[1];
        C = 0;
        N = len(str(A))
        #for i in range(A, B):
        #    for j in range(i+1, B+1):
        #        C += check(i, j, N);
        for i in range(A, B):
            for rec in getrecs(i, N):
                if rec > i and rec <= B:
                    C += 1;
        print "Case #%d: %d" % (cid, C);
