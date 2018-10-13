#!/usr/bin/env python

import sys

def Do(n, arr, cur, last, first):
    if n == 0:
        if last == first:
            return -1
        return 1
    max = 0
    pos = -1
    f = False
    for i in xrange(6):
        if last == 0 and (i == 0 or i == 1 or i == 5):
            continue
        if last == 1 and (i != 4):
            continue
        if last == 2 and (i == 2 or i == 1 or i == 3):
            continue
        if last == 3 and (i != 0):
            continue
        if last == 4 and (i == 4 or i == 3 or i == 5):
            continue
        if last == 5 and i != 2:
            continue
        if max < arr[i] or (max == arr[i] and arr[i] != 0 and f == False and not (i == 0 or i == 3 or i == 5)):
            max = arr[i]
            if first == i:
                f = True
            pos = i
    if pos != -1:
        ch = ''
        if pos == 0:
            ch = 'R'
        if pos == 1:
            ch = 'O'
        if pos == 2:
            ch = 'Y'
        if pos == 3:
            ch = 'G'
        if pos == 4:
            ch = 'B'
        if pos == 5:
            ch = 'V'
        cur.append(ch)
        arr[pos] -= 1
        if first == -1:
            first = pos
        return Do(n-1, arr, cur, pos, first)
    return -1



def Solve(n, arr):
    res = []
    if Do(n, arr, res, -1, -1) == 1:
        return "".join(res)
    return "IMPOSSIBLE"


def main():
    sys.setrecursionlimit(1500)
    t = int(raw_input())
    for i in xrange(t):
        p = raw_input().rstrip().split(" ")
        print "Case #" + str(i+1) + ": " + Solve(int(p[0]), [int(r) for r in p[1:]])

if __name__ == "__main__":
    main()
