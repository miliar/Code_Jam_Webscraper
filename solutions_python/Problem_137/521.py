#!/usr/bin/python3

import sys

pattern = {4:[["c", "."], [".", "."]], 6:[["c", ".", "."], [".", ".", "."]],
           8:[["c", ".", "."], [".", ".", "."], [".", "."]],
           9:[["c", ".", "."], [".", ".", "."], [".", ".", "."]],
           10:[["c", ".", ".", "."], [".", ".", ".", "."], [".", "."]],
           11:[["c", ".", ".", "."], [".", ".", ".", "."], [".", ".", "."]],
           12:[["c", ".", ".", "."], [".", ".", ".", "."], [".", ".", ".", "."]],
           13:[["c", ".", ".", "."], [".", ".", ".", "."], [".", ".", "."], [".", "."]],
           14:[["c", ".", ".", "."], [".", ".", ".", "."], [".", ".", "."], [".", ".", "."]],
           15:[["c", ".", ".", "."], [".", ".", ".", "."], [".", ".", ".", "."], [".", ".", "."]],
           16:[["c", ".", ".", "."], [".", ".", ".", "."], [".", ".", ".", "."], [".", ".", ".", "."]],
           17:[["c", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", "."], [".", ".", "."]],
           18:[["c", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", "."]],
           19:[["c", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", "."]],
           20:[["c", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."]],
           21:[["c", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", "."], [".", "."]],
           22:[["c", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", "."]],
           23:[["c", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", "."]],
           24:[["c", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", "."]],
           25:[["c", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."]]}

def from_pattern(res, empty, b):
    for j in range(len(pattern[empty])):
        for k in range(len(pattern[empty][j])):
            res[j].append(pattern[empty][j][k])
        for k in range(len(pattern[empty][j]), b):
            res[j].append("*")
    return len(pattern[empty])

def star(res, row, a, b):
    for j in range(row, a):
        for k in range(b):
            res[j].append("*")

def rev(res):
    ret = []
    for j in range(len(res[0])):
        ret.append([])
        for k in range(len(res)):
            ret[j].append(res[k][j])
    return ret

t = int(sys.stdin.readline())
for i in range(t):
    r, c, m = [int(x) for x in sys.stdin.readline().split()]
    a, b = min(r, c), max(r, c)
    n = a*b - m
    res = [[] for i in range(a)]
    ok = True
    if m == 0:
        for j in range(a):
            for k in range(b):
                res[j].append(".")
        res[0][0] = "c"
    elif a == 3 and b == 5 and (m == 1 or m == 2):
        for j in range(a):
            for k in range(b):
                res[j].append(".")
        res[0][0] = "c"
        for j in range(b-m, b): res[-1][j] = "*"
    elif n == 1:
        res[0].append("c")
        for j in range(b-1): res[0].append("*")
        star(res, 1, a, b)
    elif a == 1:
        res[0].append("c")
        for j in range(a*b-m-1): res[0].append(".")
        for j in range(m): res[0].append("*")
    elif a == 2:
        if n % 2 == 1 or n == 2:
            ok = False
        else:
            for j in range(n//2):
                res[0].append(".")
                res[1].append(".")
            for j in range(n//2, b):
                res[0].append("*")
                res[1].append("*")
            res[0][0] = "c"
    else:
        if not n in pattern:
            ok = False
        else:
            last_row = from_pattern(res, n, b)
            star(res, last_row, a, b)
    print("Case #" + str(i+1) + ":")
    if not ok:
        print("Impossible")
    else:
        if a != r: res = rev(res)
        for row in res: print("".join(row))
        
    