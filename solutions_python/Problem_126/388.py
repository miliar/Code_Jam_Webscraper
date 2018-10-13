#!/usr/bin/env python

import sys, re

def getNV(word, n, c):
    subs = []
    nv = 0
    for i in range(len(word)):
        for j in range(len(word)):
            w = word[i:len(word)-j]
            cn = re.findall("[^aieou]{%d}"%n, w)
            if len(cn) != 0 :
                nv += 1

    print("Case #%d: %d"%(c, nv))

def main():
    f = open(sys.argv[1], 'r').readlines()
    nbtests = f[0]
    words = []
    c = 1
    for w in f[1:] :
        a,b = w.split()
        getNV(a, int(b), c)
        c += 1

if __name__ == "__main__" :
    sys.exit(main())
