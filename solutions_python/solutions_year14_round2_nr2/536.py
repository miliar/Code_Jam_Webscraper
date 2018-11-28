#!/usr/bin/env python

with open("B-small-attempt0.in", "r") as fin:
    N = int(fin.readline())
    fout = open("B-small-attempt0.out", "w")

    # read the input
    for i in xrange(N):
        a = map(int, fin.readline().split())
        A = a[0]
        B = a[1]
        K = a[2]
        sum = 0
        for p in xrange(A):
            for q in xrange(B):
                if p & q < K:
                    sum += 1
        fout.write("Case #"+str(i+1)+": "+str(sum)+"\n")