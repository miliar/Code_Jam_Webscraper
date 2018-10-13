#!/usr/bin/env python2.6
import re
import sys

with open(sys.argv[1], "r") as f:
    word_length, lex_size, tests = [int(k) for k in f.readline().strip().split()]
    
    words = [f.readline().strip() for i in range(lex_size)]
    tests = [f.readline().strip() for i in range(tests)]

s = "".join("=%s=" % (w, ) for w in words)

for i, t in enumerate(tests):
    pat = "=(%s)=" % (t.replace("(", "[").replace(")", "]"), )
    matches = re.findall(pat, s)
    print "Case #%d: %d" % (i + 1, len(matches))
    
