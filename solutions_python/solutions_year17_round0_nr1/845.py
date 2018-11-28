#!/usr/bin/env python
# -*- coding: utf-8 -*-

def flip_pancakes(s , k):
    flip_count = 0
    for i, p in enumerate(s):
        if p == '+':
            continue
        if i >= len(s) - k + 1:
            return "IMPOSSIBLE"
        for j in xrange(i, i+k):
            if s[j] == '+':
                s[j] = '-'
            else:
                s[j] = '+'
        flip_count += 1
    return flip_count

def solve(S, K):
    return flip_pancakes(list(S), int(K))

if __name__ == "__main__":
    test_cases = input()

    for i in xrange(1, test_cases+1):
        S, K = raw_input().split(" ")
        print "Case #{}: {}".format(i, solve(S, K))
