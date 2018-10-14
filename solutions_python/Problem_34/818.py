#!/usr/bin/env python
import re

def pat2reg(pat):
    pat = pat.replace('(', '[')
    pat = pat.replace(')', ']')
    return pat

#with open('0-attempt.in', 'r') as file:
with open('A-large.in', 'r') as file:
    # Read language definitions
    tmp = file.readline().strip().split(" ")
    L = int(tmp[0]); D = int(tmp[1]); N = int(tmp[2])
    # Read words
    words = []
    for i in xrange(D):
        word = file.readline().strip()
        if len(word) == L:
            words.append(word)
    assert len(words) == D
    # Read patterns and create regular expressions
    patterns = []
    full = []
    for i in xrange(N):
        pat = pat2reg(file.readline().strip())
        full.append(pat)
        patterns.append(re.compile(pat))
    assert len(patterns) == N

    # Do the dance :)
    for i in xrange(N):
        count = 0
        for j in xrange(D):
            # print words[j], " -- ", full[i]
            if patterns[i].match(words[j]) != None:
                count += 1
        print "Case #%d: %d" % (i + 1, count)
