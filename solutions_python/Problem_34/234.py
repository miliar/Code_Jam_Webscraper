#! /usr/bin/evn python

import re

l, d, n = map(int, raw_input().strip().split())

words = []
for i in range(d):
    words.append(raw_input().strip())

for i in range(n):
    k = 0
    guess = raw_input().strip()
    guess = guess.replace('(','[').replace(')',']')
    for word in words:
        if re.match(guess, word):
            k += 1
    print 'Case #%s: %s' %(i + 1, k)
