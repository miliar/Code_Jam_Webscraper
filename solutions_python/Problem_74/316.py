#!/usr/bin/env python3

def calc(a):
        p1 = p2 = 1 # position
        f1 = f2 = 0 # idle moment
        n = int(a[0])
        for i in range(n):
                r = a[i*2+1]
                p = int(a[i*2+2])
                if r == 'O':
                        f1 = max(f1+abs(p-p1),f2) + 1
                        p1 = p
                else:
                        f2 = max(f2+abs(p-p2),f1) + 1
                        p2 = p
        return max(f1,f2)

T = int(input())
for i in range(T):
        a = input().split()
        print("Case #{0}: {1}".format(i+1, calc(a)))
