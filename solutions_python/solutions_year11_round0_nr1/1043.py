#!/usr/bin/env python

import sys

def sign(x):
  if x == 0:
    return 0
  elif x > 0:
    return 1
  else:
    return -1

def solve_one(inp):
  o = []
  b = []
  s = []
  x = inp.split()[1:]
  for j in xrange(0,len(x),2):
    if x[j] == 'O':
      l = o
      s.append(0)
    else:
      l = b
      s.append(1)
    l.append(int(x[j+1]))
  op = 1
  bp = 1
  oi = 0
  bi = 0
  si = 0
  t = 0
  while si < len(s):
    pushed = False
    t += 1
    if oi < len(o):
      if o[oi] - op == 0 and s[si] == 0:
        #print 'O push button'
        pushed = True
        oi += 1
      else:
        #print 'O move %d' % sign(o[oi] - op)
        op += sign(o[oi] - op)
    if si >= len(s):
      break
    if bi < len(b):
      if b[bi] - bp == 0 and s[si] == 1:
        #print 'B push button'
        pushed = True
        bi += 1
      else:
        #print 'B move %d' % sign(b[bi] - bp)
        bp += sign(b[bi] - bp)
    if pushed:
      si += 1
  return t

def solve(inp):
  ret = []
  T = int(inp[0])
  for i in xrange(T):
    ret.append('Case #%d: %d' % (i+1,solve_one(inp[i+1])))
  return '\n'.join(ret)

def main():
  open('.'.join([sys.argv[1].split('.')[0],'out']),'w').write(solve(open(sys.argv[1],'r').readlines()))
  #print open('.'.join([sys.argv[1].split('.')[0],'out']),'r').read()

if __name__ == '__main__':
  main()
