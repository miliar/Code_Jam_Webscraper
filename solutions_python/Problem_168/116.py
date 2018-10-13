#!/usr/bin/env python3

def int2dir(x):
    if x == '^':
        return 0
    if x == '>':
        return 1
    if x == 'v':
        return 2
    if x == '<':
        return 3

dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

def move(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def is_in(p, r, c):
    return (0 <= p[0] and p[0] < r and 0 <= p[1] and p[1] < c)

def calcdir(arr, r, c):
    newarr = {}
    for a in arrows:
        newarr[a] = [arr[a], [None for d in range(4)]]
        for d in range(4):
            pos = move(a, dirs[d])
            while is_in(pos, r, c) and pos not in arr:
                pos = move(pos, dirs[d])
            if is_in(pos, r, c):
                newarr[a][1][d] = pos
    return newarr


def test(arr):
    for a in arr:
        if arr[a][1][arr[a][0]] is None:
            return False
    return True

def popr(arr):
    ret = 0
    for a in arr:
        opts = arr[a][1]
        if opts[arr[a][0]] == None:
            for i in range(4):
                if opts[i] is not None:
                    arr[a][0] = i
                    ret += 1
                    break
            if opts[arr[a][0]] == None:
                return None
    return ret


T = int(input())

for t in range(1, T + 1):
    r, c = (int(x) for x in input().split())

    arrows = {}

    for i in range(r):
        row = input()
        for j, char in enumerate(row):
            if char != '.':
                arrows[(i,j)] = int2dir(char)

    arrows = calcdir(arrows, r, c)
    ret = popr(arrows)
    print("Case #{}: {}".format(t, 'IMPOSSIBLE' if ret == None else ret))


