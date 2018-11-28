#!/usr/bin/env python
import sys


T = []
M = 0

def CalcTree(r):
    if r >= (M-1)/2:
        return T[r]
    else:
        if T[r][2] == 1:
            return CalcTree(2*r+1) and CalcTree(2*r+2)
        else:
            return CalcTree(2*r+1) or CalcTree(2*r+2)

def PermTree(num):
    n = num
    for r in xrange((M-1) / 2):
        if T[r][1] == 1:
            b = n & 1
            n = n >> 1
            if b:
                T[r][2] = not T[r][0]
            else:
                T[r][2] = T[r][0]

def CountBits(n):
    c = 0
    while n > 0:
        if n & 1:
            c += 1
        n = n >> 1
    return c

def main():
    global T
    global M
    file_in = open("A-small-attempt0.in")
    file_out = open("A-small-attempt0.out", "w")
    #file_out = sys.stdout
    n_tests = int(file_in.readline())
    for i in xrange(n_tests):
        M, V = map(int, file_in.readline().split())
        T = []
        cg = 0
        for j in xrange((M-1)/2):
            G, C = map(int, file_in.readline().split())
            T.append([G, C, G])
            if C == 1:
                cg += 1
        for j in xrange((M+1)/2):
            I = int(file_in.readline().strip())
            T.append(I)
        res = cg+1
        for n in xrange(2**cg):
            PermTree(n)
            v = CalcTree(0)
            if v == V:
                res = min(CountBits(n), res)
        if res == cg+1:
            print >> file_out, "Case #%d: IMPOSSIBLE" % (i+1)
        else:
            print >> file_out, "Case #%d: %d" % (i+1, res)

    #file_out.close()
    #file_in.close()
if __name__ == '__main__':
    main()