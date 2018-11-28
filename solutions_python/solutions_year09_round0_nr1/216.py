from __future__ import division, print_function
import string
import re

def cj1(fInP, fOutP):
    fIn = open(fInP, 'r')
    fOut = open(fOutP, 'w')
    cases = fIn.readline()
    L, D, N = (int(x) for x in string.split(cases))
    words = ""
    for d in range(0, D):
        words += fIn.readline() + " "
    for n in range(0, N):
        search = fIn.readline()
        search = search.replace('(', '[')
        search = search.replace(')', ']')
        k = 0
        for match in re.finditer(search, words):
            k += 1
        fOut.write('Case #' + str(n+1) + ': ' + str(k) + '\n')
