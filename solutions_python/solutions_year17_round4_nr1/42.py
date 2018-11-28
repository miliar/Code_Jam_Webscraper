import os
import sys
import math


def readInts(f):
    return [int(k) for k in f.readline().strip().split(' ')]


def Min(a, b):
  if a < b: return a
  return b


def calc(P, A):
  if P == 2:
    return A[0] + math.ceil(A[1] / 2)
  elif P == 3:
    o = Min(A[1], A[2])
    return A[0] + o + math.ceil((A[1] + A[2] - o - o) / 3)
  elif P == 4:
    o = Min(A[1], A[3])
    t = int(A[2] / 2)
    r = A[1] + A[3] - o - o
    ret = A[0] + o + t
    t = A[2] % 2
    if t == 0:
      return ret + math.ceil(r / 4)
    else:
      ret += 1
      r -= 2
      if r > 0: ret += math.ceil(r / 4)
      return ret


if __name__ == "__main__":
    with open('A-large.in', 'r') as f:
        T = int(f.readline())
        for i in range(T):
          N, P = readInts(f)
          A = {0: 0, 1: 0, 2: 0, 3:0}
          for k in readInts(f):
            A[k%P] += 1
          print("Case #%d: %s" % (i+1, calc(P, A)))
