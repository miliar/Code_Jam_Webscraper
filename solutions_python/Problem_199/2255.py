#!/usr/bin/python
import sys

def calc(S, K):
  S = [0 if el == "-" else 1 for el in S]
  flips = 0
  for i in xrange(len(S)):
    if S[i] == 0:
      if i <= len(S)-K:
        flips += 1
        for j in xrange(K):
          S[i+j] = 1-S[i+j]
      else:
        return "IMPOSSIBLE"
  
  return str(flips)

def main():
  d = file(sys.argv[1]).readlines()
  n = int(d[0])
  for j in xrange(1,n+1):
    S, K = d[j].split()
    K = int(K)
    print "Case #%d: %s" % (j, calc(S, K))

main()
