import os
import sys
import math


def readInts(f):
    return [int(k) for k in f.readline().strip().split(' ')]


def Max(a, b):
  if a < b: return b
  return a


if __name__ == "__main__":
    with open('B-large.in', 'r') as f:
        T = int(f.readline())
        for i in range(T):
            N, C, M = readInts(f)
            pn = [0] * N
            cn = [0] * C
            for j in range(M):
              p, b = readInts(f)
              pn[p-1] += 1
              cn[b-1] += 1
            r = max(cn)
            sumn = 0
            for p in range(N):
              sumn += pn[p]
              r = Max(r, math.ceil(sumn / (p + 1)))
            numPromotion = 0
            for k in pn:
              if k > r:
                numPromotion += k - r
            print("Case #%d: %d %d" % (i+1, r, numPromotion))
