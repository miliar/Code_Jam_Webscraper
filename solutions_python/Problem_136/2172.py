#!python
#-*- encoding:utf-8 -*-
import sys, math

def solve(C, F, X):
    g1 = 0
    g2 = 2
    g3 = g2 + F
    t_firm = 0
    t2 = X / g2
    t = t_firm + t2
    t_new =  t_firm + C / g2 + X / g3
    while t > t_new:
        g1 = g2
        g2 = g3
        g3 = g2 + F
        t_firm = t_firm + C / g1
        t2 = X / g2
        t = t_firm + t2
        t_new = t_firm + C / g2 + X / g3
    return t

if __name__ == "__main__":
    cases = int(raw_input())
    for i in range(cases):
        C, F, X = map(float, raw_input().split())
        result = round(solve(C, F, X), 7)
        print "Case #{0}: {1:.7f}".format(i+1, result)
