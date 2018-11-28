#!/usr/bin/python
# -*- coding:utf-8 -*-

# Here we go

import numpy as np



def check(matrix, N, M):
    for i in range(0,N):
        for j in range(0,M):
            if not ( matrix[i,:].max() == matrix[i,j] or matrix[:,j].max() == matrix[i,j] ):
                return "NO"

    return "YES"


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        input_file = "test_input.txt"
    else:
        input_file = sys.argv[1]

    f = open(input_file, "r")

    T = int(f.readline())

    for i in range(1,T+1):
        print "Case #%d: " % i,

        N, M = map(int, f.readline().split(" "))
        rows = []
        for i in range(0,N):
            rows.append(map(int, f.readline().split(" ")))

        print check(np.matrix(rows), N, M)
