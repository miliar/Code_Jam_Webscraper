#!/usr/bin/env python

import sys
import re

if not len(sys.argv) == 2:
    raise Exception("Missing parameter")

f = open(sys.argv[1], "rU")

word_len, dict_len, test_len = [ int(i) for i in f.next().strip().split() ]

alien_words = set()
for i in xrange(dict_len):
    alien_word = f.next().strip()
    #print "Adding word " + alien_word
    alien_words.add(alien_word)

for i in xrange(test_len):
    test_case = f.next().strip()
    #print "Testing pattern " + alien_word
    test_case = test_case.replace('(', '[').replace(')', ']')
    test_case = re.compile(test_case)
    
    match_count = 0
    for alien_word in alien_words:
        if not (test_case.match(alien_word) is None):
            #print "\tTest case %s matched" % alien_word
            match_count += 1
    print "Case #%d: %d" % (i + 1, match_count)
