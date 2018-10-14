#!/usr/bin/env python

fin = open("1.in", "r")
fout = open("1.out", "w")

def change(x):
    if x == '-':
        return 0
    if x == '+':
        return 1

T = int(fin.readline())
for t in range(T):
    s, K = fin.readline().split()
    s = map(change, list(s))
    K = int(K)
    ans = 0

    for i in range(len(s)-K+1):
        if s[i] == 0:
            ans += 1
            for j in range(i, i+K):
                s[j] = 1 - s[j]

    for i in range(len(s)-K+1, len(s)):
        if s[i] == 0:
            ans = "IMPOSSIBLE"

    fout.write("Case #" + str(t+1) + ": " + str(ans) + "\n")
