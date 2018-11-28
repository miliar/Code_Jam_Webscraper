#!/usr/bin/env python

import re

def recur(tree, b):
    if isinstance(tree, float):
        return tree
    else:
        if tree[1] in b:
            return tree[0] * recur(tree[2], b)
        else:
            return tree[0] * recur(tree[3], b)

def solve(c):
    print "Case #%d:" % c

    L = int(raw_input())
    t = '\n'.join(raw_input() for _ in range(L))
    p = re.compile(r"([a-zA-Z]+)")
    tree = eval(','.join(p.sub("\"\\1\"", t).split()).replace('(,', '(').replace(',)', ')'))
    
    A = int(raw_input())
    for _ in range(A):
        a = raw_input().split()
        b = a[2:]
        a = a[0]

        print '%.7f' % recur(tree, b)


def main():
    N = int(raw_input())
    for i in range(N):
        solve(i+1)


if __name__ == "__main__":
    main()
