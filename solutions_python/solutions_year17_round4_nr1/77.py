import sys, re, math

ncases = input()
for icase in range(1, ncases+1):
  n, p = map(int, raw_input().split())
  g = map(int, raw_input().split())
  c = [0]*p
  for x in g:
    c[x%p] += 1
  if p == 2:
    res = c[0]+(c[1]+1)/2
  elif p == 3:
    res = c[0]+min(c[1], c[2])+(abs(c[1]-c[2])+2)/3
  else:
    res = c[0]+(c[2]+1)/2+min(c[1], c[3])
    # rest: 211111
    d = abs(c[1]-c[3])
    if c[2] & 1:
      res += c[1]
      d -= 2
    if d > 0:
      res += (d+3)/4
  print 'Case #%d: %d' % (icase, res)
