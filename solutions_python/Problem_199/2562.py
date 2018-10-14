from sys import exit, setrecursionlimit
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

setrecursionlimit(1000000)

T = read()

for testnum in range(1, T+1):
  (S, K) = input().split()
  L = len(S)
  S = [c == "+" for c in S]
  K = int(K)

  result = 0

  for i in range(L-K+1):
    if S[i] == False:
      S[i:i+K] = [not t for t in S[i:i+K]]
      result += 1

  if not all(S):
    result = "IMPOSSIBLE"

  print("Case #{0}: {1}".format(testnum, result))
