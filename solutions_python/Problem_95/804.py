#!/usr/bin/env python

import sys
import re
from string import ascii_lowercase
from math import sqrt

base_e2g = {'a': 'y', 'o': 'e', 'z': 'q'}
base_g2e = dict((v,k) for k, v in base_e2g.iteritems())

sep = re.compile('\W+')
known_words = map(lambda w: w.lower(), sep.split("""
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
"""))

default_prob = 1./len(ascii_lowercase)
prob_map = dict((g+e, 1.0) for g, e in base_g2e.items()) # probabilities

def get_g_phrases():
    t = int(sys.stdin.readline())
    for i in range(t):
        yield i+1, sys.stdin.readline().strip('\n')

def translate(s, d):
    return ' '.join([translate_word(w, d) for w in s.split(' ')])

def translate_word(w, d):
    return ''.join([d[c] if d.has_key(c) else '.' for c in w])

def search(word, known_words, prob_map):
    pattern = translate_word(word, base_g2e)
    if '.' in pattern:
        for known in known_words:
            if len(pattern) == len(known) and re.match(pattern, known):
                estimate(word, known, prob_map)
    #return normalize_prob_map(prob_map)
    return prob_map

def estimate(word, known, prob_map):
    for i in range(len(word)):
        match = word[i] + known[i]
        old_p = prob_map.get(match, default_prob)
        new_p = old_p + 1 # TODO: multiply with 0.5-0.9 and normalize
        prob_map[match] = new_p
    return prob_map

def normalize_prob_map(prob_map):
    for g in ascii_lowercase:
        total = sum(prob_map.get(g+e, default_prob) for e in ascii_lowercase)
        for e in ascii_lowercase:
            if prob_map.has_key(g+e):
                prob_map[g+e] /= total
    return prob_map

def std_dev(a):
    n = len(a)
    mean = sum(a) / n
    return sqrt(sum((x-mean)**2 for x in a) / n)

def certainty_factor(letter, prob_map):
    values = [prob_map.get(letter+match, default_prob) for match in ascii_lowercase]
    return max(values) * std_dev(values)

def guess_dict(prob_map):
    known_letters = base_g2e.keys()
    remaining_letters = set(ascii_lowercase) - set(known_letters)
    sorted_letters = known_letters + sorted(remaining_letters, key=lambda l: certainty_factor(l, prob_map), reverse=True)
    d = {}
    for letter in sorted_letters:
        best = max([((g, e), p) for (g, e), p in prob_map.items()
                    if g == letter and e not in d.values()] 
                   or [(letter+'.', 0.)], 
                   key=lambda pair: pair[1])
        pair = best[0]
        english = pair[1]
        d[letter] = english
    for g, e in base_g2e.items():
        if d[g] != e:
            print "WTF?!! %s goes to %s instead of %s" % (g, d[g], e)
    return d

# main

phrases = []
for case_no, g_phrase in get_g_phrases():
    phrases.append(g_phrase)
    #print g_phrase
    for word in g_phrase.split(' '):
        prob_map = search(word, known_words, prob_map)

g2e = guess_dict(prob_map)

# determined by running the algorithm on the sample test data
# quoting: 'Googlerese is based on the best possible replacement mapping, and we will NEVER CHANGE it.'
true_dict = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

for i in range(len(phrases)):
    #print "Case #%d: %s" % (i+1, translate(phrases[i], g2e))
    print "Case #%d: %s" % (i+1, translate(phrases[i], true_dict))

