#!/usr/bin/env python

import sys

def solve_one(inp):
  l = map(int,inp.readline().split())
  L, t, N, C = l[:4]
  a = l[4:]

  dist = []
  psum = []
  for i in xrange(N):
    dist.append(a[i%C])
    psum.append(sum(dist[:i])*2)
  psum.append(sum(dist)*2)
  res = psum[-1]
  maxgain = 0
  if L > 0:
    for i in xrange(N):
      ti0 = psum[i]
      ti1 = psum[i+1]
      gaini = 0
      boosteri = max(t,ti0)
      if ti0 <= boosteri <= ti1:
        gaini = (ti1-boosteri)/2
      maxgain = max(maxgain, gaini)
      if L > 1:
        for j in xrange(i+1,N):
          tj0 = psum[j]
          tj1 = psum[j+1]
          gainj = 0
          boosterj = max(t,tj0)
          if tj0 <= boosterj <= tj1:
            gainj = (tj1-boosterj)/2
          maxgain = max(maxgain, gaini+gainj)

  return res-maxgain

def solve(inp):
  ret = []
  T = int(inp.readline())
  for i in xrange(T):
    ret.append('Case #%d: %s' % (i+1,solve_one(inp)))
    print ret[-1]
  return '\n'.join(ret)

def main():
  open('.'.join([sys.argv[1].split('.')[0],'out']),'w').write(solve(open(sys.argv[1],'r')))
  #print open('.'.join([sys.argv[1].split('.')[0],'out']),'r').read()

if __name__ == '__main__':
  main()
