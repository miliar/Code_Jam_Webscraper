#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Izidor Matušov <izidor.matusov@gmail.com>
# Date:   14.04.2012

trans = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}

import sys
import string

text = "".join(sys.stdin.readlines()[1:]).lower()
trans[' '] = ' '
trans['\n'] = '\n'
trans['q'] = 'z'
trans['z'] = 'q'
for i, line in enumerate(text.splitlines(), 1):
    line = line.strip()
    for x in line:
        if x not in trans:
            print "!!!!Missing", x
    t = "".join(trans.get(x, '?') for x in line)
    print "Case #%d: %s" % (i, t)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
