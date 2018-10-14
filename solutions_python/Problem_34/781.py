#!/usr/bin/env python

import re, sys

inputF = sys.stdin

fline = inputF.readline()
L, D, N = map(int, fline.split() )
words = []
for i in range(D):
  line = inputF.readline()
  words.append(line)

for i in range(1, N+1):
  line = inputF.readline()
  word = line.replace('(','[').replace(')',']')
  reg = re.compile(word)
  sum = 0
  for w in words:
    if reg.match(w):
      sum += 1
  print 'Case #%d: %d' % (i, sum)
