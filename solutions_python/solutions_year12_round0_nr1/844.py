#!/usr/bin/python

import os, sys, copy, time

inputs = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv'''

outputs = '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up'''

lang_map = {}
for key, value in zip(inputs, outputs):
    lang_map[key] = value

lang_map['y'] = 'a'
lang_map['e'] = 'o'
lang_map['q'] = 'z'
lang_map['z'] = 'q'

def solve(line):
    return  ''.join([lang_map[c] for c in line])

lines = sys.stdin.readlines()
lines.pop(0)

case = 0
while lines:
    case += 1
    line = lines.pop(0)

    sys.stdout.write('Case #%d: %s' % (case, solve(line)))
