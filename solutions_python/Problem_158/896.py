#!/usr/local/bin/python

f = open('case', 'r')
t = int(f.readline())

def s(x, r, c):
  g = "GABRIEL"
  h = "RICHARD"

  if x == 1:
    return g
  elif x > 2 and (r == 1 or c == 1):
    return h
  elif x == 2 and ((r*c) % 2 == 1):
    return h
  elif x == 3 and ((r*c) % 3 != 0):
    return h
  elif x == 4 and r*c < 12:
    return h
  return g

for i in xrange(t):
  l = map(int, list(f.readline().split()))
  x = l[0]
  r = l[1]
  c = l[2]
  
  a = s(x, r, c)
  print "Case #" + str(i+1) + ": " + a
