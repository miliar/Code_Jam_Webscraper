#!/usr/bin/python
import sys

SumCache = list()

def calculateTimeToX(C, F, X, n):
    if n >= 1:
        SumCache.append(C / (2 + (n - 1) * F))
    return sum(SumCache) + (X / (2 + n * F))

def main():
    CaseNum = int(sys.stdin.readline())
    for i in range(CaseNum):
        C, F, X = (float(n) for n in sys.stdin.readline().split())
        CurrentMin = sys.maxint
        CurrentN = 0
        del SumCache[:]
        while 1:
            Min = calculateTimeToX(C, F, X, CurrentN)
            if (CurrentMin > Min):
                CurrentMin = Min
                CurrentN += 1
            else:
                print "Case #" + str(i + 1) + ":", CurrentMin
                break

if __name__ == '__main__':
    main()
