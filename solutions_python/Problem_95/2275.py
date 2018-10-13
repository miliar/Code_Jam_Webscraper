#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Apr 13, 2012

@author: daniel

We have come up with the best possible language here at Google, called
Googlerese. To translate text into Googlerese, we take any message and replace
each English letter with another English letter. This mapping is one-to-one and
onto, which means that the same input letter always gets replaced with the same
output letter, and different input letters always get replaced with different
output letters. A letter may be replaced by itself. Spaces are left as-is.

For example (and here is a hint!), our awesome translation algorithm includes
the following three mappings: 'a' -> 'y', 'o' -> 'e', and 'z' -> 'q'. This means
that "a zoo" will become "y qee".

Googlerese is based on the best possible replacement mapping, and we will never
change it. It will always be the same. In every test case. We will not tell you
the rest of our mapping because that would make the problem too easy, but there
are a few examples below that may help.

Given some text in Googlerese, can you translate it to back to normal text?
Solving this problem

Usually, Google Code Jam problems have 1 Small input and 1 Large input. This
problem has only 1 Small input. Once you have solved the Small input, you have
finished solving this problem. Input

The first line of the input gives the number of test cases, T. T test cases
follow, one per line.

Each line consists of a string G in Googlerese, made up of one or more words
containing the letters 'a' - 'z'. There will be exactly one space (' ')
character between consecutive words and no spaces at the beginning or at the end
of any line. Output

For each test case, output one line containing "Case #X: S" where X is the case
number and S is the string that becomes G in Googlerese. Limits

1 ≤ T ≤ 30.
G contains at most 100 characters.
None of the text is guaranteed to be valid English.
Sample

Input
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv


Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
'''

import string

translation = {'a': 'y', 'o': 'e', 'z': 'q'}

# use the examples to populate as much of the mapping as possible.
i1 = 'our language is impossible to understand'
i2 = 'there are twenty six factorial possibilities'
i3 = 'so it is okay if you want to just give up'
o1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
o2 = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
o3 = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'

for i, o in zip(i1, o1):
  translation[i] = o
for i, o in zip(i2, o2):
  translation[i] = o
for i, o in zip(i3, o3):
  translation[i] = o

print len(translation)
print [l for l in string.lowercase if l not in translation]
print [l for l in string.lowercase if l not in translation.values()]

# Process of elimination says 'q' => 'z'
translation['q'] = 'z'

# Create a reverse lookup - we have pre-translated and want to go back to 
# english.
t_rev = dict((v, k) for k, v in translation.items())

with open(r'data/a_small.txt') as fi, open(r'data/a_small_out.txt', 'w') as fo:
  problems = int(fi.readline())

  for i in range(1, problems + 1):
    fo.write('Case #%d: %s' % (i, ''.join(t_rev.get(letter, letter) for letter in fi.readline())))
