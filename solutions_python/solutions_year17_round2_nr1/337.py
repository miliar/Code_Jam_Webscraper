#!/usr/bin/env python

def Solve(d, arr):
    minTime = -1.0
    for i in arr:
        if i[0] >= d:
            continue
        t = float(d-i[0])/i[1]
        if minTime < 0 or minTime < t:
            minTime = t
    return d / minTime

def main():
    t = int(raw_input())
    for i in xrange(t):
        p = raw_input().rstrip().split(" ")
        d = int(p[0])
        n = int(p[1])
        arr = []
        for j in xrange(n):
            p = raw_input().rstrip().split(" ")
            arr.append((int(p[0]), int(p[1])))
        print "Case #" + str(i+1) +": " + str(Solve(d, arr))

if __name__ == "__main__":
    main()
