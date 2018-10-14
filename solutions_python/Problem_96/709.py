#!/usr/bin/env python

import sys

num_lines = int(sys.stdin.readline())

for count in range(0,num_lines):
  sp_line = sys.stdin.readline().split(" ")
  N = int(sp_line[0])
  S = int(sp_line[1])
  p = int(sp_line[2])
  scores = []
  good_scores = 0
  sup_scores = 0
  for i in range(3, len(sp_line)):
    scores.append(int(sp_line[i]))
  for score in scores:
    q = score / 3
    r = score % 3
    if score == 0 or score == 1:
      if score >= p:
        good_scores += 1
    elif r == 0 and q >= p:
      good_scores += 1
    elif r == 0 and q+1 >= p:
      sup_scores += 1
    elif r == 1 and q+1 >= p:
      good_scores += 1
    elif r == 2 and q+1 >= p:
      good_scores += 1
    elif r == 2 and q+2 >= p:
      sup_scores += 1
  total = good_scores + min(S, sup_scores)
  sys.stdout.write("Case #%d: %d\n" % (count+1, total))
