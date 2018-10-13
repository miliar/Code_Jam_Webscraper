#!/usr/bin/env python

IN = [
"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"
]

OUT = [
"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"
]

MAP = {}
for j,s in enumerate(IN):
  for i,c in enumerate(s):
    MAP[IN[j][i]] = OUT[j][i]

ALL="abcdefghijklmnopqrstuvwxyz"
MAP['q'] = 'z'
MAP['z'] = 'q'
"""
for c in ALL:
  try:
    print "IN: %s, OUT: %s" % (c, MAP[c])
  except Exception as e:
    print e
"""

def trans(line):
  s = ''
  for c in line:
    s += MAP[c]
  return s

f=open('A-small-attempt0.in.txt')
lines = f.read().split('\n')
for i,line in enumerate(lines[1:]):
  print "Case #%s: %s" % (i+1, trans(line))
