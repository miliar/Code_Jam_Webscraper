# ertug (Ertug Karamatli)

import sys
import re
from math import floor

f = file(sys.argv[1])

ln = 0
L = 0
D = 0
N = 0

ldict = []
lpatt = []

#read
for line in f:
    line = line.strip()
    if line == '': continue
    if ln == 0:
        L, D, N = line.split(' ')
        L = int(L)
        D = int(D)
        N = int(N)
    elif ln <= D:
        ldict.append(line)
    elif ln > D:
        lpatt.append(line)
    ln += 1

#parse
parsedpatts = []
for patt in lpatt:
    pstart = False
    pcont = []
    parsedpatt = []

    for c in patt:
        if c == '(':
            pstart = True
            continue
        elif c == ')':
            pstart = False
            parsedpatt.append(pcont)
            pcont = []
            continue
        elif pstart == False:
            parsedpatt.append(c)
            continue

        if pstart:
            pcont.append(c)

    parsedpatts.append(parsedpatt)


cases = []
for i in xrange(len(parsedpatts)):
    cases.append(0)

case = 0
for p in parsedpatts:
    for w in ldict:
        ismatched = False
        for i in xrange(len(w)):
            if w[i] in p[i]:
                ismatched = True
            else:
                ismatched = False
                break
        if ismatched:
            cases[case] += 1
    case += 1


cn = 1
for c in cases:
    print 'Case #%s: %s' % (cn, c)
    cn += 1

