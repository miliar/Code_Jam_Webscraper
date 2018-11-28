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
        a1 = int(fp.readline())-1
        l1 = []
        for i in range(4):
            l1.append(fp.readline().split())

        a2 = int(fp.readline())-1
        l2 = []
        for i in range(4):
            l2.append(fp.readline().split())

        ans = list(set(l1[a1]).intersection(l2[a2]))
        if len(ans) > 1:
            print "Case #%s: Bad magician!" % (t+1,)
        elif len(ans) == 0:
            print "Case #%s: Volunteer cheated!" % (t+1,)
        else:
            print "Case #%s: %s" % (t+1, ans[0])



