""" Solution to Google Code Jam 2014 Qualification Problem D

Problem: https://code.google.com/codejam/contest/2974486/dashboard#s=p3

>>> test(
...   testlabel='sample via parse()',
...   testinput='''4
... 1
... 0.5
... 0.6
... 2
... 0.7 0.2
... 0.8 0.3
... 3
... 0.5 0.1 0.9
... 0.6 0.4 0.3
... 9
... 0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899
... 0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458
... ''')  #doctest: +NORMALIZE_WHITESPACE
Case #1: 0 0
Case #2: 1 0
Case #3: 2 1
Case #4: 8 4

"""

import sys, os.path
sys.path.insert(0, os.path.abspath('../.lib'));

from codejam import *

f5 = lambda f: '%.5f' % f

def solve(A, B, N):
  assert N > 0, N
  assert N == len(A) == len(B), [N, len(A), len(B)]

  A.sort()
  B.sort()
  L = N - 1

  if log.debug:
    log.debug(map(f5, A))
    log.debug(map(f5, B))

  D = i = 0
  j = L
  for a in A:
    if a > B[i]:
      D += 1
      if log.debug: log.debug('D+ %d [%d]: %.5f > %.5f' % (D, i, a, B[i]))
      i += 1
    else:
      if log.debug: log.debug('D= %d [%d]: %.5f < %.5f < %.5f' % (D, i, a, B[i], B[j]))
      j -= 1

  W = i = 0
  for a in A:
    while i < N and a > B[i]:
      W += 1
      if log.debug: log.debug('W+ %d [%d]: %.5f > %.5f' % (W, i, a, B[i]))
      i += 1

    if i >= N:
      break

    if log.debug: log.debug('W= %d [%d]: %.5f < %.5f' % (W, i, a, B[i]))
    i += 1

  return D, W

def parse(fi):
  N = int(fi.next().strip())
  A = map(float, fi.next().strip().split())
  B = map(float, fi.next().strip().split())
  return [A, B, N]

def format(r):
  return ' '.join(map(str, r))

if __name__ == '__main__':
    main(solve, parse, format)
