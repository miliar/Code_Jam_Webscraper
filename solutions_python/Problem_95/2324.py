#!/usr/bin/env python

import sys

def is_char(c):
    return ord(c) >= ord('a') and ord(c) <= ord('z')

def construct(map, inLine, outLine):
    for i,o in zip(inLine, outLine):
        if not is_char(i):
            assert not is_char(o)
            continue
        if i in map:
            assert o == map[i]
        map[i] = o

def construct_all():
    map = {'y': 'a', 'e': 'o', 'q': 'z'}
    inLines = ("""ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv""").split("\n")
    outLines = [s[len("Case #1: "):] for s in ("""Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up""").split("\n")]
    for inLine, outLine in zip(inLines, outLines):
        construct(map, inLine, outLine)
    alphaIn = set([chr(c + ord('a')) for c in xrange(0,26)])
    alphaOut = set(alphaIn)
    for cIn,cOut in map.iteritems():
        alphaIn.remove(cIn)
        alphaOut.remove(cOut)
    map[list(alphaIn)[0]] = list(alphaOut)[0]
    return map

def translate(map, s):
    return "".join((map[c] if is_char(c) else c) for c in s)

def main():
    map = construct_all()
    case = 0
    for line in sys.stdin:
        if case > 0:
            print 'Case #%d: %s' % (case, translate(map, line).strip())
        case += 1

main()
