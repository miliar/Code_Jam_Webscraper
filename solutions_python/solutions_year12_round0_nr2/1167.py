#!/usr/bin/env python3
import sys
import math

def best_suprising(score):
    if score == 0:
        return 0
    div3 = score // 3
    mod3 = score % 3
    if mod3 == 0 or mod3 == 1:
        return div3+1
    elif mod3 == 2:
        return div3+2
        

def best_unsuprising(score):
    div3 = score // 3
    if score % 3 == 0:
        return div3
    else:
        return div3+1

def max_at_least_p(S, p, scores):
    count = 0
    for score in scores:
        if best_unsuprising(score) >= p:
            count += 1
        elif best_suprising(score) >= p and S > 0:
            count += 1
            S -= 1
    return count

with open(sys.argv[1], 'r') as f:
    T = int(f.readline())
    i = 0
    while i < T:
        N, S, p, *t = map(int,f.readline().split())
        print("Case #%d: %d" % (i+1, max_at_least_p(S, p, t)))
        i += 1
