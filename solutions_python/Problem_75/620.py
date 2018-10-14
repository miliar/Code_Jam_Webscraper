#!/usr/bin/env python

from sys import stdin

def solve(combine, opposed, invoke):
    result = ''
    for i in invoke:
        result += i
        while result[-2:] in combine:
            result = result[:-2]+combine[result[-2:]]
        if result[-1] in opposed and opposed[result[-1]] in result:
            result = ''
    return '['+', '.join(list(result))+']'

def main():
    T = int(stdin.readline())
    for i in range(T):
        line = stdin.readline().split()
        C = int(line.pop(0))
        combine = {}
        for j in range(C):
            t = line.pop(0)
            combine[t[0]+t[1]] = t[2]
            combine[t[1]+t[0]] = t[2]
        D = int(line.pop(0))
        opposed = {}
        for j in range(D):
            t = line.pop(0)
            opposed[t[0]] = t[1]
            opposed[t[1]] = t[0]
        N = int(line.pop(0))
        invoke = line.pop(0)
        print "Case #{0}: {1}".format(i+1, solve(combine, opposed, invoke))

main()
