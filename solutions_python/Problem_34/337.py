#!/usr/bin/env python 
################################################################################
# Jeffrey A. Sandoval
# http://www.cs.rice.edu/~jasandov
#
# Google Code Jam 2009
# Qualification Round
# September 3, 2009
#
# Problem A:  Alien Language
################################################################################
# This is a matching problem.  There is a given language of D words,
# each of length L, and a given set of test cases.  Each test case
# specifies a word of length L where each letter is either a specific
# letter or a set of possible letters.  The goal is to determine how
# many words in the language could match a given test case.
#
# This problem screams out "regular expressions"!  The test cases can
# be converted to regular expression syntax by replacing the
# parenthesis with brackets.  Then, each word can be tested against a
# given test case simply by testing the regular expression.  We just
# count the matches and output the result.
#
# It occurs to me that this might not be the most efficient method of
# finding matches, since *every* word will be matched against each
# test case.  Instead, it might be possible to prune the search by
# sorting the words of the language into a binary search tree.  Then
# each test case could be treated as a traversal of this binary search
# tree.  Unlike normal binary search, however, we would need to
# accomodate a form of backtracking to handle letters that have
# multiple possibilities.  The advantage of this search is that it
# should be much faster than the brute-force method described above.
# Of course, it would be more complex to code it up, so I'll try the
# brute force.
################################################################################

import sys
import re
import logging

#logging.basicConfig(level=logging.DEBUG)

input = sys.stdin

# L specifies the length of each word in the language
# D specifies the number of words in the alien dictionary
# N specifies tne number of test cases in the input
(L, D, N) = tuple(map(int, input.readline().split()))
logging.info("L = %d", L)
logging.info("D = %d", D)
logging.info("N = %d", N)

# words is a list of the words in the alien language
words = []
for i in range(D):
    words.append(input.readline().strip())
logging.info("words = " + str(words))

# tests is a list of the test cases, which are represented as regular expressions
tests = []
for i in range(N):
    tests.append(input.readline().strip().replace("(", "[").replace(")", "]"))
logging.info("tests = " + str(tests))


# This nested pair of loops attempts to match a given test (the outer
# loop) against every word in the language (the inner loop); the test
# is compiled into a regular expression object so that each word can
# be tested very quickly.  The matches are counted and finally printed
# at the end of the outer loop.
for i in range(len(tests)):
    test = tests[i]
    matches = 0
    pattern = re.compile(test)
    for word in words:
        logging.info("Looking for %s in %s", str(test), str(word))
        if (pattern.match(word)):
            matches += 1
            logging.info("Found %s in %s", str(test), str(word))
    print "Case #" + str(i+1) + ": " + str(matches)
    
