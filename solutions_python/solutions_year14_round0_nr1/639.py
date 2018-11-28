#!/bin/env python

def solve(n):
    a = int(raw_input())
    ar = None
    for j in range(4):
        tmp = raw_input()
        if j + 1 == a:
            ar = {int(i) for i in tmp.split(' ')}
    b = int(raw_input())
    br = None
    for j in range(4):
        tmp = raw_input()
        if j + 1 == b:
            br = {int(i) for i in tmp.split(' ')}
    r = []
    for i in ar:
        if i in br:
            r.append(i)
    if len(r) == 0:
        print("Case #%d: Volunteer cheated!" % n)
    elif len(r) == 1:
        print("Case #%d: %d" % (n, r[0]))
    else:
        print("Case #%d: Bad magician!" % n)

if __name__ == '__main__':
    N = int(raw_input())
    for i in range(N):
        solve(i + 1)
