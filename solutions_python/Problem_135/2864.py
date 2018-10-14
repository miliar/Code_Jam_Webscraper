#!/usr/bin/env python

import sys

def rl():
  return sys.stdin.readline().strip()

def solve_one():
  l = []
  for j in xrange(2):
    x = int(rl())
    for i in xrange(4):
      line = rl()
      if i+1==x:
        l.append(set(line.split()))
  l = l[0].intersection(l[1])
  if len(l) == 1:
    return l.pop()
  elif len(l) == 0:
    return 'Volunteer cheated!'
  else:
    return 'Bad magician!'

def main():
  for i in xrange(int(rl())):
    print 'Case #%d: %s' % (i+1,solve_one())

if __name__ == '__main__':
  main()
