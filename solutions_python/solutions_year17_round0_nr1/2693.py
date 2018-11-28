#!/usr/bin/env python

import sys

def pancakes(S, K):
    S = list(S)
    count = 0

    for x in range(0, len(S) - K + 1):
        if S[x] == '-':
            for y in range(x, x + K):
                S[y] = '+' if S[y] == '-' else '-'
            count = count + 1
    return str(count) if "".join(S[-K:]) == "+" * K else "IMPOSSIBLE"    

num = sys.stdin.readline()

for x in range(1, int(num) + 1):
    pattern, K = sys.stdin.readline().split(" ")
    print "Case #" + str(x) + ": " + pancakes(pattern, int(K))
