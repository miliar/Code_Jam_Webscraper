#!/usr/bin/env python3

from fractions import gcd

def avg(a):
        aa = list(a)
        return sum(aa) / len(aa)

def calc(n, a):
        res = []
        owp = {}
        for i in range(n):
                r = 0
                m = 0
                for j in range(n):
                        if a[i][j] == '.': continue
                        total = sum(1 for k in range(n) if a[j][k] != '.' and k != i)
                        won = sum(1 for k in range(n) if a[j][k] == '1' and k != i)
                        r += won/total
                        m += 1
                owp[i] = r / m
                        
        for i in range(n):
                total = sum(1 for k in range(n) if a[i][k] != '.')
                won = sum(1 for k in range(n) if a[i][k] == '1')
                wp = won/total
                oowp = avg(owp[k] for k in range(n) if a[i][k] != '.')
                res.append(wp * 0.25 + owp[i] * 0.5 + oowp * 0.25)

        return res

t = int(input())
for i in range(t):
        n = int(input())
        a = []
        for k in range(n):
                a.append(input())
        print("Case #{0}:".format(i+1))
        for r in calc(n, a):
                print("{0:.8f}".format(r))
