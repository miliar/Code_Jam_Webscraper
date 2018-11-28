#!/usr/bin/python

import sys
import fileinput
import string

input = fileinput.input()

T = int(input.next().strip())

trantab = string.maketrans('abcdefghijklmnopqrstuvwxyz',
                           'yhesocvxduiglbkrztnwjpfmaq')

for tcase in xrange(T):
    print 'Case #%d:' % (tcase + 1),
    line = input.next().strip()
    print line.translate(trantab)
