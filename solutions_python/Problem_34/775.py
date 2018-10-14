#!/usr/bin/python
import re

header = raw_input()

#L - length, D - lines, N - test case
L, D, N = header.split(" ")
word_list = [ raw_input() for i in xrange(int(D)) ]
test_cases = [ re.compile(raw_input().replace("(","[").replace(")","]")) for i in xrange(int(N)) ]

idx = 1
for test_case in test_cases:
        print "Case #%d: %d" % (idx, len([ e for e in word_list if re.match(test_case,e) != None ]))
        idx += 1
