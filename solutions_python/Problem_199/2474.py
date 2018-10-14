#!/usr/bin/python

from sys import stdin


def parse_input(line):
    panc = [x == '+' for x in line.split(" ")[0]]
    k = int(line.split(" ")[1])
    return panc, k

def flip(pancakes, i, k):
    for j in range(0, k):
        pancakes[i+j] = not pancakes[i+j]

def count_flips(pancakes, k):
    flips = 0
    for i in range(0, len(pancakes)-k+1):
        if not pancakes[i]:
            flip(pancakes, i, k)
            flips+=1
    res = reduce(lambda a,b : a &b, pancakes)
    if res:
        return str(flips)
    else:
        return "IMPOSSIBLE"


TESTCASES = int(stdin.readline())
for i in range(1,TESTCASES+1):
    p, k = parse_input(stdin.readline())
    res = count_flips(p,k)
    print "Case #%d: %s" % (i, res)
