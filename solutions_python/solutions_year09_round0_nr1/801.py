#!/usr/bin/env python
import re

f = open('A-large.in', 'r')

L, D, N = f.readline().split()
wordlist = [f.readline().strip() for i in range(int(D))]
caselist = [f.readline().strip() for i in range(int(N))]

optlist = []
splitter = re.compile(r'\([a-z]+\)|[a-z]')
multichar = re.compile(r'\([a-z]+\)')
singlechar = re.compile(r'[a-z]')
casenum = 1
for case in caselist:
    count = 0
    optlist = splitter.findall(case)
    list = []
    for opt in optlist:
        if multichar.match(opt):
            current = singlechar.findall(opt)
            list.append(current)
        else:
             list.append([opt])
    for word in wordlist:
        comparer = map(None, word, list)
        contained = True
        for letter in comparer:
            if letter[0] not in letter[1]:
                contained = False
                break
        if contained:
            count += 1
    print 'Case #%d: %d' % (casenum, count)
    casenum += 1


