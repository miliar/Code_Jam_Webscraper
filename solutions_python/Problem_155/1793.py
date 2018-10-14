#!/usr/bin/python

import fileinput

if __name__ == '__main__':
  fin = fileinput.input()
  t = int(fin.readline())
  for i in range(t):
    line = fin.readline()
    m, aud = line.split()
    m = int(m)
    x = 0
    total = 0
    s = 0
    for j in aud:
      c = int(j)
      if c:
        if s > total :
	  x += s - total
	  total += s - total
	total += c
      s += 1
    print 'Case #{0}: {1}'.format(i+1, x)

