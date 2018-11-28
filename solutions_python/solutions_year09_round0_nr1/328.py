#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
import copy

pattern = re.compile('\(\w+\)|\w')
L, D, N = [int(i) for i in raw_input().split()]
words = set()

def word_filter(word):
    if len(word) > 1:
        return word[1:-1]
    else:
        return word

def check(word_list):
    word_list = map(word_filter, word_list)
    result = copy.deepcopy(words)
    for i in range(len(word_list)):
        result = set([w for w in result if w[i] in word_list[i]])
    return len(result)

for i in range(D):
    word = raw_input()
    words.add(word)

for i in range(N):
    word = raw_input()
    print 'Case #%d: %d' % (i+1, check(pattern.findall(word)))
