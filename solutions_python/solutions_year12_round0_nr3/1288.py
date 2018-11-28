#!/usr/bin/env python3.2

for t in range(int(input())):
  A, B = (int(x) for x in input().split())
  def numRecycledOf(x):
    s = str(x)
    r = (int(s[i:] + s[:i]) for i in range(len(s)))
    return len(set(filter(lambda y: A <= y <= B and x != y, r)))
  print('Case #', t+1, ': ', sum(numRecycledOf(x) for x in range(A,B+1))//2, sep='')
