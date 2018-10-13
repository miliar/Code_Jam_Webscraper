import codejam as cj

def IsValid(A, motes):
  sum = A
  for mote in motes:
    if sum <= mote:
      return False
  return True

def sort(l):
  return tuple(sorted(l))

@cj.memoize
def Op(A, motes, n):
  # print(A, motes, n)
  if not motes:
    return n
  if A <= motes[0]:
    if A > 1:
      # return min(Op(A + motes[0] + 1, motes, n+1), Op(A, motes[1:], n+1))
      # return min(Op(A + motes[0] - 1, motes, n+1), Op(A, motes[1:], n+1))
      return min(Op(A + A - 1, motes, n+1), Op(A, motes[1:], n+1))
    return Op(A, motes[1:], n+1)
  return Op(A + motes[0], motes[1:], n)

def ProcessCase(file):
  A, n = cj.IntLine(file.readline())
  motes = cj.IntLine(file.readline())
  motes = sort(motes)
  assert len(motes) == n
  yield A, motes
  
def HandleCase(lines):
  A, motes = lines[0]
  # print(A, motes)
  return Op(A, motes, 0)

cj.HandleCase = HandleCase
cj.ProcessCase = ProcessCase

import sys
sys.setrecursionlimit(100000)
cj.main()
