#!/usr/bin/env python

import collections

import math
import re
import sys

#sys.setrecursionlimit(50)

INPUT = "tiny"
#INPUT = "C-large.in"
INPUT = "C-small-attempt3.in"

def debug(*args):
    return
    sys.stderr.write(str(args) + "\n")

class Memoize:
    def __init__(self,function):
        self._cache = {}
        self._callable = function
            
    def __call__(self, *args, **kwds):
        cache = self._cache
        key = self._getKey(*args,**kwds)
        try: return cache[key]
        except KeyError:
            cachedValue = cache[key] = self._callable(*args,**kwds)
            return cachedValue
    
    def _getKey(self,*args,**kwds):
        return kwds and (args, ImmutableDict(kwds)) or args    


@Memoize
def bit_count(v):
    c = 0
    while v > 0:
        if v & 1:
            c += 1
        v >>= 1
    return c


def show_words(lang, lookup):
    rev = dict((a,b) for b, a in lookup.items())
    t = 0
    while lang > 0:
        if lang & 1:
            debug(rev[t])
        t += 1
        lang >>= 1


def do_trial(sentences):
    words = [set(s.split()) for s in sentences]
    all_words = []
    for s in sentences:
        all_words.extend(s.split())
    all_words = sorted(set(all_words))
    #import pdb; pdb.set_trace()
    word_lookup = dict((w, n) for n, w in enumerate(all_words))
    words_v = []
    for s in sentences:
        v = 0
        for w in s.split():
            v |= (1 << word_lookup[w])
        words_v.append(v)

    english = words_v[0]
    show_words(english, word_lookup)
    debug("-----------")
    french = words_v[1]
    show_words(french, word_lookup)
    debug("-----------")
    both = english & french
    min_both = len(all_words)
    #import pdb; pdb.set_trace()
    c = 2**(len(words)-2)
    i = 0
    while i < c:
        debug(bin(i))
        english = words_v[0]
        french = words_v[1]
        for _, s in enumerate(words_v[2:]):
            which = (i & (1<<_))
            if which:
                english |= words_v[2+_]
            else:
                french |= words_v[2+_]
            both = english & french
            if bit_count(both) > min_both:
                break
                #i = c
                #import pdb; pdb.set_trace()
                #i 
        min_both = min(bit_count(both), min_both)
        i += 1
    return min_both

f = file(INPUT)
T = int(f.readline()[:-1])
for i in range(T):
    N = int(f.readline()[:-1])
    sentences = []
    for _ in range(N):
        sentences.append(f.readline()[:-1])
    #if i == 2:
    #    import pdb; pdb.set_trace()
    v = do_trial(sentences)
    print "Case #%d: %s" % (i+1, v)
