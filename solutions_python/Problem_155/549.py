#!/usr/bin/env python3

import sys

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for t in range(1, T+1):
        smaxstr, strshy = sys.stdin.readline().split()
        strshy = strshy.strip()
        shyPeople = [int(x) for x in strshy]
        smax = int(smaxstr)+1 #Caution with this!

        standing = 0
        extra = 0
        for i in range(smax):
            if i <= standing:
                standing = standing + shyPeople[i]
            else:
                dif = i - standing
                extra = extra + dif
                standing = standing + shyPeople[i] + dif

        print ("Case #%d: %d" % (t, extra))
