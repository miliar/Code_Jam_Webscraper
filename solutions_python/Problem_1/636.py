#!/usr/bin/python
#
# Author        :   Martin Krivus <martin.krivus@gmail.com>
# Description   :   Saving the Universe 
# Date          :   17.7.2008
#
#

import os
import sys
DEBUG = False 


FILE  = sys.stdin.read()
lines = FILE.split("\n")
CASES = int(lines[0])
if DEBUG:
    print "Number of cases : %s " % CASES

stored = {}

""" DFS """
def rec(stored, MIN, changes, current_engine, engines, ln_e, words, ln_w):
    if ln_w == 0:
        return changes
    if not changes < MIN:
        return changes
    if engines[current_engine] != words[0]:
        key = hash((changes, current_engine, ln_w))
        if stored.has_key(key):
            result =  stored[key]
        else:
            result = rec(stored, MIN, changes, current_engine, engines, ln_e, words[1:], ln_w - 1)
            stored[key] = result
        return result
    else:
        for e in xrange(ln_e):
            if engines[e] != words[0]:
                ch = rec(stored, MIN, changes+1, e, engines, ln_e, words[1:], ln_w - 1)
                if ch < MIN:
                    MIN = ch
        return MIN

""" Test each case """
def test( engines, words ):
    # Max possible
    MIN = 100000
    for e in xrange(len(engines)):
        if words[0] != engines[e]:
            result = rec({}, MIN, 0, e, engines, len(engines), words, len(words))
            if result < MIN:
                MIN = result 

    return MIN


# main
now = 1
for case in xrange(CASES):
    # init lists
    engines = []
    words   = []

    # read num of engines
    engines_count = int(lines[now])
    now += 1 
    # append all engines
    for i in xrange(engines_count):
        engines.append(lines[now])
        now += 1

    # read num of words
    words_count = int(lines[now])
    now += 1
    # append all words
    for i in xrange(words_count):
        words.append(lines[now])
        now +=1

    if DEBUG:
        print "Engines : %s" % ",".join(engines)
        print "Words   : %s" % ",".join(words)
    if words_count > 0:
        result = test(engines, words)
    else:
        result = 0
    print "Case #%s: %s" % (case + 1, result)




