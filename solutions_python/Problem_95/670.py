#!/usr/bin/env python

import sys

d = open('dict.txt')
mapping = dict()
mapping['z'] = 'q'
mapping['q'] = 'z'
while True:
  line1, line2 = d.readline(), d.readline()
  if len(line1) == 0:
    break
  for i in range(len(line1)):
    mapping[line1[i]] = line2[i]

n = int(raw_input())

for i in range(n):
  line = raw_input()
  out = ''
  for j in range(len(line)):
    out += mapping[line[j]]
  print 'Case #%d: %s' % (i + 1, out)
