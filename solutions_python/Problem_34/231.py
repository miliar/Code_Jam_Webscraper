#!/usr/bin/python
"Google Qualification - A"

import re

line = raw_input().split()
L = int(line.pop(0))
D = int(line.pop(0))
N = int(line.pop(0))

words = {}
for w in range(0, D):
    words[w] = raw_input().strip()
    assert re.search(r'^[a-z]+$', words[w])
    #print 'word', w, words[w]

cases = {}
for c in range(1, N + 1):
    cases[c] = raw_input().strip().replace('(', '[').replace(')', ']')
    assert re.search(r'^[a-z\[\]]+$', cases[c])
    case = re.compile('^%s$' % cases[c])
    wc = 0
    for w in range(0, D):
        if case.search(words[w]):
            wc += 1
    print 'Case #%d: %s' % (c, wc)
