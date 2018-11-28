#!/usr/bin/env python

d = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l',
        'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a',
        'x': 'm', 'z':'q', 'q':'z'}

T = int(raw_input())
for i in range(T):
    es = raw_input()
    l = len(es)
    s = ''
    for j in range(l):
        s += d[es[j]]
    print 'Case #%d: %s' % (i+1,s)
