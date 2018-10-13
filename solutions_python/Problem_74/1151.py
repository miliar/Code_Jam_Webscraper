#!/usr/bin/python
import sys

def calc(l):
  time = 0
  loc_o = 1
  loc_b = 1
  last_c_o = 0
  last_c_b = 0
  for type, pos in l:
    if type == "O":
      d = abs(loc_o-pos)
      time += 1 + max(d-(time-last_c_o),0)
      last_c_o = time
      loc_o = pos
    else:
      d = abs(loc_b-pos)
      time += 1 + max(d-(time-last_c_b),0)
      last_c_b = time
      loc_b = pos
  return time

def main():
  d = file(sys.argv[1]).readlines()
  n = int(d[0])
  for j in xrange(1, n+1):
    l = []
    last_color = None
    for i, op in enumerate(d[j][:-1].split()[1:]):
      if (i+1)%2:
        last_color = op
      else:
        l.append((last_color, int(op)))
      
    
    print "Case #%d: %d" % (j, calc(l))

main()
