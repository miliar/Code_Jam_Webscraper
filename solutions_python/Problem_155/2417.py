from __future__ import print_function
import sys

T = int(sys.stdin.next().strip())

for i in range(T):
    tmp = sys.stdin.next().strip().split(" ")
    smax = int(tmp[0])
    audiences = map(int, list(tmp[1]))

    #print(smax)
    #print(audiences)

    shyness = []
    for j, k in enumerate(audiences):
        for l in range(k):
            shyness.append(j)

    offset = 0
    #print(shyness)
    for m, n in enumerate(shyness):
        if m+offset < n:
            offset = n-m
    print("Case #%d: %d" % (i+1, offset))
