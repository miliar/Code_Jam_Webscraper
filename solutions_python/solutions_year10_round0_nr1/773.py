#!/usr/bin/env python

import sys

if __name__ == "__main__":
    T = eval(sys.stdin.readline())
    for i in range(1,T+1):
        N,K = map(eval,sys.stdin.readline().split())
        K = K % (2**N)
        print "Case #" + str(i) + ': ' + ("ON" if K == 2**N - 1 else "OFF")
