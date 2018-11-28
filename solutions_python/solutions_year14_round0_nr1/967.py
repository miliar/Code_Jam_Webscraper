""" Solution to Google Code Jam 2014 Qualification Problem A

Problem statement
=================

Input
-----

Output
------

Limits
------

Doctest
=======

>>> test(
...   testlabel='sample via parse()',
...   testinput='''3
... 2
... 1 2 3 4
... 5 6 7 8
... 9 10 11 12
... 13 14 15 16
... 3
... 1 2 5 4
... 3 11 6 15
... 9 10 7 12
... 13 14 8 16
... 2
... 1 2 3 4
... 5 6 7 8
... 9 10 11 12
... 13 14 15 16
... 2
... 1 2 3 4
... 5 6 7 8
... 9 10 11 12
... 13 14 15 16
... 2
... 1 2 3 4
... 5 6 7 8
... 9 10 11 12
... 13 14 15 16
... 3
... 1 2 3 4
... 5 6 7 8
... 9 10 11 12
... 13 14 15 16
... ''')  #doctest: +NORMALIZE_WHITESPACE
Case #1: 7
Case #2: Bad magician!
Case #3: Volunteer cheated!

"""

import sys, os.path
sys.path.insert(0, os.path.abspath('../.lib'));

from codejam import *

NONE = 'Volunteer cheated!'
MORE = 'Bad magician!'

def solve(A, B):
  A.intersection_update(B);
  if len(A) == 1:
    return A.pop()
  elif len(A) == 0:
    return NONE
  else:
    return MORE

def parse(fi):
  read_token = lambda: fi.next().strip()
  read_tokens = lambda: fi.next().strip().split()
  result = []

  for block in range(2):
    pick = int(read_token()[0]) - 1
    assert 0 <= pick < 4

    for line in range(4):
      if line == pick:
        result.append(set(map(int, read_tokens())))
      else:
        fi.next()

  return result

def format(r):
  return r

if __name__ == '__main__':
    main(solve, parse, format)
