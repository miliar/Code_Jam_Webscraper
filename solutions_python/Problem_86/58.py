#!/usr/bin/env python

import sys

def solve_one(inp):
  N, L, H = map(int,inp.readline().split())
  f = map(int,inp.readline().split())
  for i in xrange(L,H+1):
    next = False
    for j in xrange(len(f)):
      if f[j]%i != 0 and i%f[j] != 0:
        next = True
        break
    if not next:
      return i
  return 'NO'

def solve(inp):
  ret = []
  T = int(inp.readline())
  for i in xrange(T):
    ret.append('Case #%d: %s' % (i+1,solve_one(inp)))
  return '\n'.join(ret)

def main():
  open('.'.join([sys.argv[1].split('.')[0],'out']),'w').write(solve(open(sys.argv[1],'r')))
  print open('.'.join([sys.argv[1].split('.')[0],'out']),'r').read()

if __name__ == '__main__':
  main()
