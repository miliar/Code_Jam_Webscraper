#!/usr/bin/env python

from sys import stdin

def solve():
    N, L, H = map(int, stdin.readline().split())
    F = map(int, stdin.readline().split())
    for i in range(L, H+1):
        harmony = True
        for j in F:
            if i % j != 0 and j % i != 0:
                harmony = False
                break
        if harmony:
            return i
    return 'NO'

def main():
    T = int(stdin.readline())
    for i in range(T):
        print "Case #{0}: {1}".format(i+1, solve())

main()
