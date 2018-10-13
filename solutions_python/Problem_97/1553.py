#!/usr/bin/python

def solve():
  n = map(int, raw_input().split())

  if len(n) == 0: return 0
  if n[0] < 10: return 0

  c = 0

  for i in range(n[0], n[1] + 1):
    s = str(i)
    added = []
    for j in range(1, len(s)):
       t = s[-j:] + s[0:-j]
       
       if int(t) <= i: continue
       if int(t) > n[1]: continue
       if t in added: continue

       added.append(t)
#       print i, t
       c += 1
   
  return c

for i in xrange(input()):
  print "Case #%d: %s" % (i+1, solve())



