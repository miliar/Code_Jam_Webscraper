#!/usr/bin/python
import sys

r1 = lambda: sys.stdin.readline().strip()

N = int(r1())
p = []
a = []
d = dict()
d['a'] = 'y'
d['q'] = 'z'
d['o'] = 'e'
d['z'] = 'q'

for i in range(N):
  p.append(r1())
for i in range(N):
  a.append(r1())

for i in range(N):
  for j in range(len(p[i])):
    d[p[i][j]] = a[i][j]

N = int(r1())
while len(p) != 0:
  p.pop()
while len(a) != 0:
  a.pop()

for i in range(N):
  p.append(r1())

for i in range(N):
  ret = ""
  for j in range(len(p[i])):
    ret = ret + d[p[i][j]]
  print "Case #%d: %s" % (i+1, p[i])