#!/usr/bin/python

import os
import sys

#sys.stdin = open('A-test.in', 'r')
#sys.stdin = open('A-small.in', 'r')
#sys.stdout = open('A-small.out', 'w')
#sys.stdin = open('A-small-attempt0.in', 'r')
#sys.stdout = open('A-small-attempt0.out', 'w')
#sys.stdin = open('A-small-attempt1.in', 'r')
#sys.stdout = open('A-small-attempt1.out', 'w')
sys.stdin = open('A-large.in', 'r')
sys.stdout = open('A-large.out', 'w')

DEBUG = 0 or os.getenv("DEBUG")

if str(DEBUG) == 'log':
    sys.stderr = open('log', 'w')

def debug(*what):
    if DEBUG:
        sys.stderr.write("[DEBUG] " + " ".join(map(str, what)) + "\n")

#-----------------------------------------------------------------------------

Node = [None] * 26

trie = Node[:]

def alpha_ord(c):
    return ord(c) - ord('a')

def push_trie(s):
    global trie, l
    p = trie
    for i in range(l):
        index = alpha_ord(s[i])
        if not p[index]:
            if i == len(s) - 1: p[index] = True
            else: p[index] = Node[:]
        p = p[index]

def n_matches(p):
    i = 0
    q = [(trie, '')]
    while i < len(p):
        if len(q) == 0:
            return 0
        if p[i] == '(':
            i += 1
            s = []
            while i < len(p) and p[i] != ')':
                s.append(p[i])
                i += 1
            q = [(x[0][alpha_ord(c)], x[1] + c) for x in q for c in s if x[0][alpha_ord(c)]]
        else:
            q = [(x[0][alpha_ord(p[i])], x[1] + p[i]) for x in q if x[0][alpha_ord(p[i])]]
        #debug(i, [x[1] for x in q])
        i += 1
    return len(q)

l, d, n = map(int, raw_input().split())

for i in xrange(d):
    push_trie(raw_input())

for case in xrange(n):
    p = raw_input()
    debug()
    debug("Case #%d: %s" % (case + 1, p))
    r = n_matches(p)
    print "Case #%d: %d" % (case + 1, r)
