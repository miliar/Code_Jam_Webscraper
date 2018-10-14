#!/usr/bin/python

import sys, datetime

SEPARATE_LINE = "=" * 20

def updateVineRange(vines, i, N):
    curVine = vines[i]
    for j in range(i + 1, N):
        nextVine = vines[j]
        if curVine[2] >= nextVine[0] - curVine[0]:
            maxRange = min(nextVine[0] - curVine[0], nextVine[1])
            if maxRange > nextVine[2]:
                nextVine[2] = maxRange
        else:
            return

def solve(N, vines, D):
    vine = vines[0]
    vines[0][2] = vines[0][0]
    for i in range(N):
        curVine = vines[i]
        if curVine[2] == 0:
            return "NO"
        if curVine[2] >= D - curVine[0]:
            return "YES"
        updateVineRange(vines, i, N)
    return "NO"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit();

    inFile = open(sys.argv[1])
    outFile = open(sys.argv[2], "w")

    startTime = datetime.datetime.now()
    print "Start Time = %s" % startTime
    print SEPARATE_LINE

    T = int(inFile.readline())
    for i in range(T):
        N = int(inFile.readline())
        vines = list()
        for j in range(N):
            d, l = map(int, inFile.readline().strip().split())
            # last 0 is initial range
            vines.append([d, l, 0])
        D = int(inFile.readline())
        result = solve(N, vines, D)
        outFile.write("Case #%d: %s\n" % (i + 1, result))
    endTime = datetime.datetime.now()

    print SEPARATE_LINE
    print "End Time = %s" % endTime
    print "Cost Time = %s" % (endTime - startTime)
    inFile.close()
    outFile.close()
