#!/usr/bin/env python
# encoding: utf-8
"""
Hang Man

"""

import sys, time
import itertools as it

# debug helper function
DEBUG = True
_debugf = open('/tmp/debug.log', 'w', 0)

def _debug(s):
    if not DEBUG: return
    if type(s) != str: s = repr(s)  
    _debugf.write("%9.3f - %s\n" % (time.clock(), s))



#problem specific functions

def parseInput(f):
    N,M = map(int, f.readline().split())
    words = [f.readline().strip() for _ in range(N)]
    letters = [f.readline().strip() for _ in range(M)]
    return words, letters

def main(args):
    words, lettersList = args
    wordDict = {}
    for word in words:
        _t = wordDict.get(len(word), [])
        _t.append(word)
        wordDict[len(word)] = _t

    #solve problem
    ret = []
    for letters in lettersList:
        bestscore = -1
        bestword = ''
        for word in words:
            posWords = wordDict[len(word)]
            points = 0
            for letter in letters:
                _tWords = filter(lambda x: letter in x, posWords)
                if any(_tWords):
                    if letter in word:
                        hits = map(lambda x: letter == x, word)
                        posWords = filter(lambda w: map(lambda x: letter == x, w) == hits, _tWords)
                    else:
                        posWords = filter(lambda x: letter not in x, posWords)
                        points+=1
            if points > bestscore:
                bestscore = points
                bestword = word
        ret.append(bestword)


    
    return ' '.join(ret)

if __name__ == "__main__":
    if len(sys.argv)==1:
        filename = 'test.in'
    else:
        filename = sys.argv[1]
    
    _debug("Starting %s" % filename)
    f = open(filename)
    cases = int(f.readline())
    for case in range(cases):
        args = parseInput(f)
        print "Case #%i: %s" % (case+1, main(args))
    _debug("Done")