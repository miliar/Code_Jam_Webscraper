#!/usr/bin/env python

import sys, re

word_len, words_no, patterns_no = map(int, sys.stdin.readline().split())

alien_dict = []

for _ in xrange(words_no):
    alien_dict.append(sys.stdin.readline().strip())

for no, line in enumerate(sys.stdin):
    pattern = re.compile(line.strip().replace('(', '[').replace(')', ']'))
    print 'Case #%d: %d' % (no + 1, sum(bool(pattern.match(word)) for word in alien_dict))
