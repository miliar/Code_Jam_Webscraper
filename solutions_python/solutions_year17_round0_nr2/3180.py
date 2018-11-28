#!/usr/bin/python

def tidify(k):
  p = 0
  s = []
  for c in k:
    if c < p:
      i = s[len(s)-1] - 1
      s[len(s)-1] = i
      s += [9 for x in range(len(k) - len(s))]
      return tidify(s)
    else:
      s.append(c)
    p = c
  return s
    

n = int(raw_input())
for i in range(1, n+1):
   k = map(int, list(str(raw_input())))
   print "Case #%s: %s" % (i, "".join(map(str, tidify(k))).strip("0"))
