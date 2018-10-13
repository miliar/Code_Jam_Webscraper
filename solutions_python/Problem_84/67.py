#!/usr/bin/env python

import sys

def solve_one(inpu):
  r = len(inpu)
  c = len(inpu[0].strip())
  
  inp = []
  for i in xrange(r):
    inp.append(list(inpu[i].strip()))

  for i in xrange(r):
    for j in xrange(c):
      if inp[i][j] == '#':
        if j+1<c and i+1<r and inp[i][j+1] == '#' and inp[i+1][j] == '#' and inp[i+1][j+1] == '#':
          inp[i][j] = '/'
          inp[i][j+1] = '\\'
          inp[i+1][j] = '\\'
          inp[i+1][j+1] = '/'
        else:
          return '\nImpossible'
  
  ret = []
  for i in xrange(r):
    ret.append(''.join(inp[i]))
  return '\n'+'\n'.join(ret)

def solve(inp):
  ret = []
  T = int(inp[0])
  inp = inp[1:]
  for i in xrange(T):
    R = int(inp[0].split()[0])
    ret.append('Case #%d: %s' % (i+1,solve_one(inp[1:R+1])))
    inp = inp[R+1:]
  return '\n'.join(ret)

def main():
  open('.'.join([sys.argv[1].split('.')[0],'out']),'w').write(solve(open(sys.argv[1],'r').readlines()))
  print open('.'.join([sys.argv[1].split('.')[0],'out']),'r').read()

if __name__ == '__main__':
  main()
