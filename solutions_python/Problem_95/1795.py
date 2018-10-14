#!/usr/bin/env python

import sys

nl = int(sys.stdin.readline())

f = "abcdefghijklmnopqrstuvwxyz"
g = "yhesocvxduiglbkrztnwjpfmaq"
t = str.maketrans(f, g)

for i in range(nl):
  print("Case #%d: %s" % (i + 1, sys.stdin.readline().rstrip('\n').translate(t)))
