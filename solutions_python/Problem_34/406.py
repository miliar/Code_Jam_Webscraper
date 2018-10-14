#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys       import stdin
from itertools import izip

def filterwords(wordset, avail, pos):
    for word in wordset:
        #print word, pos
        if word[pos] in avail:
            yield word

L, D, N = map(int, stdin.readline().split())
langwords = frozenset([stdin.readline().strip() for x in xrange(D)])

for line, case in izip(stdin, xrange(N)):
    line = line.strip()
    #print "LINE", line
    pos, startpos, endpos = 0, 0, 0
    words = langwords.copy()

    while startpos < len(line) and len(words) > 0:
        #print "START", startpos
        if line[startpos] == '(':
            endpos   = line.find(')', startpos+1)
            words    = frozenset(filterwords(words, line[startpos+1:endpos], pos))
            startpos = endpos+1
        else:
            words     = frozenset(filterwords(words, line[startpos], pos))
            startpos += 1
        pos += 1
    print "Case #%d: %d" % (case+1, len(words))
