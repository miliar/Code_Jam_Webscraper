#!/usr/bin/python

import fractions, sys

def gcd_arr(arr):
    return reduce(fractions.gcd, arr)

def consecutive_diff(arr):
    return [(arr[i]-arr[i-1]) for i in range(1, len(arr))]

def calc(arr):
    gcd = gcd_arr(consecutive_diff(sorted(arr)))
    m = min(arr)
    if gcd == 1 or m%gcd == 0:
        return gcd, 0
    else:
        return gcd, ((m/gcd)+1)*gcd - m

# main logic
f = open(sys.argv[1])

cnt = int(f.readline())

for i in range(0, cnt):
    arr = [int(x) for x in f.readline().split()[1:]]
    gcd, res = calc(arr)
    print "Case #" + str(i+1) + ": " + str(res)


