#!/usr/bin/env python3

T = int(input())

def solve(casei):
    line = input().split(" ")
    S = list(str(line[0]))
    mylen = len(S)
    K = int(line[1])
    cnt = 0
    for i in range(0, mylen):
        if (S[i] == '-'):
            if (i + K <= mylen): # flip
                cnt = cnt + 1
                for j in range(i, i + K):
                    if S[j] == '-': S[j] = '+'
                    else: S[j] = '-'
            else:
                cnt = -1
                break
    ans = cnt
    if ans == -1:
        print("Case #{}: IMPOSSIBLE".format(casei))
    else:
        print("Case #{}: {}".format(casei, ans))

for i in range(1, T+1):
    solve(i)
