#!/usr/local/bin/python

f = open('case', 'r')
f.readline()


def p(m, l):
  s = 0
  rSum = 0 
  for (i, k) in enumerate(l):
    rSum += k
    if k == 0 and rSum < i + 1:
      s += 1
      rSum += 1
  return s

sol = open('ans', 'w')

for (i, l) in enumerate(f):
  k = l.strip("\n")
  k = k.split(" ")

  shy = map(int, list(k[1]))
  a = p(int(k[0]), shy)
  m = "Case #" + str(i + 1) + ": " + str(a) + "\n"
  print m,
  sol.write(m)
