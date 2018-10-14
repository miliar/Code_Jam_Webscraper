#!/usr/bin/env python
import sys

m = {
    'a' : 'y',
    'b' : 'h',
    'c' : 'e',
    'd' : 's',
    'e' : 'o',
    'f' : 'c',
    'g' : 'v',
    'h' : 'x',
    'i' : 'd',
    'j' : 'u',
    'k' : 'i',
    'l' : 'g',
    'm' : 'l',
    'n' : 'b',
    'o' : 'k',
    'p' : 'r',
    'q' : 'z',
    'r' : 't',
    's' : 'n',
    't' : 'w',
    'u' : 'j',
    'v' : 'p',
    'w' : 'f',
    'x' : 'm',
    'y' : 'a',
    'z' : 'q',
    ' ' : ' ',
}

def mmm(c):
    return m[c]

n = int(raw_input())
for t in range(n):
    line = raw_input()
    line = map(mmm, line)
#    line = [mmm(i) for i in line]
    print 'Case #%d: %s' % (t+1, "".join(line))
