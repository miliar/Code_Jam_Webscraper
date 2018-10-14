#pseudocode:
#  keep track of k=stand up level, n=number standing
#  add S[k] to n,
#  add min(k+1 - n,0) to solution and n
#  k++


#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(inp):
  e = inp.split(' ')
  k_max = e[0]
  S = e[1]
  soln = 0
  n = 0

  for k in xrange(len(S)):
    n+=int(S[k])
    need = max(k + 1 - n,0)
    soln+=need
    n+=need
  return soln

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
