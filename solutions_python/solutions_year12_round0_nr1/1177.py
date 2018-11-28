#!/usr/bin/env python
# Karl WNW
# input stdin, output stdout

import sys
from string import maketrans

en = "abcdefghijklmnopqrstuvwxyz"
go = "ynficwlbkuomxsevzpdrjgthaq"

def translate(i):
    l = sys.stdin.readline().split()
    translation = []
    for w in l:
        transtab = maketrans(go, en)
        translation.append(w.translate(transtab))
    print "Case #%d: %s" % (i, ' '.join(translation))

def main():
    C = int(sys.stdin.readline().strip())
    for t in range(C):
        translate(t+1)
    
if __name__ == '__main__':
    main()

    
