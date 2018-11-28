#!/usr/bin/env python

import sys

def solve_one(inpu):

  def rotations(n):
    m = 10
    M = 10
    while M<n:
      M*=10
    M/=10

    ret = []
    while n>m:
      if n%m >= m/10:
        a = n%m * M + n/m
        ret.append(a)
      M/=10
      m*=10
    
    return ret

  A,B = map(int,inpu.split())
  ret = 0
  already = {}
  for i in xrange(A,B+1):
    if i % 100000 == 0:
      print i
    for rot in rotations(i):
      if rot != i and A<=rot<=B:
        if i<rot:
          p = (i,rot)
        else:
          p = (rot,i)
        if p not in already:
          already[p]=1
          ret+=1
  return ret

def solve(inp):
  ret = []
  T = int(inp[0])
  for i in xrange(T):
    print i
    ret.append('Case #%d: %d' % (i+1,solve_one(inp[i+1])))
  return '\n'.join(ret)

def main():
  open('.'.join([sys.argv[1].split('.')[0],'out']),'w').write(solve(open(sys.argv[1],'r').readlines()))
  print open('.'.join([sys.argv[1].split('.')[0],'out']),'r').read()

if __name__ == '__main__':
  main()
