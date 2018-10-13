#!/usr/bin/env python
#-*- coding: ISO-8859-1 -*-

import sys

file_in = 'A-small.in'
file_out = 'A-small.out'
#         'abcdefghijklmnopqrstuvwxyz'
from_to = 'yhesocvxduiglbkrztnwjpfmaq'

def solve(G):
    result = ''
    
    for l in G:
        b = ord(l)
        if b == 32:
            result += ' '
        else:
            result += from_to[b - 97]
    
    return result

if __name__ == '__main__':
    i = open(file_in, 'r')
    o = open(file_out, 'w')
    T = int(i.readline().strip())
    for case in xrange(T):
        G = i.readline().strip()
        result = solve(G)
        o.write('Case #%d: %s\n' % (case + 1, result))
    o.close()
    i.close()
    sys.exit(0)
