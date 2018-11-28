#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

import sys

def debug(a): sys.stderr.write(str(a) + '\n')
def readarray(foo): return [foo(e) for e in raw_input().split()]
def readint(): return int(raw_input().strip())

debug = lambda x: None

def decrypt(line):
    from string import maketrans
    trans = maketrans(
        'z'
        'y qee'
        'ejp mysljylc kd kxveddknmc re jsicpdrysi'
        'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
        'de kr kd eoya kw aej tysr re ujdr lkgc jv',
        'q'
        'a zoo'
        'our language is impossible to understand'
        'there are twenty six factorial possibilities'
        'so it is okay if you want to just give up')
    debug('abcdefghijklmnopqrstuvwxyz'.translate(trans))
    return line.translate(trans)

T = readint()
for i in xrange(T):
    line = raw_input()
    debug(line)
    print('Case #{0}: {1}'.format(i + 1, decrypt(line)))
