#!/usr/bin/env python 
################################################################################
# Jeffrey A. Sandoval
# http://www.cs.rice.edu/~jasandov
#
# Google Code Jam 2009
# Qualification Round
# September 3, 2009
#
# Problem C:  Welcome to Code jam
################################################################################
# This problem can be solved with a recursive depth first search.  To
# be slightly more efficient, I first strip out any irrelevant
# characters from the test string.  Characters are irrelevant if they
# do not appear in the search string.
#
# Then I call a recursive search routine that takes the search string
# and the test string.  The routine returns the number of matches it
# finds.  If the search string is empty, it means we found a match and
# we should return 1.  Next, if the test string is empty then we
# reached the end of the test string without finding a match, so we
# should return 0.
#
# Next, we check matching first characters in the search string and
# test string.  If we find them, we recursively search on the "rest"
# of the two strings (by removing the first character).  We keep track
# of how many matches the recursive call found.
#
# Then we also need to search for matches that don't rely on a match
# for the current character.  We make a recurisve call on the same
# search string but the "rest" of the test string.
#
# Finally, we add up the results of the two recursive calls and return
# it.
#
# Since we only care about the last 4 digits, we should use a modulo
# counter by wrapping around when we hit 10000.
################################################################################

import sys
import logging
import array


#logging.basicConfig(level=logging.DEBUG)

def main():
    input = sys.stdin
    
    # N specifies the number of test cases
    N = int(input.readline().strip())
    logging.info("N = %d", N)

    for i in range(N):
        searchString = "welcome to code jam"
        testString = input.readline().strip()
        findStrings(i + 1, searchString, testString)


def findStrings(index, searchString, testString):
    logging.info("index = %d", index)
    logging.info("searchString = %s", searchString)
    logging.info("testString = %s", testString)
    
    testString = stripIrrelevantCharacters(searchString, testString)
    count = findAllStrings(searchString, testString)
    print "Case #" + str(index) + ": " + str(count % 10000).zfill(4)


def findAllStrings(searchString, testString):
    if (len(searchString) == 0):
        # We found a full string match, and we cannot keep searching
        # since we're out of search characters
        return 1
    if (len(testString) == 0):
        # We reached the end of the search string without a match
        return 0
    
    ret = 0
    if (searchString[0] == testString[0]):
        # We found a character match, so we should keep on searching
        ret += (findAllStrings(searchString[1:], testString[1:]) % 10000)

    # Now advance the testString and look for other matches that don't
    # include a matched character at this point
    ret += (findAllStrings(searchString[:], testString[1:]) % 10000)
    return ret % 10000

def stripIrrelevantCharacters(searchString, testString):
    chars = list(searchString)
    chars.sort()
    i = 0
    while (i + 1 < len(chars)):
        if (chars[i] == chars[i + 1]):
            chars.pop(i)
        else:
            i += 1

    logging.info("Relevant chars = " + str(chars))

    ret = ""
    i = 0
    for c in testString:
        if (c in chars): ret += c
        
    logging.info("Pruned testString = " + str(ret))
    return ret


main()
