import os, sys

infile = sys.stdin

def solve(cap, arr):
    arr = sorted(arr)
    N = len(arr)
    l = 0
    r = N - 1
    merge = 0
    while l < r:
        if arr[l] + arr[r] <= cap:
            l += 1
            r -= 1
            merge += 1
        else:
            r -= 1
    return N - merge

T = int(infile.readline())

for i in xrange(1, T+1):
    N, cap = [int(v) for v in infile.readline().split()]
    arr = [int(v) for v in infile.readline().split()]
    # print N, cap
    # print arr
    print "Case #%d: %d" % (i, solve(cap, arr))
