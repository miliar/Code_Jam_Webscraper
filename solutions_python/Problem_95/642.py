#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
translator = { 'a' : 'y',
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
               ' ' : ' '}

def compute(line):
    trans = "";
    for c in line:
        trans += translator[c]
    return trans

f=open(sys.argv[1])
lines=f.read().split("\n")
nb_lines=int(lines[0])
lines=lines[1:]

for i in range(nb_lines):
    print("Case #%d: %s" % (i+1, compute(lines[i])))
