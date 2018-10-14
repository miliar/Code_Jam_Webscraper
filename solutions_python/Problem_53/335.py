#!/usr/bin/env python

import sys,math

def main(argv):
    n = int(sys.stdin.readline())
    for i in range(1,n+1):
        line = sys.stdin.readline()
        (N,K) = line.split(" ")
        N = int(N)
        K = int(K)
        temp = int(math.pow(2,N))
        res = "OFF"
        if (K == 0):
            res = "OFF"
        elif ((K % temp) == (temp-1)):
            res = "ON"

        print("Case #%d: %s" % (i, res))
    

main(sys.argv)
