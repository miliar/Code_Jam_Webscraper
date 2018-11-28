#!/usr/bin/env python

import sys

samples = ["ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
trans = ["our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"]

cipher = {'z':'q', 'q':'z'}
for i in range(0,3):
  for j in range(0,len(samples[i])):
    if samples[i][j] != ' ':
      cipher[samples[i][j]] = trans[i][j]

num_lines = int(sys.stdin.readline())
for i in range(0,num_lines):
  line = sys.stdin.readline()
  sys.stdout.write("Case #%d: " % (i+1))
  for c in line:
    if c in cipher:
      sys.stdout.write(cipher[c])
    else:
      sys.stdout.write(c)
