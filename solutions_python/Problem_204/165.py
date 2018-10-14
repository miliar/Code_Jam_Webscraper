#!/usr/bin/env python

import collections, itertools

fin = open("2.in", "r")
fout = open("2.out", "w")

used = [[False for i in range(8)] for j in range(2)]

def work(a, b, c):
    return 10 * a >= 9 * b * c and 10 * a <= 11 * b * c

T = int(fin.readline())
for t in range(T):
    print str(t+1)
    N, P = map(int, fin.readline().split())
    R = map(int, fin.readline().split())
    Q = []
    for i in range(N):
        Q.append(map(int, fin.readline().split()))
        map(lambda x: x, Q[i])

    l = 1
    ans = 0
    done = False
    while not done:
        if l > 1000000:
            break
        sol = [-1 for i in range(N)]
        for i in range(N):
            Q[i] = [x for x in Q[i] if 10 * x >= 9 * R[i] * l]
        for i in range(N):
            if len(Q[i]) == 0:
                done = True
                break
            for j in range(len(Q[i])):
                if work(Q[i][j], R[i], l):
                    sol[i] = j
                    break
        solved = True
        for i in range(N):
            if sol[i] == -1:
                solved = False
                break
        if solved:
            ans += 1
            for i in range(N):
                del Q[i][sol[i]]
        else:
            l += 1

    fout.write("Case #" + str(t+1) + ": " + str(ans) + "\n")
