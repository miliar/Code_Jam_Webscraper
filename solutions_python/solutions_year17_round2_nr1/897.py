#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

import sys

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        d, n = map(int, sys.stdin.readline().split())
        res = float("inf")
        for j in range(n):
            ki, si =  map(int, sys.stdin.readline().split())
            res = min(res, si/(d-ki))
        print("CASE #%s: %s" % (i+1, d*res))

main()
