#!/usr/bin/python3

# Given number K
# How many numbers 0< N < A and 0 < M < B exist such that A & B < K?

# 1: one machine generates the 1, the other machine generates... all odd
# numbers!

def debug(*args, **kwargs):
    # print(*args, **kwargs)
    pass

cases = int(input())

for case in range (1, cases + 1):

    (a, b, k) = [int(x) for x in input().split()]
    if a > b:
        # Swap
        c = a
        a = b
        b = c

    count = 0
    for i in range(a):
        for j in range(b):
            if i & j < k:
                debug(i, j)
                count+= 1

    print("Case #%s: %s" % (case, count))
    
