from __future__ import print_function, division
from fileinput import input

inp = input()
t = int(inp.readline())

def find(hole):
    if hole % 2 == 0:
        return (hole // 2, hole // 2 - 1)
    return (hole // 2, hole // 2)

def solve(n, k):
    pool1 = n
    pool1_size = 1
    pool2 = n
    pool2_size = 0

    gone = 0
    sat = 1
    while True:
        if gone + sat >= k:
            index = k - gone
            if index <= pool1_size:
                return find(pool1)
            else:
                return find(pool2)

        gone += sat
        sat *= 2

        npool1 = -1
        npool1_size = 0
        npool2 = -1
        npool2_size = 0

        if pool1 % 2 == 0:
            npool1 = pool1 // 2
            npool1_size += pool1_size
            npool2 = pool1 // 2 - 1
            npool2_size += pool1_size
        else:
            npool1 = (pool1-1) // 2
            npool1_size = pool1_size * 2

        if pool2 % 2 == 0:
            npool1 = pool2 // 2
            npool1_size += pool2_size
            npool2 = pool2 // 2 - 1
            npool2_size += pool2_size
        else:
            npool2 = (pool2-1) // 2
            npool2_size += pool2_size * 2

        pool1 = npool1
        pool1_size = npool1_size
        pool2 = npool2
        pool2_size = npool2_size


for case in xrange(t):
    n, k = map(int, inp.readline().split())
    res = solve(n, k)
    print("Case #{}: {} {}".format(case + 1, res[0], res[1]))
