#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
import math
import sys

def solve(A, B):
    sqrt = math.sqrt(A)
    if sqrt > int(sqrt):
        lowest = int(sqrt) + 1
    else:
        lowest = int(sqrt)
    highest = int(math.sqrt(B))
    
    cnt = 0
    for n in range(lowest, highest + 1):
        sq = n * n
        if palindrome(n) and palindrome(sq):
            cnt += 1
            
    return cnt
    
def palindrome(n):
    s = str(n)
    for i in range(len(s)):
        if s[i] != s[-i - 1]:
            return False
    print(n, "is a palindrome")
    return True
    
# main
me = sys.argv[0].split("/")[-1].replace(".py", "")
file = me + "-sample"
file = me + "-small-attempt0"
#file = me + "-large"

with open(file + ".in", "r") as fdin:
    with open(file + ".out", "w") as fdout:

        T = int(fdin.readline())
        for ncase in range(T):
            A, B = [int(x) for x in fdin.readline().split()]

            result = solve(A, B)
    
            line = "Case #%d: %s" % (ncase + 1, result)
            print(line)
            fdout.write("%s\n" % line)
    