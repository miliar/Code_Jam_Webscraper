#!/usr/bin/env python
import sys


def flip(row, position, k):
    a = list(row)
    for i in range(position, position + k):
        if a[i] == '-':
            a[i] = '+'
        else:
            a[i] = '-'
    return "".join(a)


def bfs(row, k):

    queue = [(row, 0)]
    visited = set()
    while len(queue) != 0:
        # print queue
        visting, flips = queue.pop(0)
        # print visting, flips
        if visting == ('+' * len(row)):
            return str(flips)
        if visting not in visited:
            visited.add(visting)
            for i in range(len(visting)):
                if visting[i] == "+":
                    continue
                else:
                    queue.append(
                        (flip(visting, min(i, len(row) - k), k), flips + 1))
    return "IMPOSSIBLE"

num_test = int(raw_input())

for i in range(num_test):
    row, k = raw_input().split(" ")

    print "Case #" + str(i + 1) + ": " + bfs(row, int(k))
