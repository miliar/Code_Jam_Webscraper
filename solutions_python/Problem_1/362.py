#!/usr/bin/python

import sys

class QuerySolver:
  def __init__(self, S):
    self.S = S
    self.d = {}
    for s in self.S:
      self.d[s] = True
    self.N = len(S) # N left
    self.result = 0

  def query(self, query):
    if self.d[query] and self.N == 1:
      self.result += 1
      for k in self.d.keys():
        self.d[k] = True
      self.N = len(self.d.keys()) - 1
      self.d[query] = False
    elif self.d[query]:
      self.d[query] = False
      self.N -= 1

if __name__ == '__main__':
  if len(sys.argv) != 2:
     print ('Usage: %s file' % sys.argv[0])
     sys.exit(1)

  f = open(sys.argv[1])
  NTEST =  int(f.readline())

  for i in xrange(NTEST):
    print ('Case #%d:' % (i + 1)),

    NS = int(f.readline())
    S = []
    for i in xrange(NS):
      S.append(f.readline()[:-1])

    Solve = QuerySolver(S)

    NQ = int(f.readline())
    for i in xrange(NQ):
      Solve.query(f.readline()[:-1])

    print Solve.result
