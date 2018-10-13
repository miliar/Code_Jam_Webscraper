#!/usr/bin/python2
""" INPUT """
import sys
input = sys.argv[1]
output = input.replace('in', 'out')
fin = open(input, 'r')
fout = open(output, 'w')
lines = [line.strip() for line in fin]
lines.reverse()

"""
Maintain a map of patterns to word lists.
Make a new map of patterns ot word lists from previous.
Each word has a score.
"""

def solve(words, orders):
    results = ""
    for order in orders:
        next = dict()
        for w in words:
            pattern = "".join(["-" for c in w])
            if not next.has_key(pattern):
                next[pattern] = []
            next[pattern].append((w,0))
        for c in order:
            prev = next
            next = dict()
            for (pattern, xwords) in prev.items():
                # If character appears "somewhere" in words, then bump up the scores of those w/ none
                # reclassify new patterns
                seen = False
                for (word, score) in xwords:
                    for w in word:
                        if w == c:
                            seen = True
                for (word, score) in xwords:
                    p = ""
                    nothere = True
                    for i in range(len(word)):
                        if word[i] == c:
                            nothere = False
                            p += c
                        else:
                            p += pattern[i]
                    if not next.has_key(p):
                        next[p] = []
                    add = (seen and nothere) and 1 or 0
                    next[p].append((word,score+add))
        score = -1
        for word in words:
            if next[word][0][1] > score:
                score = next[word][0][1]
                result = word
        results += " " + result
    return results.strip()

T = int(lines.pop())
for CASE in range(1,T+1):
    print T
    N,M = (int (x) for x in lines.pop().split(' '))
    words = [lines.pop() for i in range(N)]
    orders = [lines.pop() for i in range(M)]
    result = solve(words,orders)
    fout.write('Case #%s: %s\n' % (CASE, result))
