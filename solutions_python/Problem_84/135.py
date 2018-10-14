#!/usr/bin/env python3

def calc(r, c, a):
        for i in range(r):
                for j in range(c):
                        if a[i][j] == '#':
                                if i == r - 1 or j == c - 1 or a[i][j+1] != '#' or a[i+1][j] != '#' or a[i+1][j+1] != '#':
                                        return ['Impossible']
                                a[i][j] = a[i+1][j+1] = '/'
                                a[i+1][j] = a[i][j+1] = '\\'
                                
        return a

t = int(input())
for i in range(t):
        r, c = [int(a) for a in input().split()]
        a = []
        for k in range(r):
                a.append(list(input()))
        print("Case #{0}:".format(i+1))
        for s in calc(r, c, a):
                print(''.join(s))
