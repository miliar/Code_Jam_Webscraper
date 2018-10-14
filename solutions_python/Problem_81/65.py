#!/usr/bin/env python
# coding=utf-8
from __future__ import division
from sys import stdin

def avg(data):
    res = sum(data)/len(data)
    #print("avg({0}):{1}".format(data,res))
    return res

def averageValues(mask, data, n):
    return [ avg( [ data[i][j] for j in range(n) if mask[i][j] != '.' ] ) for i in range(n)]

def solve(caseNo):
    print("Case #{0}:".format(caseNo))
    n = int(stdin.readline().strip())
    plays = [ stdin.readline().strip() for i in range(n)]
    wins = [ [ 1 if plays[i][j] == '1' else 0 for j in range(n) ] for i in range(n)]
    op = [ len([1 for j in range(n) if plays[i][j] != '.']) for i in range(n) ]
    #print(plays)
    #print(wins)
    wp = averageValues(plays, wins, n)
    #print(wp)
    owp = averageValues(plays, [ [ (wp[j]*op[j] - wins[j][i])/(op[j]-1) for j in range(n)] for i in range(n)], n)
    #print(owp)
    oowp = averageValues(plays, [ owp for i in range(n)], n)
    #print(oowp)
    for i in range(n):
        print("{0:.9f}".format(0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i]))

if __name__ == "__main__":
    cases = int(stdin.readline().strip())
    for i in range(cases):
        solve(i+1)
