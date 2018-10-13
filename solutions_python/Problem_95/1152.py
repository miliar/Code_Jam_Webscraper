#!/usr/bin/env python
#-*- coding:utf-8 -*-

from string import ascii_lowercase
from pprint import pprint
import sys, os
sample_googlerese = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
"""
sample_answer = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
"""
char_map = dict()
for c in ascii_lowercase:
    char_map[c] = ""
char_map['q'] = 'z'
char_map[' '] = ' '

def make_char_mapping():
    for a,g in zip(sample_answer, sample_googlerese):
        if g in ascii_lowercase:
            char_map[g] = a
    for c in ascii_lowercase:
        if not c in char_map.values():
            char_map['z'] = c

def decode(input_str):
    output = list()
    for c in input_str:
        if not c == '\n':
            output.append(char_map[c])
    return ''.join(output)

if __name__ == "__main__":
    make_char_mapping()
    filename = sys.argv[1]
    template = "Case #%d: %s"
    with open(filename) as r:
        casenum = int(r.readline())
        for i in xrange(casenum):
            input_str = r.readline()
            print template % (i + 1, decode(input_str))
