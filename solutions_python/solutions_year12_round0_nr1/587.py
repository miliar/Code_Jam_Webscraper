#!/usr/bin/python

import sys

#      abcdefghijklmnopqrstuvwxyz
tbl = "yhesocvxduiglbkrztnwjpfmaq"

T = int(sys.stdin.readline())
for i in range(T):
  G = sys.stdin.readline().strip().lower()
  S = ""
  for c in G:
    if c.isalpha():
      S += tbl[ord(c)-ord('a')]
    else:
      S += c
  print "Case #%d: %s" % (i+1,S)

