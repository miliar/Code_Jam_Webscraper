# https://code.google.com/codejam/contest/dashboard?c=2994486#s=p1

FILENAME = "B-small-attempt0"

import sys
sys.stdin = open(FILENAME + ".in", 'r')
sys.stdout = open(FILENAME + ".out", 'w')

def get_int(): return int(get_line())
def get_line(): return raw_input()

def solve():
  A, B, K = map(int, [int(i) for i in get_line().split()])
  win = 0
  for a in range(A):
    for b in range(B):
      if (a & b) < K: win += 1

  return win

for case in range(get_int()):
  print('Case #%d: %d' % (case+1, solve()))
