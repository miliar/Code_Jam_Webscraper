#!/usr/bin/python

import sys
from math import sqrt

def parse(f):
  n = int(f.readline())
  d = []
  for i in range(n):
    x,y,z,vx,vy,vz=map(int, f.readline().split(' '))
    d.append((x,y,z, vx,vy,vz))
  return d

def solve(o):
  ab = [0,0,0, 0,0,0]
  ab = reduce(lambda a,v: map(sum, zip(a,v)), o, ab)
  ab = map(lambda x: (0.0+x)/len(o), ab)
  B = ab[3]*ab[3] + ab[4]*ab[4] + ab[5]*ab[5]
  if B != 0:
    t = -1 * (ab[0]*ab[3] + ab[1]*ab[4] + ab[2]*ab[5]) / B
  else:
    t = 0
  if t <= 0:
    t = 0
  mind = sqrt(sum(map(lambda xy: (xy[0]+xy[1]*t)*(xy[0]+xy[1]*t), zip(ab[:3],ab[3:]))))
  return t,mind

def main():
  f = sys.stdin
  n = int(f.readline())
  for i in range(n):
    o = parse(f)
    t, mind = solve(o)
    print 'Case #%d: %.8f %.8f' % (i+1, mind, t)

if __name__ == '__main__':
  main()
