import sys
import re #regular expressions
import math
import random
import array #homogenours lists
import collections
import bisect #operations on sorted lists (e.g. bisect.insort)
import heapq

def solve(N, ABs):
    if (N == 1):
        return 0
    elif (N == 2):
        a0=ABs[0][0]
        b0=ABs[0][1]
        a1=ABs[1][0]
        b1=ABs[1][1]
        if ((a0 > a1) and (b1 > b0)):
            return 1

        if ((a1 > a0) and (b0 > b1)):
            return 1
    #solution for N > 2
    result = 0
    ABs.sort() #we sort by Ai
    for i in range(0,N):
        Ai=ABs[i][0]
        Bi=ABs[i][1]
        for j in range(0,i):
            if (ABs[j][1] > Bi):
                result = result + 1
    return result


if __name__ == "__main__":
    cases = int(sys.stdin.readline().strip())
    #for all cases
    for case in range(1,cases+1):
        print "Case #{0}:".format(case),

        #read and format input here
        N = int(sys.stdin.readline().strip())
        ABs = []
        for i in range(0,N):
            ABs.append(map(int,sys.stdin.readline().strip().split()))

        #print solution
        print solve(N, ABs);