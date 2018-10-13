#!/usr/bin/python3
t = int(input())


for it in range(1, t+1) :
    ist, ik = input().split()
    s = [1 if c == '+' else 0 for c in ist]
    k = int(ik)
    n = 0
    for i in range(len(s)-k+1) :
        if s[i] == 0:
            n += 1
            for j in range(i, i+k):
                s[j] = not s[j]
    if min(s) == 0: n = "IMPOSSIBLE"
    print("Case #%d:"% it, n)