#! /usr/bin/env python -u
# coding=utf-8
import sys

__author__ = 'xl'

if __name__ == "__main__":
    fp = open("A.in")
    sys.stdout = open("A.out", "w")
    # fp = sys.stdin

    T = int(fp.readline())
    for t in range(T):
        N = int(fp.readline())

        strs = []
        for i in range(N):
            strs.append(fp.readline().strip())

        a = "_%s_" % strs[0]
        b = "_%s_" % strs[1]

        i = 0
        opr = 0
        bad = False
        while len(a) > i and len(b) > i:
            if a[i] == b[i]:
                i+=1
                continue
            elif a[i] == b[i-1]:
                a = a[:i]+a[i+1:]
                opr+=1
            elif b[i]==a[i-1]:
                b = b[:i]+b[i+1:]
                opr+=1
            else:
                bad = True
                break

        if len(a)!=len(b) and not bad:
            bad = True

        print "Case #%s: %s" % (t + 1, opr if not bad else "Fegla Won")



