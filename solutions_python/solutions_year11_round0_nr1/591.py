#!/usr/bin/python

fname = 'A-large'

def solve(s):
  tmp = s.split(' ', 1)
  N = int(tmp[0])
  if len(tmp) > 1: s = tmp[1]
  oPos = 1; oTime = 0
  bPos = 1; bTime = 0
  for i in xrange(N):
    tmp = s.split(' ', 2)
    R = tmp[0]
    P = int(tmp[1])
    if len(tmp) > 2: s = tmp[2]
    if R == 'O':
      dTime = oPos - P
      if dTime < 0: dTime = -dTime
      nTime = oTime+dTime
      if nTime<bTime: nTime = bTime
      oTime = nTime+1
      oPos = P
    else:
      dTime = bPos - P
      if dTime < 0: dTime = -dTime
      nTime = bTime+dTime
      if nTime<oTime: nTime = oTime
      bTime = nTime+1
      bPos = P
  if bTime >= oTime: return bTime
  else: return oTime

fin = file(fname+'.in')
T = int(fin.readline().strip())
fout = file(fname+'.out', 'w')
for i in xrange(T):
  fout.write('Case #%s: %s\n' %(i+1, solve(fin.readline())))

