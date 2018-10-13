#! /usr/bin/python3.1

import sys
from sys import stdin
import os
import copy

def solve(r, k, n, g):
    cycles = {}
    front = 0
    r1 = 0
    result = 0
    riding = []
    queue = copy.copy(g)
    while r1 < r:
        r1 += 1
        try:
            front1, count = cycles[front]
        except KeyError:
            count = 0
            front1 = front
            while queue and (count + queue[0]) <= k:
                front1 = (front1 + 1) % n
                group = queue.pop(0)
                count += group
                riding.append(group)
            queue.extend(riding)
            del riding[:]
            cycles[front] = (front1, count)
        result += count
        front = front1
    return result

def main(argv=sys.argv):
    ncases = int(stdin.readline().strip())
    for i in range(1, ncases + 1):
        r, k, n = [int(x) for x in stdin.readline().split()]
        g = [int(x) for x in stdin.readline().split()]
        print("Case #{0}: {1}".format(i, solve(r, k, n, g)))
    return 0

if __name__ == '__main__':
    sys.exit(main())
