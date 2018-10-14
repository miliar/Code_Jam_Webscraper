#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Apr 13, 2012

@author: daniel


Problem

You're watching a show where Googlers (employees of Google) dance, and then each
dancer is given a triplet of scores by three judges. Each triplet of scores
consists of three integer scores from 0 to 10 inclusive. The judges have very
similar standards, so it's surprising if a triplet of scores contains two scores
that are 2 apart. No triplet of scores contains scores that are more than 2
apart.

For example: (8, 8, 8) and (7, 8, 7) are not surprising. (6, 7, 8) and (6, 8, 8)
are surprising. (7, 6, 9) will never happen.

The total points for a Googler is the sum of the three scores in that Googler's
triplet of scores. The best result for a Googler is the maximum of the three
scores in that Googler's triplet of scores. Given the total points for each
Googler, as well as the number of surprising triplets of scores, what is the
maximum number of Googlers that could have had a best result of at least p?

For example, suppose there were 6 Googlers, and they had the following total
points: 29, 20, 8, 18, 18, 21. You remember that there were 2 surprising
triplets of scores, and you want to know how many Googlers could have gotten a
best result of 8 or better.

With those total points, and knowing that two of the triplets were surprising,
the triplets of scores could have been:

10 9 10
6 6 8 (*)
2 3 3
6 6 6
6 6 6
6 7 8 (*)

The cases marked with a (*) are the surprising cases. This gives us 3 Googlers
who got at least one score of 8 or better. There's no series of triplets of
scores that would give us a higher number than 3, so the answer is 3.

Input

The first line of the input gives the number of test cases, T. T test cases
follow. Each test case consists of a single line containing integers separated
by single spaces. The first integer will be N, the number of Googlers, and the
second integer will be S, the number of surprising triplets of scores. The third
integer will be p, as described above. Next will be N integers ti: the total
points of the Googlers. Output

For each test case, output one line containing "Case #x: y", where x is the case
number (starting from 1) and y is the maximum number of Googlers who could have
had a best result of greater than or equal to p. 
'''

from itertools import combinations_with_replacement as cwr
from collections import defaultdict
from operator import itemgetter

ScoreLookup = defaultdict(set)

for a, b, c in cwr(range(11), 3):
  d1, d2, d3 = abs(a - b), abs(a - c), abs(b - c)
  if any((d1 > 2, d2 > 2, d3 > 2)):
    continue
  special = any((d1 > 1, d2 > 1, d3 > 1))
  ScoreLookup[a + b + c].add(tuple(sorted((a, b, c)) + [special]))

with open(r'data/b_small.txt') as fi, open(r'data/b_small_out.txt', 'w') as fo:
  cases = int(fi.readline())

  for case in range(1, cases + 1):
    ints = map(int, fi.readline().split())
    # Number of Googlers
    N = ints.pop(0)
    # Surprising Triplets
    S = ints.pop(0)
    # p - Best Score test for this round.
    p = ints.pop(0)

    # Result - People who could've scored at least p.
    res = 0

    # The remaining values are individuals total scores
    for score in ints:
      opts = list(ScoreLookup[score])

      # Remove combinations that don't pass for p.
      opts = filter(lambda x: any(y >= p for y in x), opts)

      for a, b, c, special in opts:
        # Score could've been made without being surprising.
        if not special:
          res += 1
          break
        # We can only have up to S surprising triplets.
        if special and S:
          res += 1
          S -= 1
          break

    fo.write('Case #%d: %d\n' % (case, res))
