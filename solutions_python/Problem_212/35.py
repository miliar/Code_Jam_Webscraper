#!/usr/bin/python3

import sys

nRounds = int(sys.stdin.readline().strip())

known_pattern = [
        [],
        [],
        [(0,2)],
        [(0,1,1), (0,3,0), (0,0,3)],
        [(0,4,0,0), (0,1,0,1), (0,0,2,0), (0,2,1,0), (0,0,1,2), (0,0,0,4)],
    ]

mem = {}

def recurse(rds, p):
    if rds in mem:
        return mem[rds]
    result = 0
    for pat in known_pattern[p]:
        next_rds = []
        avail = True
        for i in range(0,p):
            entry = rds[i] - pat[i]
            if entry < 0:
                avail = False
                break
            next_rds.append(rds[i] - pat[i])
        if avail:
            result = max(result, recurse(tuple(next_rds), p) + 1)
    is_zero = True
    for i in range(1, p):
        if (rds[i] != 0):
            is_zero = False
    if result == 0 and not is_zero:
        result = 1
    mem[rds] = result
    return result

for _ in range(0, nRounds):
    sys.stdout.write("Case #{}: ".format(_+1))
    strInput = sys.stdin.readline().strip()
    # do something
    N = int(strInput.split(' ')[0])
    P = int(strInput.split(' ')[1])
    G = [0] * P
    strInput = sys.stdin.readline().strip().split(' ')
    for i in range(0, N):
        rd = int(strInput[i]) % P
        G[rd] = G[rd] + 1
    mem = {}
    result = recurse(tuple(G), P)
    result = result + G[0]
    sys.stdout.write("{}\n".format(result))
    sys.stdout.flush()
