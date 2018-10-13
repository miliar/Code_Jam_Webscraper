#!/usr/bin/env python

import sys

def parse(s):
  a = s.split()
  N = int(a[0])
  pairs = zip(range(0, N), a[1::2], map(int, a[2::2]))
  return N, pairs

def solve(args):
  N, pairs = args
  O = filter(lambda (i, ch, n): ch == 'O', pairs)
  B = filter(lambda (i, ch, n): ch == 'B', pairs)
  lenO = len(O)
  lenB = len(B)
  curGoal = 0
  curO = 0
  curB = 0
  posO = 1
  posB = 1
  step = 0
  # print "N=%d curO=%d curB=%d O=%s B=%s" % (N, curO, curB, str(O), str(B))
  while (curGoal < N):
    pressedO = False
    pressedB = False
    if (curO < lenO and O[curO][0] == curGoal and O[curO][2] == posO):
      # print "i=%d O" % curGoal
      curGoal += 1
      curO += 1
      pressedO = True

    elif (curB < lenB and B[curB][0] == curGoal and B[curB][2] == posB):
      # print "i=%d B" % curGoal
      curGoal += 1
      curB += 1
      pressedB = True

    if (not pressedB):
      if (curB < lenB):
        if (posB < B[curB][2]):
          posB += 1
        elif (B[curB][2] < posB):
          posB -= 1
    if (not pressedO):
      if (curO < lenO):
        if (posO < O[curO][2]):
          posO += 1
        elif (O[curO][2] < posO):
          posO -= 1
    # print "step %d: curGoal=%d curO=%d curB=%d posO=%d posB=%d" % (step, curGoal,  curO, curB, posO, posB)
    step += 1
  return step

def main():
  T = int(sys.stdin.readline())
  for i in range(T):
    print "Case #%d: %d" % (i+1, solve(parse(sys.stdin.readline().strip())))

if __name__ == '__main__':
  main()
