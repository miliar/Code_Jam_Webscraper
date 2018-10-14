#!/usr/bin/env python

import sys

def solve_one(inpu):
  inp = inpu.split()
  C = int(inp[0])
  Cs = inp[1:1+C]
  Ds = inp[C+2:-2]
  Ns = inp[-1]

  combine = {}
  for c in Cs:
    combine[''.join([c[0],c[1]])] = c[2]
    combine[''.join([c[1],c[0]])] = c[2]

  opposed = {}
  for d in Ds:
    opposed[d[0]] = d[1]
    opposed[d[1]] = d[0]

  l = []

  for i in xrange(len(Ns)):
    l.append(Ns[i])
    x = ''.join(l[-2:])
    if x in combine:
      l = l[:-2]
      l.append(combine[x])
    if l[-1] in opposed and opposed[l[-1]] in l:
      l = []

  return ''.join(['[', ', '.join(l), ']'])

def solve(inp):
  ret = []
  T = int(inp[0])
  for i in xrange(T):
    ret.append('Case #%d: %s' % (i+1,solve_one(inp[i+1])))
  return '\n'.join(ret)

def main():
  open('.'.join([sys.argv[1].split('.')[0],'out']),'w').write(solve(open(sys.argv[1],'r').readlines()))
  #print open('.'.join([sys.argv[1].split('.')[0],'out']),'r').read()

if __name__ == '__main__':
  main()
