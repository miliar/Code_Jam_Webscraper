#!/usr/bin/python

import sys

INPUT = sys.stdin
INPUT = open(sys.argv[1],'r')

def getline():
    return INPUT.readline()[:-1]

def trace(*strs):
    print >> sys.stderr, '..',
    for str in strs:
        print >> sys.stderr, str,
    print >> sys.stderr

import re

(L, D, N) = map(int, getline().split())

corpus = ''
for d in range(D):
    known_word = getline()
    corpus += known_word + '\n'
# trace(corpus)

for case_num in range(1, N+1):
    trace()
    trace( 'Case #', case_num )

    pattern = getline()
    regex = pattern.replace('(','[').replace(')',']')
    regex = '(?m)^' + regex + '$'
    answer = len(re.findall( regex, corpus ))

    print 'Case #%d: %s' % (case_num, answer)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
