#!/usr/bin/env python

N = int(raw_input())

rate = 2

for case in xrange(N):
  (C, F, X) = map(float, raw_input().split())

  solutions = ([], [])
  solutions[0].append(0.0)
  farm = 0
  while True:
    if farm > 1:
      if solutions[1][-2] < solutions[1][-1]:
        break
    solutions[1].append( X/(2 + farm*F) + solutions[0][-1])
    solutions[0].append( C/(2 + farm*F) + solutions[0][-1] )
    farm += 1

  print 'Case #' + str(case+1) + ': ' + '{0:.8f}'.format(solutions[1][-2])
