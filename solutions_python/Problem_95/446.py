#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
"""
before = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
          'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
          'de kr kd eoya kw aej tysr re ujdr lkgc jv',
          'y qee']

after = ['our language is impossible to understand',
         'there are twenty six factorial possibilities',
         'so it is okay if you want to just give up',
         'a zoo']

table = dict()
for pair in zip(before, after):
    tmp = zip(pair[0], pair[1])
    print pair[0], pair[1]
    for t in tmp:
        if t[0] not in table:
            table[t[0]] = t[1]
"""

table = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

T = int(sys.stdin.readline())
for i in range(1, T+1):
    l = sys.stdin.readline()
    tmp = range(len(l) - 1)
    for j in range(len(l) - 1):
        tmp[j] = table[l[j]]
    print "Case #%d:" % i, "".join(tmp)
