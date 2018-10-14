#!/usr/bin/env python3

import sys, os, re
import numpy as np
import math
from collections import defaultdict

def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    T = int(input().strip())
    for t in range(1, T+1):
        inp = [int(x) for x in input().strip().split(" ")]
        C = {}
        colors = ["R", "O", "Y", "G", "B", "V"]
        allow = {"R": ["Y", "G", "B"],
             "O": ["B"],
             "Y": ["B", "V", "R"],
             "G": ["R"],
             "B": ["R", "O", "Y"],
             "V": ["Y"]
            } 
        N = inp[0]
        inp = inp[1:]
        for i, l in enumerate(colors):
            C[l] = inp[i]
        #log(C)

        ans = ""

        B = ["." for x in range(N)]

        def is_possible():
            for c in colors:
                s = sum([C[a] for a in allow[c]])
                if C[c] > s: #impossible
                    return False
                else:
                    return True

        def get_max_color(col):
            maxcolor = "."
            maxnum = 0
            allowed = 0
            for c in col:
                if C[c] > maxnum:
                    maxnum = C[c]
                    maxcolor = c
                    allowed = sum([C[x] for x in allow[c]])
                    if B[0] in allow[c]:
                        allowed += 1
                elif C[c] == maxnum:
                    newallowed = sum([C[x] for x in allow[c]])
                    if B[0] in allow[c]:
                        newallowed += 1
                    if newallowed < allowed:
                        maxnum = C[c]
                        maxcolor = c
                        allowed = newallowed
                    
            if maxcolor != '.':
                C[maxcolor] -= 1
            return maxcolor

        if is_possible():  
            B[0] = get_max_color(colors)
            for i in range(1, N):
                #print("".join(B))
                #print(C)
                B[i] = get_max_color(allow[B[i-1]])
                if B[i] == '.':
                    break
            #print("".join(B))

        if sum(C.values()) != 0 or B[0] not in allow[B[-1]]:
            ans = "IMPOSSIBLE"
        else:
            ans = "".join(B)
        print("Case #{}: {}".format(t, ans))

if __name__ == '__main__':
    main()
