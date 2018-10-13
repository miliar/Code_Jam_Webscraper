import sys
import numpy as np
import math

def getans(N, K, U, plist):
    plist.sort()
    if N == 1:
        return plist[0] + U
    while U > 0:
        cur = 0
        while cur < N-1 and plist[cur+1] == plist[cur]:
            cur += 1
        if cur == N-1:
            diff = 1 - plist[cur]
        else:
            diff = plist[cur+1] - plist[cur]
        tofill = diff * (cur+1)
        if U >= tofill and cur < N-1:
            U -= tofill
            for i in range(cur+1):
                plist[i] = plist[cur+1]
        else:
            for i in range(cur+1):
                plist[i] += U / (cur+1)
            U = 0
    return np.prod(plist)

#Read data
if len(sys.argv) < 2:
    print("Missing input file name")
    quit()
with open(sys.argv[1], "r") as f:
    T = int(f.readline())
    for x in range(T):
        N, K = [int(z) for z in f.readline().split()]
        U = float(f.readline())
        plist = [float(z) for z in f.readline().split()]
        print("Case #%d: %.8f" % (x + 1, getans(N, K, U, plist)))
