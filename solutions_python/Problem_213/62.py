import sys, re, math

ncases = input()
for icase in range(1, ncases+1):
  n, c, m = map(int, raw_input().split())
  bc = [0]*c
  pc = [0]*n
  for _ in range(m):
    p, b = map(int, raw_input().split())
    pc[p-1] += 1
    bc[b-1] += 1
  res = max(bc)
  sc = 0
  for i in range(n):
    sc += pc[i]
    res = max(res, (sc+i)/(i+1))
  w = 0
  for x in pc:
    if x > res:
      w += (x-res)
  print 'Case #%d: %d %d' % (icase, res, w)
