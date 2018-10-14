#!/usr/bin/env python
# -*- coding=utf-8 -*-
#****************************************************
# Author: Alex Yang - alex890714@gmail.com
# Last modified: 2012-04-14 07:12
# Filename: ax.py
# Description:
#****************************************************

from sys import stdin, stdout
from StringIO import StringIO

cm = {
    ' ': ' ',
    'a': 'y',
    'b': 'h',
    'c': 'e',
    'd': 's',
    'e': 'o',
    'f': 'c',
    'g': 'v',
    'h': 'x',
    'i': 'd',
    'j': 'u',
    'k': 'i',
    'l': 'g',
    'm': 'l',
    'n': 'b',
    'o': 'k',
    'p': 'r',
    'q': 'z',
    'r': 't',
    's': 'n',
    't': 'w',
    'u': 'j',
    'v': 'p',
    'w': 'f',
    'x': 'm',
    'y': 'a',
    'z': 'q'
}

stdin = open('a.in', 'r')
buff = StringIO()
out = open('a.out', 'w')

t = int(stdin.readline())

for i in xrange(t):
    _in = stdin.readline()
    res = ''
    for c in _in:
        if cm.get(c, None):
            res += cm[c]
    print >>buff, 'Case #%d: %s' % (i + 1, res)

out.write(buff.getvalue())
out.close()
