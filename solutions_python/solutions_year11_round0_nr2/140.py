#! /usr/bin/python

import sys, itertools

def getline():
    return sys.stdin.readline().strip()

def out(s):
    if False:
        print s

def read_combine(l):
    c = {}
    for i in l:
        c[tuple(sorted([i[0], i[1]]))] = i[2]
    return c

def read_oppose(l):
    c = {}
    for x, y in l:
        if not c.has_key(x):
            c[x] = []
        if not c.has_key(y):
            c[y] = []
        c[x].append(y)
        c[y].append(x)
    return c

def solve(casenum):
    data = getline().split()
    C = int(data[0])
    combine = read_combine(data[1:C + 1])
    D = int(data[C + 1])
    oppose = read_oppose(data[C + 2:C + D + 2])
    N = int(data[C + D + 2])
    elements = data[C + D + 3]
    answer, answerDict = [], {}
    out((combine, oppose, elements))

    for i in range(N):
        cleared = False
        e = elements[i]
        out(('start:', answer, answerDict, e))
        if answer:
            pair = tuple(sorted([answer[-1], e]))
            replacement = combine.get(pair)
            if replacement:
                answerDict[answer.pop()] -= 1
                e = replacement

        for o in oppose.get(e, []):
            if answerDict.get(o):
                answer, answerDict = [], {}
                out(('clear:', answer, answerDict))
                cleared = True

        if not cleared:
            answer.append(e)
            answerDict[e] = answerDict.get(e, 0) + 1
            out(('end:  ', answer, answerDict, e))

    print 'Case #%d: [%s]' % (casenum, ', '.join(answer))

cases = int(getline())
for case in xrange(cases):
    solve(case + 1)
