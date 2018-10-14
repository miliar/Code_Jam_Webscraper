#!/usr/bin/python

import sys
import string

line = iter(sys.stdin.readlines())

T = int(next(line))

for case in xrange(1,T+1):
    print "Case #%d:" % case, next(line).translate(string.maketrans('abcdefghijklmnopqrstuvwxyz',
                                                                    'yhesocvxduiglbkrztnwjpfmaq')),
