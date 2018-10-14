#!/usr/bin/python

import sys
from collections import Counter

def split_space(n):
    return n/2, (n-1)/2

def last_split(n, people):
    spaces = Counter()
    spaces[n] = 1

    while True:
        max_k = max(spaces.keys())
        max_v = spaces[max_k]
        del spaces[max_k]

        if people <= max_v:
            return split_space(max_k)

        a, b = split_space(max_k)
        spaces[a] += max_v
        spaces[b] += max_v

        people -= max_v

def main():
    index = 0
    sys.setrecursionlimit(3000)
    sys.stdin.readline()
    for line in map(str.strip, sys.stdin.readlines()):
        # print line
        stalls, people = map(int, line.split())
        index += 1

        result = last_split(stalls, people)
        print "Case #{}: {} {}".format(index, result[0], result[1])

main()
