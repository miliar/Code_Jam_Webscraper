#!/usr/bin/env python

import fractions

T = int(raw_input())
for case in range(T):
  n, pd, pg = raw_input().split(' ')
  n = int(n)
  pd = int(pd)
  pg = int (pg)
  min_n = 100 / fractions.gcd(100, pd)
  possible = n >= min_n
  if pg == 0:
    possible = possible and pd == 0
  elif pg == 100:
    possible = possible and pd == 100
  print 'Case #%i: %s' % (case+1, 'Possible' if possible else 'Broken')
