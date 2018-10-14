#!/usr/bin/python
import sys

def solve(N, K):
    snappers = [False] * N
    for t in range(0, K):
        r2 = range(0, N)
        r2.reverse()
        for i in r2:
            power = True
            for j in range(0, i):
                if not snappers[j]:
                    power = False
                    break
            if power:
                snappers[i] = not snappers[i]
    power = True
    for i in range(0, N):
        if not snappers[i]:
            power = False
            break
    if power:
        return "ON"
    else:
        return "OFF"

f=open(sys.argv[1])
T = int(f.readline())

lines = f.readlines()
c = 0
for l in lines:
    r = l.split(' ')
    N = int(r[0])
    K = int(r[1])
    c += 1
    print "Case #%d: %s" % (c, solve(N, K))
