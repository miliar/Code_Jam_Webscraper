#!/usr/bin/env python

import sys

infile = sys.stdin

def index(char):
    return ord(char)-ord('a')

# Parse header information
[L, D, N] = [int(x) for x in infile.readline().split()]
    
# Setup a lookup data structure
lookup = [[set() for i in range(26)] for i in range(L)]
allwords = set()
for num in range(D):
    word = infile.readline()
    allwords.add(word)
    for pos in range(L):
        lookup[pos][index(word[pos])].add(word)

# Iterate through received words
for num in range(N):
    word = infile.readline().strip()
    matches = set()
    i = 0
    pos = 0
    # print('\nallwords = %s' % allwords)
    # print('word = %s' % word)
    while i < len(word):
        letterwords = set()
        if word[i] == '(':
            while True:
                i += 1
                if (word[i] == ')'):
                    break
                letterwords = letterwords.union(lookup[pos][index(word[i])])
        else:
            letterwords = lookup[pos][index(word[pos])]

        if len(matches) == 0:
            matches = letterwords.copy()
        else:
            matches.intersection_update(letterwords)
        # print('pos = %d, letterwords = %s' % (pos, letterwords));
        # print('matches = %s' % matches)
        if len(matches) == 0:
            break

        i += 1
        pos += 1

    print('Case #%d: %d' % (num + 1, len(matches)))
