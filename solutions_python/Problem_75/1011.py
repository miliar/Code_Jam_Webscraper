#!/usr/bin/env python

cases = int(raw_input())
for case in range(cases):
    line = raw_input().split(' ')
    ncombinations = int(line.pop(0))
    comb = {}
    for i in range(ncombinations):
        s = line.pop(0)
        comb[s[:2]] = s[2]
        comb[s[1::-1]] = s[2]
    opposed = {}
    nop = int(line.pop(0))
    for i in range(nop):
        s = line.pop(0)
        opposed[s[0]] = s[1]
        opposed[s[1]] = s[0]
    n = int(line.pop(0))
    str = line.pop(0)
    assert(len(str) == n)
    res = ""
    #print "combine:", comb
    #print "reset:", opposed
    #print "input:", str
    for i in str:
        res += i
        c = comb.get(res[-2:])
        while c:
            res = res[:-2] + c
            c = comb.get(res[-2:])
        if opposed.get(res[-1]) and opposed.get(res[-1]) in res:
            #print "reset", str
            res = ''
        
    print "Case #%d: [%s]" % (case + 1, ', '.join(res))
