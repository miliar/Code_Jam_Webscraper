#!/opt/local/bin/python

import sys
import re

def doit(N, K):
    bK = bin(int(K))[2:]
    N = int(N)
    for d in reversed(bK[1:]):
        N = (N - int(d)) // 2

    return [str(N // 2), str((N-1) // 2)]

T = int(sys.stdin.readline())
for casenum in range(T):
    data = sys.stdin.readline().split()

    n = doit(*data)




    print("Case #" + str(casenum + 1) + ": " + " ".join(n) ) # + "\t[" + data[:-1] + "]")
