#!/usr/bin/python
# -*- coding: utf-8 -*-
## Problem A. Speaking in Tongues (GCJ Qualification Round 2012)

from string import maketrans

def open_fi(fi):
    T = int(raw_input())
    intab = "ynficwlbkuomxsevzpdrjgthaq"
    outab = "abcdefghijklmnopqrstuvwxyz"
    transtab = maketrans(intab, outab)

    for k in xrange(T):
        googlerese = raw_input()
        english = googlerese.translate(transtab)

        ## affichage sol
        char = "Case #%d: %s" %(k+1, english)
        print char


if __name__ == "__main__":
    ## avec un fichier a ouvrir dans le code
    open_fi("A-test.in")
