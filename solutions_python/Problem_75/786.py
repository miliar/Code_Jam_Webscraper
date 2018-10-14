#!/usr/bin/env python

from sys import stdin

def fixup(res,combos,oppose):
    last = ''.join(res[-2:])
    if last in combos:
        res.pop(); res.pop(); res.append(combos[last])
        return True
    for x in res[:-1]:
        if x+res[-1] in oppose or res[-1]+x in oppose:
            while res: res.pop()
            break
    return False

t = int(stdin.readline())
for case in xrange(1,t+1):
    inpt = stdin.readline().split()
    c = int(inpt[0])
    d = int(inpt[c+1])
    n = int(inpt[c+d+2])
    combos = dict((x[:2],x[2]) for x in inpt[1:c+1])
    combos.update(dict((x[1]+x[0],x[2]) for x in inpt[1:c+1]))
    oppose = set(inpt[c+2:c+d+2])
    elts = list(inpt[c+d+3])
    res = [elts[0]]
    for e in elts[1:]:
        res.append(e)
        while fixup(res,combos,oppose): pass
    print "Case #%d: [%s]"%(case,", ".join(res))
