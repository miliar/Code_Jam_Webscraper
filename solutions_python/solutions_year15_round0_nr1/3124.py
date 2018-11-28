""" Solution to Google Code Jam 2015 Qualification Problem A

Problem: https://code.google.com/codejam/contest/dashboard?c=6224486#s=p0

>>> test(
...   testlabel='sample via parse()',
...   testinput='''4
... 4 11111
... 1 09
... 5 110011
... 0 1
... ''')  #doctest: +NORMALIZE_WHITESPACE
Case #1: 0
Case #2: 1
Case #3: 2
Case #4: 0
"""

import sys, os.path
sys.path.insert(0, os.path.abspath('../.lib'));

from codejam import *

def solve(S):
  c = 0
  r = 0
  for i, s in enumerate(S):
    if i > c:
       r += i - c
       c = i
       if log.debug: log.debug((i, c, i - c, r))
    c += s

  return r

def parse(fi):
  l, a = fi.next().split()

  l = int(l) + 1
  assert l == len(a), [l, len(a)]

  a = map(int, a)
  return a,

def format(r):
  return r

if __name__ == '__main__':
    main(solve, parse, format)
