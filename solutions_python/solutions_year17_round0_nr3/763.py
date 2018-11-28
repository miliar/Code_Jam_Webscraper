#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def solve(N, K):
    left = long((N - 1) / 2)
    right = N - 1 - left
    if K == 1:
        return "{max} {min}".format(max=right, min=left)
    elif K > 1:
        left_k = long((K - 1) / 2)
        right_k = K - 1 - left_k
        if left_k == right_k:
            return solve(left, left_k)
        else:
            return solve(right, right_k)

if __name__ == "__main__":
    T = input()
    for t in xrange(1, T+1):
        N, K = map(int ,sys.stdin.readline().split())
        print "Case #{no}: {result}".format(no=t, result=solve(N, K))
