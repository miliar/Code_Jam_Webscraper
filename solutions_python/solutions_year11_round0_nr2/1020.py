# -*- coding: utf-8 -*-

import sys

result = ''
elements = []
combines = {}
opposeds = {}

def readelement():
    global elements
    element = elements[0]
    elements = elements[1:]
    return element

def addcombine(combinestr):
    global combines
    combines[combinestr[0] + combinestr[1]] = combinestr[2]
    combines[combinestr[1] + combinestr[0]] = combinestr[2]

def addopposed(opposedstr):
    global opposeds
    e1 = opposedstr[0]
    e2 = opposedstr[1]
    if e1 in opposeds:
        opposeds[e1] = opposeds[e1] + e2
    else:
        opposeds[e1] = e2
    if e2 in opposeds:
        opposeds[e2] = opposeds[e1] + e1
    else:
        opposeds[e2] = e1

def checkcombine():
    global result
    if result[-2:] in combines:
        result = result[:-2] + combines[result[-2:]]

def checkopposed():
    global result
    element = result[-1]
    if element in opposeds:
        for opposedelement in opposeds[element]:
            if opposedelement in result[:-1]:
                result = ''

def printresult():
    global result
    retval = '['
    if result <> '':
        for element in result:
            retval += element + ', '
        retval = retval[:-2]
    retval += ']'
    return retval

fin = sys.stdin
T = int(fin.readline())
for case in range(1, T+1):
    result = ''
    elements = fin.readline().split(' ')
    combines = {}
    opposeds = {}
    C = int(readelement())
    for i in range(0, C):
        addcombine(readelement())
    D = int(readelement())
    for i in range(0, D):
        addopposed(readelement())
    N = int(readelement())
    elementlist = readelement()
    for i in range(0, N):
        result += elementlist[i]
        checkcombine()
        checkopposed()
    print 'Case #%d: %s' % (case, printresult())

