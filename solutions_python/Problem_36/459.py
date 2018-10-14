#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def find_all(text, c):
  indices = []
  for i in range(0, len(text)):
    if text[i] == c:
      indices.append(i)
  return indices

def get_combination(text, sub):
  if len(sub) == 1:
    return len(find_all(text, sub))
  else:
    total = 0
    c = sub[0]
    indices = find_all(text, c)
    for index in indices:
      total += get_combination(text[index:], sub[1:])
    return total

search = "welcome to code jam"
N = int(sys.stdin.readline().strip())
for i in range(0, N):
  text  = sys.stdin.readline().strip()
  count = get_combination(text, search)
  print "Case #%(num)d: %(count)04d" % {"num":i+1, "count":count}
