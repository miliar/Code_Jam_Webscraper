#!/usr/bin/env python

from sys import stdin

def solve(candies):
    s = reduce(lambda x,y: x^y, candies, 0)
    if s!=0:
        return 'NO'
    return sum(candies)-min(candies)

def main():
    T = int(stdin.readline())
    for i in range(T):
        stdin.readline()
        candies = map(int, stdin.readline().split())
        print "Case #{0}: {1}".format(i+1, solve(candies))

main()
