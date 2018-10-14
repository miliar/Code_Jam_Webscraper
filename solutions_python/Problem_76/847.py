#!/usr/bin/env python

import sys

def weird_add(x,y):
  s=0
  c=0
  while x>0 or y>0:
    ss=(x&1)+(y&1)
    if ss==2: ss=0
    s+=ss<<c
    c+=1
    x>>=1
    y>>=1
  return s

def solve_one(inpu):
  inp = map(int,inpu[1].split())
  pile = [0]*len(inp)
  res = [-1]
  
  def r(i):
    if i<0:
      real = [0,0]
      weird = [0,0]
      for j in xrange(len(inp)):
        real[pile[j]] += inp[j]
        weird[pile[j]] = weird_add(weird[pile[j]], inp[j])
      if weird[0] == weird[1] and real[0] > 0 and real[1] > 0:
        #print real,weird
        res[0] = max(res[0], max(real))
      return
    pile[i] = 0
    r(i-1)
    pile[i] = 1
    r(i-1)
  
  r(len(inp)-1)
  if res[0] >= 0:
    return res[0]
  else:
    return 'NO'

def solve(inp):
  ret = []
  T = int(inp[0])
  for i in xrange(T):
    ret.append('Case #%d: %s' % (i+1,solve_one(inp[i*2+1:i*2+3])))
    #print '-'*50
  return '\n'.join(ret)

def main():
  open('.'.join([sys.argv[1].split('.')[0],'out']),'w').write(solve(open(sys.argv[1],'r').readlines()))
  print open('.'.join([sys.argv[1].split('.')[0],'out']),'r').read()

if __name__ == '__main__':
  main()
