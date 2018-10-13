#!/usr/bin/env python
import sys

def readline(): return sys.stdin.readline().strip()

T = int(readline())
for t in range(T):
  N = int(readline())
  mt = []
  ms = []
  for n in range(N):
    l = readline()
    row = []
    for r in l:
      row.append(0 if r == '.' else int(r)*2-1)
    ms.append(sum(map(lambda x: 0 if x == 0 else 1, row)))
    mt.append(row)
  wps = []
  for n in range(N):
    wp = sum(map(lambda x: 1 if x == 1 else 0, mt[n])) / float(ms[n])
    wps.append(wp)
  #print(wps)
  owps = []
  for n in range(N):
    owp = 0
    for i in range(N):
      if mt[n][i] == 0: continue
      wins = 0
      matches = 0
      for j in range(N):
        if j == n: continue
        if mt[i][j] == 0: continue
        if mt[i][j] == 1: wins += 1
        matches += 1
      owp += wins/float(matches) if matches > 0 else 0
    owp /= float(ms[n])
    owps.append(owp)
  #print(owps)
  oowps = []
  for n in range(N):
    oowp = 0
    for i in range(N):
      if mt[n][i] == 0: continue
      oowp += owps[i]
    oowp /= float(ms[n])
    oowps.append(oowp)
  #print(oowps)
  print 'Case #%d:' % (t+1)
  for n in range(N):
    print str(0.25*wps[n]+0.50*owps[n]+0.25*oowps[n])


