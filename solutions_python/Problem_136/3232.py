#!/usr/bin/env python
import sys

def min_seconds(C, F, X):
  persec = 2
  secs = 0
  while True:
    if X / persec < C / persec + (X / (persec + F)):
      return X /persec + secs
    secs += C / persec
    persec += F

if __name__ == '__main__':
  lines = map(lambda line: line.strip(), sys.stdin.readlines())
  i = 1
  case = 1
  while i < len(lines):
    C, F, X = map(float, lines[i].split(' '))
    print "Case #%s: %.7f" % (case, min_seconds(C, F, X))
    i += 1
    case += 1
