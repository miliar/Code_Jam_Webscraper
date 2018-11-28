#!/usr/bin/python

from sys import stdin
import re


def main():
    L, D, N = map(int, stdin.next().split())
    dict = [stdin.next().strip() for i in range(D)]
    
    ret = 0
    for nn in range(1,N+1):
        word = stdin.next().strip()
        match = dict[:]

        i0 = 0
        for l in range(L):
            if (word[i0]=='('):
                i1 = word.find(')',i0)
                ok = word[i0+1:i1]
                ok = [i for i in ok]
                i0 = i1 + 1
            else:
                ok = [word[i0]]
                i0 += 1

#             print '%s' % match
#             print 'ok %s' % ok
            match = [m for m in match
                     if m[l] in ok]
        print "Case #%d: %d" % (nn, len(match))
        




    
if __name__ == "__main__":
    main()
