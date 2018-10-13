#!/usr/bin/python
import sys

def solve():
  N = int(sys.stdin.readline())
  strs = [sys.stdin.readline().strip() for i in xrange(N)]
  runs = []
  rlens = []
  for sti, st in enumerate(strs):
    rlen = []
    r = -1
    for c, ch in enumerate(st):
      if c == 0 or ch != st[c-1]:
        r += 1
        if sti == 0:
          runs.append(ch)
        elif r >= len(runs) or runs[r] != ch:
          return "Fegla Won"
        rlen.append(1)
      else:
        rlen[-1] += 1
    r += 1
    if r != len(runs):
      return "Fegla Won"
    rlens.append(rlen)
  #print rlens
  #print runs
  cost = 0
  for r in xrange(len(runs)):
    ys = [rlen[r] for rlen in rlens]
    ys.sort()
    # print ys
    bestdsum = sum(abs(y-ys[0]) for y in ys)
    besti = 0
    dsum = bestdsum
    for i in xrange(1,len(ys)):
      delt = ys[i] - ys[i-1]
      dsum += (2*i-len(ys))*delt
      if dsum < bestdsum:
        bestdsum = dsum
        besti = i
      prevdelt = delt
    # print "besti", i, " with dsum" , bestdsum
    #print [(sum(abs(rlen[r] - x) for rlen in rlens)) for x in xrange(1,101)]
    cost += bestdsum
  return cost

T = int(sys.stdin.readline())
for test_case in xrange(1, T+1):
  answer = solve()
  print "Case #{0}: {1}".format(test_case, answer)
