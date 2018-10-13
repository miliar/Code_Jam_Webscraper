#!/usr/bin/env python

import sys
from operator import mul

vow = set(['a', 'e', 'i', 'o', 'u'])

def Solve(word, n):
    ltrs = list(word)
    for i in range(len(ltrs)):
        if ltrs[i] in vow: ltrs[i] = '0'
        else: ltrs[i] = '1'
    #ltrs = map(int, ltrs)
    sub = "".join(map(str, [1]*n))
    pat = "".join(ltrs)
    res = 0
    pos = 0
    occ = 0
    resset = set()
    while(pat.find(sub, pos) != -1):
        pos = pat.find(sub, pos)
        left = pos+1
        right = len(pat)-pos-n+1
        #res += left*right
        for i in range(pos+1):
            for j in range(pos+n, len(pat)+1):
                resset.add((i, j))
        #print pos, sub, pat, res
        pos += 1
        #occ += 1
    #res -= occ
    return len(resset)

def main():
    infile = open(sys.argv[1], 'r')
    inp = infile.readlines()
    T = int(inp[0])
    strn = 1
    for i in range(T):
        (word, n) = inp[strn].split()
        n = int(n)
        strn += 1
        print "Case #"+str(i+1)+': '+str(Solve(word, n))


if __name__=='__main__':
    main()
