import sys

pre = open ("precalc.in", "r")
pres = []
for s in pre:
  pres.append (int(s) ** 2)

n = int (sys.stdin.readline())
for i in range (n):
  l, r = sys.stdin.readline().split()
  l, r = int(l), int(r)
  res = sum (1 for x in pres if l <= x and x <= r)
  print 'Case #' + str(i + 1) + ': ' + str(res)
